from django.test import TestCase #using database this time
from .models import Posts 
from django.urls import reverse

# Create your tests here.
class PostModelTest(TestCase): 
    'testing to check database content is correct with what is inputted'

    def setUp(self):
        'creating a test database and creating an id with a text in it '
        Posts.objects.create(text='just a test')

    def test_text_content(self):
        'cross checking text in database is same with argument provided'
        post = Posts.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name,'just a test')


class HomePageViewTest(TestCase):
    ' Specifically, we want to test that it exists (throwsan HTTP 200 response), uses thehomeview, and uses thehome.htmltemplate'

    def setup(self):
        Post.obejcts.create('this is another test')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code,200)
    
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code,200)
    
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp, 'home.html')
        