from django.test import SimpleTestCase
from django.urls import reverse, resolve
from EcommerceAPI.apps.product.views import product_list, product_detail, product_update, product_create, product_delete
from rest_framework.test import APITestCase
from EcommerceAPI.apps.product.models import Product, Brand
from rest_framework import status
from EcommerceAPI.apps.product.serializers import ProductSerializer

class ProductApiUrlsTests(SimpleTestCase):
    def test_get_product_list_is_resolved(self):
        url = reverse('product-list')
        self.assertEqual(resolve(url).func, product_list)

    def test_get_product_detail_is_resolved(self):
        url = reverse('product-detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func, product_detail)

    def test_update_product_is_resolved(self):
        url = reverse('product-update', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func, product_update)

    def test_create_product_is_resolved(self):
        url = reverse('product-create')
        self.assertEqual(resolve(url).func, product_create)

    def test_delete_product_is_resolved(self):
        url = reverse('product-delete', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func, product_delete)

class ProductGetTest(APITestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name="test")
        self.product1 = Product.objects.create(name="Product 1", description='test', available=False, brand=self.brand)
        self.product2 = Product.objects.create(name="Product 2", description='test', available=False, brand=self.brand)

    def test_product_list(self):
        response = self.client.get('/api/product-list/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        products = Product.objects.all().order_by('-id')
        expected_data = ProductSerializer(products, many=True).data
        self.assertEqual(response.data, expected_data)

    def test_product_detail(self):
        pk = self.product2.id
        response = self.client.get(f'/api/product-detail/{pk}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_product_detail_non_existing(self):
        non_existing_id = self.product2.id + 1
        response = self.client.get(f'/api/product_detail/{non_existing_id}')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class ProductPostTest(APITestCase):

    def setUp(self):
        self.brand = Brand.objects.create(name="test")
        self.product = Product.objects.create(name="Test Product", description='test', available=False, brand=self.brand)

    def test_product_create(self):
        data = {
            'name': 'Test Product',
            'description': 'Test',
            'brand': f'{self.brand.pk}'
        }
        response = self.client.post('/api/product-create/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_product_invalid_data(self):
        data = {}
        response = self.client.post('/api/product-create/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_product_update(self):
        data = {
            'name': 'Test Product (updated)',
            'description': 'Test',
            'brand': f'{self.brand.pk}'
        }
        response = self.client.post(f'/api/product-update/{self.product.pk}', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_product = Product.objects.get(pk=self.product.id)
        self.assertEqual(updated_product.name, data['name'])

    def test_category_update_non_existing(self):
        data = {
            'name': 'Test Product (updated)',
            'description': 'Test',
            'brand': f'{self.brand.pk}'
        }
        non_existing_id = self.product.pk + 5
        response = self.client.post(f'/api/product-update/{non_existing_id}', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class ProductDeleteTest(APITestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name="test")
        self.product = Product.objects.create(name="Test Product", description='test', available=False, brand=self.brand)

    def test_product_delete(self):
        response = self.client.delete(f'/api/product-delete/{self.product.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Product.DoesNotExist):
            Product.objects.get(pk=self.product.id)

    def test_product_delete_non_existing(self):
        non_existing_id = self.product.id + 1
        response = self.client.delete(f'/api/product-delete/{non_existing_id}')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)