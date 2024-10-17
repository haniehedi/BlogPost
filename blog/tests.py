from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post, Author

class BlogTests(APITestCase):

    def setUp(self):
        self.author = Author.objects.create(name="mahdie", email="m@gmail.com")
        self.post = Post.objects.create(
            title='Test Post',
            content='Content for the test post',
            author=self.author
        )

    def test_get_posts(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        data = {
            'title': 'New Post',
            'content': 'Content of new post',
            'author': {
                'name': "Test Author",
                'email': "test_author@example.com"
            }
        }
        response = self.client.post(reverse('post_list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_post(self):
        data = {
            'title': 'Updated Post Title',
            'content': 'Updated content',
            'author': {
                'name': "Test Author",
                'email': "test_author@example.com"
            }
        }
        response = self.client.put(reverse('post_detail', kwargs={'pk': self.post.pk}), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_post(self):
        response = self.client.delete(reverse('post_detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
