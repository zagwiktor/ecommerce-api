# EcommerceAPI

EcommerceApi is a straightforward project in which users can add products, their categories, and brands using an API. The API was built using Django Rest Framework, while for the frontend, I used HTML, CSS, and JavaScript.
# Installation

1. Install Python version 3.11 [(Python)](https://www.python.org/downloads/)

2. Pull the repository

3. I strongly recommend using a specific virtual environment for this project. You can create one by typing the following 
   command:

```bash
python -m venv <name-of-your-enviroment> 
```
* Activate the virtual environment:
Windows
```bash
.\env\Scripts\activate
```
macOS/Linux
```bash
source env/bin/activate
```
* And add them by accessing the interpreter settings and selecting the file from 
the folder where we created our virtual environment (name-of-your-environment -> Scripts -> python.exe).

4. To install all necessary libraries in the project terminal, type in:

```bash
pip install -r requirements.txt
```

# Documentation

## Adding or retrieving products

Allowed methods:

>POST, GET

POST: 
>/api/product-create/
> 
Request body pattern:
```bash
{
        "id": 2,
        "name": "Example product",
        "description": "Example description",
        "available": true,
        "date_added": "2023-10-12",
        "brand": 3,
        "category": 1
},
```
GET (list): 
>/api/product-list/

Example response:
```bash
[
    {
        "id": 3,
        "name": "Example product 2",
        "description": "Example description 2",
        "available": true,
        "date_added": "2023-10-12",
        "brand": 3,
        "category": 1
    },
    {
        "id": 2,
        "name": "Example product",
        "description": "Example description",
        "available": true,
        "date_added": "2023-10-12",
        "brand": 3,
        "category": 1
    }
]
```
UPDATE:
>/api/product-update/{id}

Request body pattern:
```bash
{
        "id": 2,
        "name": "Example product (UPDATED)",
        "description": "Example description",
        "available": true,
        "date_added": "2023-10-12",
        "brand": 3,
        "category": 1
},
```
## Deleting products

>/api/product-delete/{id}


Allowed methods:

>DELETE

This endpoint will delete product associated with provided id.

# The appearance of EcommerceApi

![image](https://github.com/zagwiktor/ecommerce-api/assets/92055936/fe076d37-12a7-41cd-9f70-53720d38a7f5)
