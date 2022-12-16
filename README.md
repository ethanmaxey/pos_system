# Point of Sale Project – Group 1

## To Access the Website

[pos4.azurewebsites.net](https://pos4.azurewebsites.net/)

Username: admin
Password: password#1

## Type of Database Application we have Built<br>
In this project, we have developed a point-of-sale database application for a grocery store that sells the different kinds of produce you would typically see at a grocery store. 
## Types of Data that can be Manipulated<br>
The types of data that can be added, modified, and edited is the data associated with the employees (their username, email address, first name, last name, and whether or not they are a staff member), the vendors (vendor name, id, address, and whether or not they need an order request), the customers (first name, last name, email address, and username), the product categories (category id, name, and date updated), and finally the products (product name, description, price, amount, date updated, and their vendor id).
## User Roles
1.  Users/Customers<br>
  a.  Customers can see the products on the shop page<br>
2.	Employees<br>
  a.  Can see all of the sales they have made on the dashboard<br>
  b.  The customers who’ve ordered from our store<br>
  c.  The product categories<br>
  d.  The products themselves<br>
  e.	And finally the transactions<br>
3.	Administrators<br>
  a.	Can see everything that the customer and the employees can see<br>
  b.  And all of the reports<br>
## Semantic Constraints<br>
1.  Trigger 1 (Holiday Discount) <br>
  a.  	If the transaction date occurs on a particular date defined in the trigger, we give           the customer a 10% discount<br>
    1.	We make sure semantic integrity is followed through the following:<br>
      a.  Making sure the transaction date is indeed a date<br>
      b. 	We also check to make sure the date lies on a holiday in order to provide the                 customer with a discounted price on their item of choice<br>
2.	Trigger 2 (Alert Vendor)<br>
  a.  If the amount of a particular product reaches below 50, we set the need_order attribute   in the table vendor to either true if the vendor needs to order more product, and false       if otherwise<br>
    1.  We make sure semantic integrity is followed by:<br>
      a.	Ensuring the amount of product can only be entered as a integer<br>
      b.	We check to see if the amount of product is less than 50, if so we set the Boolean             attribute need_order to true and false otherwise<br>
## Queries/Reports<br>
1. 	Sales report of the Employees
2.	Transaction table + auth_user table
3.	Total sales for each product category
4.	Category table + transaction table
5.	Sales by date
6.	Transaction table




# Git Workflow
## One Time Setup
1. git clone https://github.com/kundanpaudel/pos_11-21
2. cd pos_11-21
3. git checkout "<YOUR_NAME>"

## Merge Lifecycle
1. Make your changes and test along the way
2. git add -A
3. git commit -m "..." # The commit messages should be verbose describing the purpose of the changes you made
4. git pull origin master
5. TEST and fix anything that is broken - Only push working changes!
6. git push origin "<YOUR_NAME>" # Never push to master directly!
7. Let Ethan know you have changes that are ready to be merged
8. Ethan will test your changes locally.
9. Ethan will merge your branch into `master`.

## MySQL Migrations

1. Create schema in database and load all tables, triggers etc.
2. Make sure models.py does not have any classes in them.
3. Make sure you comment out everything imported from models.py in views.py.
4. Run 'python manage.py migrate'
5. Run 'python manage.py inspectdb > (filename).py' . In the (filename ) put any name you like. This file will be created wherever your models.py is located. This basically pulls all tables from database and create classes from it. 
6. Copy/paste the classes ypu want from the created file to models.py. the classes will have meta field with db_table:'tablename' inside each of them. 
