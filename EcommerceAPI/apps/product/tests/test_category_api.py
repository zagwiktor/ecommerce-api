from django.test import SimpleTestCase
from django.urls import reverse, resolve
from EcommerceAPI.apps.product.views import category_list, category_detail, category_create, category_update, category_delete
from rest_framework.test import APITestCase
from EcommerceAPI.apps.product.models import Category
from rest_framework import status
from EcommerceAPI.apps.product.serializers import CategorySerializer

class CategoryApiUrlsTests(SimpleTestCase):
    def test_get_category_list_is_resolved(self):
        url = reverse('category-list')
        self.assertEqual(resolve(url).func, category_list)

    def test_get_category_detail_is_resolved(self):
        url = reverse('category-detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func, category_detail)

    def test_update_category_is_resolved(self):
        url = reverse('category-update', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func, category_update)

    def test_create_category_is_resolved(self):
        url = reverse('category-create')
        self.assertEqual(resolve(url).func, category_create)

    def test_delete_category_is_resolved(self):
        url = reverse('category-delete', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func, category_delete)

class CategoryGetTest(APITestCase):
    def setUp(self):
        self.category1 = Category.objects.create(name="Category 1")
        self.category2 = Category.objects.create(name="Category 2")
    def test_category_list(self):
        response = self.client.get('/api/category-list/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = CategorySerializer([self.category1, self.category2], many=True).data
        self.assertEqual(response.data, expected_data)
    def test_category_detail(self):
        pk = self.category1.id
        response = self.client.get(f'/api/category-detail/{pk}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = CategorySerializer(self.category1, many=False).data
        self.assertEqual(response.data, expected_data)

        pk = self.category1.id + 5
        response = self.client.get(f'/api/category-detail/{pk}')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {'message': 'Category is not exists.'})

class CategoryPostTest(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Category 1")
    def test_category_create(self):
        data = {
            'name': 'Test Category',
            'parent': None
        }
        response = self.client.post('/api/category-create/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        invalid_data = {}
        response = self.client.post('/api/category-create/', invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_category_update(self):
        data = {
            'name': 'Category 1 (updated)'
        }
        response = self.client.post(f'/api/category-update/{self.category.id}', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_category = Category.objects.get(pk=self.category.id)
        self.assertEqual(updated_category.name, data['name'])
    def test_category_update_non_existing(self):
        data = {'name': 'Category 1 (updated)'}
        non_existing_id = self.category.id + 5
        response = self.client.post(f'/api/category-update/{non_existing_id}', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CategoryDeleteTest(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Category 1")
    def test_category_delete(self):
        response = self.client.delete(f'/api/category-delete/{self.category.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Category.DoesNotExist):
            Category.objects.get(pk=self.category.id)

    def test_category_delete_non_existing(self):
        non_existing_id = self.category.id + 5
        response = self.client.delete(f'/api/category_delete/{non_existing_id}')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)