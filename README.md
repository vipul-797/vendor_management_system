# vendor_management_system
This Vendor Management System is built using Django and Django REST Framework. It allows you to manage vendor profiles, track purchase orders, and evaluate vendor performance metrics.

*Login Credentials:*
```
username: admin
password: admin
```


Core Features
Vendor Profile Management
Create, update, delete, and retrieve vendor profiles.
Purchase Order Tracking
Manage purchase orders with details like PO number, vendor reference, items, quantity, and status.
Vendor Performance Evaluation
Calculate performance metrics such as on-time delivery rate, quality rating, response time, and fulfilment rate for vendors.


###  Vendor Profile Management:

● POST /api/vendors/: Create a new vendor.
● GET /api/vendors/: List all vendors.
● GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.
● PUT /api/vendors/{vendor_id}/: Update a vendor's details.
● DELETE /api/vendors/{vendor_id}/: Delete a vendor

### Purchase Order Tracking:

● POST /api/purchase_orders/: Create a purchase order.
● GET /api/purchase_orders/: List all purchase orders with an option to filter by
vendor.
● GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
● PUT /api/purchase_orders/{po_id}/: Update a purchase order.
● DELETE /api/purchase_orders/{po_id}/: Delete a purchase order.

###  Vendor Performance Evaluation:

● GET /api/vendors/{vendor_id}/performance: Retrieve a vendor's performance
metrics.


### Use Swagger UI to test the API

* Go to http://localhost:8000/swagger/

* Click on "Authorize" button on the top right corner

* Enter the following credentials:
```
tokenAuth (apiKey) : "Token e9c99278469375ec523d76d38ae2c33cb9d8a3b3"
```
and click on "Authorize" button

* Now you can test the API. Click on any endpoint and then click on "Try it out" button. Enter the required parameters and click on "Execute" button.

## Screenshots
![image](https://github.com/vipul-797/vendor_management_system/assets/83302716/6b806a8b-4fc2-4d21-ae19-85ec5d7884f8)


![image](https://github.com/vipul-797/vendor_management_system/assets/83302716/1ffc62fc-7331-40df-a83c-c7faabfbbb29)


![image](https://github.com/vipul-797/vendor_management_system/assets/83302716/ce974add-4e69-46fb-a263-3e02760a1977)


![image](https://github.com/vipul-797/vendor_management_system/assets/83302716/e8bbb90c-4548-43a9-b269-48cc42a8a311)


![image](https://github.com/vipul-797/vendor_management_system/assets/83302716/f22afad0-515f-47d5-a57b-abf1f66c8b79)


![image](https://github.com/vipul-797/vendor_management_system/assets/83302716/49ee5322-5920-466a-8e86-bcac0c879a16)



![image](https://github.com/vipul-797/vendor_management_system/assets/83302716/a740da20-ddc1-4277-9971-f5071ee449d3)


![image](https://github.com/vipul-797/vendor_management_system/assets/83302716/586de5c7-38be-4172-a691-5b2d35f66896)




