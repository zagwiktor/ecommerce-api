from django.shortcuts import render
import requests
# Create your views here.
def list_product(request):
    api_url_category = f"http://127.0.0.1:8000/api/category-list/"
    api_url_brand = f"http://127.0.0.1:8000/api/brand-list/"

    response_category = requests.get(api_url_category)
    data_category = response_category.json()
    data_category_filtered = []
    for item in data_category:
        new_item = {'id': item['id'], 'name': item['name']}
        data_category_filtered.append(new_item)


    response_brand = requests.get(api_url_brand)
    data_brand = response_brand.json()



    context = {"categories": data_category_filtered, "brands": data_brand}

    return render(request, 'frontend/list.html', context)