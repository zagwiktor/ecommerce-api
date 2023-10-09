from django.test import SimpleTestCase
from django.urls import reverse, resolve
from EcommerceAPI.apps.product.views import brand_list, brand_detail, brand_update, brand_create, brand_delete
from rest_framework.test import APITestCase
from EcommerceAPI.apps.product.models import Brand
from EcommerceAPI.apps.product.serializers import BrandSerializer
from rest_framework import status

class ProductApiUrlsTests(SimpleTestCase):
    def test_get_brand_list_is_resolved(self):
        url = reverse('brand-list')
        self.assertEqual(resolve(url).func, brand_list)

    def test_get_brand_detail_is_resolved(self):
        url = reverse('brand-detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func, brand_detail)

    def test_update_brand_is_resolved(self):
        url = reverse('brand-update', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func, brand_update)

    def test_create_brand_is_resolved(self):
        url = reverse('brand-create')
        self.assertEqual(resolve(url).func, brand_create)

    def test_delete_brand_is_resolved(self):
        url = reverse('brand-delete', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func, brand_delete)

class BrandGetTest(APITestCase):
    def setUp(self):
        self.brand1 = Brand.objects.create(name="Brand 1")
        self.brand2 = Brand.objects.create(name="Brand 2")

    def test_brand_list(self):
        response = self.client.get('/api/brand-list/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = BrandSerializer([self.brand1, self.brand2], many=True).data
        self.assertEqual(response.data, expected_data)

    def test_category_detail(self):
        pk = self.brand1.id
        response = self.client.get(f'/api/brand-detail/{pk}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = BrandSerializer(self.brand1, many=False).data
        self.assertEqual(response.data, expected_data)

    def test_category_detail_non_existing(self):
        pk = self.brand1.id + 5
        response = self.client.get(f'/api/brand-detail/{pk}')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {'message': 'Brand is not exists.'})

class BrandPostTest(APITestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name="Brand (test)")

    def test_brand_create(self):
        data = {
            'name': 'Brand'
        }
        response = self.client.post('/api/brand-create/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_brand_create_invalid_data(self):
        data = {}
        response = self.client.post('/api/brand-create/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_brand_update(self):
        data = {
            'name': 'Brand (updated)'
        }
        response = self.client.post(f'/api/brand-update/{self.brand.id}', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_category = Brand.objects.get(pk=self.brand.id)
        self.assertEqual(updated_category.name, data['name'])

    def test_category_update_non_existing(self):
        data = {'name': 'Brand (updated)'}
        non_existing_id = self.brand.id + 5
        response = self.client.post(f'/api/brand-update/{non_existing_id}', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class BrandDeleteTest(APITestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name="Brand (test)")

    def test_product_delete(self):
        response = self.client.delete(f'/api/brand-delete/{self.brand.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Brand.DoesNotExist):
            Brand.objects.get(pk=self.brand.id)

    def test_product_delete_non_existing(self):
        non_existing_id = self.brand.id + 1
        response = self.client.delete(f'/api/brand-delete/{non_existing_id}')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
