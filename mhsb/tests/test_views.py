from django.test import TestCase
from django.urls import reverse
from ..models import Post_1,Post_2,Post_3,Post_4,Comment_1,Comment_2,Comment_3,Comment_4
from ..forms import PostForm_1,PostForm_2,PostForm_3,PostForm_4,CommentForm_1,CommentForm_2,CommentForm_3,CommentForm_4
from mhsb.views import *
from django.utils import timezone

class HomeTests(TestCase):

  def test_get(self):
    """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
    response = self.client.get(reverse('index'))
    self.assertEqual(response.status_code, 200)

class WeaponTests(TestCase):

  def test_get(self):
    """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
    response = self.client.get(reverse('weapon'))
    self.assertEqual(response.status_code, 200)

class SousyokuTests(TestCase):

  def test_get(self):
    """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
    response = self.client.get(reverse('sousyoku'))
    self.assertEqual(response.status_code, 200)

class KyoukaTests(TestCase):

  def test_get(self):
    """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
    response = self.client.get(reverse('kyouka'))
    self.assertEqual(response.status_code, 200)
    
    
 
    
    
class FormListTests_1(TestCase):
  def setUp(self):
    self.post = Post_1.objects.create(
        user = 'test_user',
        content = 'test_content',
        picture = 'test_picture',
        created = timezone.now(),
    )
    self.post.save()
    
  def test_get(self):
    """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
    
    self.post = Post_1.objects.create()
    response = self.client.get(reverse('formlist_1'))
    self.assertEqual(response.status_code, 200)

class DetailTests_1(TestCase):
  def setUp(self):
    self.post = Post_1.objects.create(
        user = 'test_user',
        content = 'test_content',
        picture = 'test_picture',
        created = timezone.now(),
    )
    self.post.save()
    
  def test_get(self):
    """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
    
    self.post = Post_1.objects.create()
    response = self.client.get(reverse('post_detail_1',args=[self.post.pk]))
    self.assertEqual(response.status_code, 200)
    
    
    
    
    
    
class FormListTests_2(TestCase):
  def setUp(self):
    self.post = Post_2.objects.create(
        user = 'test_user',
        content = 'test_content',
        picture = 'test_picture',
        created = timezone.now(),
    )
    self.post.save()
    
  def test_get(self):
    """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
    
    self.post = Post_2.objects.create()
    response = self.client.get(reverse('formlist_2'))
    self.assertEqual(response.status_code, 200)
    

class DetailTests_2(TestCase):
  def setUp(self):
    self.post = Post_2.objects.create(
        user = 'test_user',
        content = 'test_content',
        picture = 'test_picture',
        created = timezone.now(),
    )
    self.post.save()
    
  def test_get(self):
    """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
    
    self.post = Post_2.objects.create()
    response = self.client.get(reverse('post_detail_2',args=[self.post.pk]))
    self.assertEqual(response.status_code, 200)






class FormListTests_3(TestCase):
  def setUp(self):
    self.post = Post_3.objects.create(
        user = 'test_user',
        content = 'test_content',
        picture = 'test_picture',
        created = timezone.now(),
    )
    self.post.save()
    
  def test_get(self):
    """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
    
    self.post = Post_3.objects.create()
    response = self.client.get(reverse('formlist_3'))
    self.assertEqual(response.status_code, 200)


class DetailTests_3(TestCase):
  def setUp(self):
    self.post = Post_3.objects.create(
        user = 'test_user',
        content = 'test_content',
        picture = 'test_picture',
        created = timezone.now(),
    )
    self.post.save()
    
  def test_get(self):
    """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
    
    self.post = Post_3.objects.create()
    response = self.client.get(reverse('post_detail_3',args=[self.post.pk]))
    self.assertEqual(response.status_code, 200)
    
    
 
 
 
 
class FormListTests_4(TestCase):
  def setUp(self):
    self.post = Post_4.objects.create(
        user = 'test_user',
        content = 'test_content',
        picture = 'test_picture',
        created = timezone.now(),
    )
    self.post.save()
    
  def test_get(self):
    """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
    
    self.post = Post_4.objects.create()
    response = self.client.get(reverse('formlist_4'))
    self.assertEqual(response.status_code, 200)
   
class DetailTests_4(TestCase):
  def setUp(self):
    self.post = Post_4.objects.create(
        user = 'test_user',
        content = 'test_content',
        picture = 'test_picture',
        created = timezone.now(),
    )
    self.post.save()
    
  def test_get(self):
    """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
    self.post = Post_4.objects.create()
    response = self.client.get(reverse('post_detail_4',args=[self.post.pk]))
    self.assertEqual(response.status_code, 200)