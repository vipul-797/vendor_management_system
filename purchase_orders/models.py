from django.db import models
from vendor_profiles.models import Vendor, HistoricalPerformance
from django.db.models import Avg, Count, signals
from django.utils.timezone import now

STATUS = (
    ("pending", "pending"),
    ("completed", "completed"),
    ("canceled", "canceled"),
)

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=10)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=now)
    delivery_date = models.DateTimeField()
    items = models.JSONField(default=dict)
    quantity = models.PositiveIntegerField(default=0)
    status = models.CharField(choices=STATUS, max_length=100)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.po_number
    
def historical_performance_handler(sender, instance, **kwargs):
    po = PurchaseOrder.objects.filter(vendor=instance.vendor)
    
    po_count = po.count()
    completed_po_count = po.filter(status="completed").count()

    on_time_delivery_rate = completed_po_count / po_count if po_count > 0 else 0

    quality_rating_avg = po.filter(quality_rating__isnull=False).aggregate(quality_rating_avg=Avg('quality_rating'))
    quality_rating_avg = quality_rating_avg.get('quality_rating_avg', 0)

    avg_response_time_seconds = po.aggregate(avg_response_time=Avg(models.F('delivery_date') - models.F('acknowledgment_date')))
    avg_response_time_seconds = avg_response_time_seconds.get('avg_response_time', 0).total_seconds()

    fulfilment_rate = completed_po_count / po_count if po_count > 0 else 0

    # Create HistoricalPerformance object with converted avg_response_time
    HistoricalPerformance.objects.create(
        vendor=instance.vendor,
        on_time_delivery_rate=on_time_delivery_rate,
        quality_rating_avg=quality_rating_avg,
        average_response_time=avg_response_time_seconds,  # Store as numeric value in seconds
        fulfillment_rate=fulfilment_rate,
    )

signals.post_save.connect(historical_performance_handler, sender=PurchaseOrder)
