# crud_operation
1)Here first you ahve to setup the project you can use virtual environment or you can setup it your own system

# Install dependencies from requirements.txt
pip install -r requirements.txt

# After this you have to edite the mysql detail in the settings.py
put your mysql things in it 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'crud_assignment',
        'USER': 'root',
        'PASSWORD': 'Sam@#123',
        'HOST': 'localhost',  
        'PORT': '3306',  
    }
}


# now you have to migrate it using commands
a) python manage.py makemigrations
b) python manage.py migrate

# after this you have to create a super using using this command for creating the taken
cmd = python manage.py createsuperuser

Here you have to enter the username and password 

#### after all these steps you can run the project and here are the other steps

NOTE = There are 5 api's in this project and they are like this 

A) first you have to crearte token using the username and passowrd that you have created in createsuperuser command 
# ###########################################  1st API ###################################################
**FIRST API TOKEN CREATION**
url = http://127.0.0.1:8000/crud_app/token/
body(json) = 
{
  "username": "admin",
  "password": "Admin123"
}

# RESPONSE 
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0MjcyMDIxMywiaWF0IjoxNzQyNjMzODEzLCJqdGkiOiI0ZGMwMmIyM2Y4YmE0NzFkYTg3OGNlODkyNzEwNzQ3OSIsInVzZXJfaWQiOjF9.YOVOrUWieR6HugKmY1Feg-ec6S1iMJT9hTUTZNqWjQc",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQyNjM0MTEzLCJpYXQiOjE3NDI2MzM4MTMsImp0aSI6ImY1MzE4MjZlOWFjYzRkMGI4ODFhOWZkOTgzNTIxNTgyIiwidXNlcl9pZCI6MX0.9aHvx7zn6NT8T-0izuct7AGXUIItTzMDs8JDz91t2WU"
}


# ###########################################  2ND API ###################################################

**DATA CREATION API**
url = http://127.0.0.1:8000/crud_app/create/
body(json) = 
# request for single data creation 
{
    "name": "Item 1",
    "description": "Description for Item 1"
}

# request for bulk data creation
[
    {"name": "Item 1", "description": "Description for Item 1"},
    {"name": "Item 2", "description": "Description for Item 2"},
    {"name": "Item 3", "description": "Description for Item 3"},
    {"name": "Item 4", "description": "Description for Item 4"},
    {"name": "Item 5", "description": "Description for Item 5"},
    
]

header(bulk edite) = 
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQyNjM0MTEzLCJpYXQiOjE3NDI2MzM4MTMsImp0aSI6ImY1MzE4MjZlOWFjYzRkMGI4ODFhOWZkOTgzNTIxNTgyIiwidXNlcl9pZCI6MX0.9aHvx7zn6NT8T-0izuct7AGXUIItTzMDs8JDz91t2WU

## RESPONSE
{
    "message": "All items inserted successfully",
    "status": 201
}

# ###########################################  3rd API ###################################################

**DATA LISTING API**
url = http://127.0.0.1:8000/crud_app/list/

header(bulk edite) = 
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQyNjM0MTEzLCJpYXQiOjE3NDI2MzM4MTMsImp0aSI6ImY1MzE4MjZlOWFjYzRkMGI4ODFhOWZkOTgzNTIxNTgyIiwidXNlcl9pZCI6MX0.9aHvx7zn6NT8T-0izuct7AGXUIItTzMDs8JDz91t2WU

## RESPONSE
{
    "data": [
        {
            "id": 1,
            "name": "Updated Item Name",
            "description": "Updated Description"
        },
        {
            "id": 2,
            "name": "Item 2",
            "description": "Description for Item 2"
        },
        {
            "id": 3,
            "name": "Item 3",
            "description": "Description for Item 3"
        },
        {
            "id": 4,
            "name": "Item 4",
            "description": "Description for Item 4"
        },
        {
            "id": 5,
            "name": "Item 5",
            "description": "Description for Item 5"
            
        }
    ],
    "count_of_data": 39,
    "count_of_pages": 8,
    "status": 200,
    "message": "Items retrieved successfully."
}





# ###########################################  4th API ###################################################

**DATA UPDATING API**
url = http://127.0.0.1:8000/crud_app/update/1/   
# here in place of one you have have to send id you want to update

body(json) = 
{
  "name": "Updated ",
  "description": "Updated Desc1"
}

header(bulk edite) = 
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQyNjM0MTEzLCJpYXQiOjE3NDI2MzM4MTMsImp0aSI6ImY1MzE4MjZlOWFjYzRkMGI4ODFhOWZkOTgzNTIxNTgyIiwidXNlcl9pZCI6MX0.9aHvx7zn6NT8T-0izuct7AGXUIItTzMDs8JDz91t2WU

## RESPONSE
{
    "message": "Item successfully updated.",
    "data": {
        "id": 1,
        "name": "Updated",
        "description": "Updated Desc1"
    },
    "status": 200
}





# ###########################################  5th API ###################################################

**DATA DELETING API**
url = http://127.0.0.1:8000/crud_app/delete/39/
## 39 is the id of that dta i want to delete
header(bulk edite) = 
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQyNjM0MTEzLCJpYXQiOjE3NDI2MzM4MTMsImp0aSI6ImY1MzE4MjZlOWFjYzRkMGI4ODFhOWZkOTgzNTIxNTgyIiwidXNlcl9pZCI6MX0.9aHvx7zn6NT8T-0izuct7AGXUIItTzMDs8JDz91t2WU

## RESPONSE
{
    "message": "Item successfully deleted.",
    "status": 204
}
