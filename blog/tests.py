from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Post
# Create your tests here.


# class PostModelTest(TestCase):

#     def setUp(self):
#         Post.objects.create(post_title='just a test')

#     def test_text_content(self):
#         post=Post.objects.get(id=1)
#         expected_object_name= f'{post.post_title}'
#         self.assertEqual(expected_object_name, 'just a test')

# class Blog(TestCase):
    
#     def setUp(self):
#         Post.objects.create(post_title='this is another test.')
    
#     def test_view_url_exists_at_proper_location(self):
#         resp = self.client.get('/blog/')
#         self.assertEqual(resp.status_code,200)
    
#     def test_view_url_by_name(self):
#         resp = self.client.get(reverse('blog'))
#         self.assertEqual(resp.status_code, 200)
    
#     def test_view_uses_correct_template(self):
#         resp = self.client.get(reverse('blog'))
#         self.assertEqual(resp.status_code, 200)
#         self.assertTemplateUsed(resp, 'blog.html')

class BlogTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.post = Post.objects.create(
            post_title = 'A good title',
            post = 'Nice body content',
            author = self.user
        )

    def test_string_representation(self):
        post = Post(post_title = 'A sample title')
        self.assertEqual(str(post), post.post_title)
    
    def test_post_content(self):
        self.assertEqual(f'{self.post.post_title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.post}', 'Nice body content')
    
    def test_post_list_view(self):
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'blog.html')

    def test_post_detail_view(self):
        response = self.client.get('/blog/1/')
        no_response = self.client.get('/blog/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')