from django.test import TestCase
from .models import Post
from django.urls import reverse

# Create your tests here.

# Testing the Model
class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='Testing: just a simple comment')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'Testing: just a simple comment')

# Test Hompage --> see if it exists
class HomePageViewsTest(TestCase):

    def setUp(self):
        Post.objects.create(text='This is another Test')
    
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_views_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')


