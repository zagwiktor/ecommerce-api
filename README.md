# EcommerceAPI

EcommerceApi is a straightforward project in which users can add products, their categories, and brands using an API. The API was built using Django Rest Framework, while for the frontend, I used HTML, CSS, and JavaScript.

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