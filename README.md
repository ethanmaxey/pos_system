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
