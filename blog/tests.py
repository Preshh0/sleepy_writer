from django.test import TestCase
from django.urls import reverse
from .models import Post
# Create your tests here.


class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(post_title='just a test')

    def test_text_content(self):
        post=Post.objects.get(id=1)
        expected_object_name= f'{post.post_title}'
        self.assertEqual(expected_object_name, 'just a test')

