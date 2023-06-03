from django.test import TestCase
from django.urls import reverse, resolve
from ..views import *
from django.urls import path

class TestUrls(TestCase):

  """index ページへのURLでアクセスする時のリダイレクトをテスト"""
  def test_post_home_url(self):
    view = resolve("/")
    self.assertEqual(view.func.view_class, HomeView)

  def test_post_weapon_url(self):
    view = resolve("/mhsb/weapon/")
    self.assertEqual(view.func.view_class, WeaponView)
    
  def test_post_sousyoku_url(self):
    view = resolve("/mhsb/sousyoku/")
    self.assertEqual(view.func.view_class, SousyokuView)
    
  def test_post_kyouka_url(self):
    view = resolve("/mhsb/kyouka/")
    self.assertEqual(view.func.view_class, KyoukaView)
    
  def test_post_formlist_1_url(self):
    view = resolve("/mhsb/formlist_1/")
    self.assertEqual(view.view_name,"formlist_1")
  
  def test_post_formlist_2_url(self):
    view = resolve("/mhsb/formlist_2/")
    self.assertEqual(view.view_name,"formlist_2")
    
  def test_post_formlist_3_url(self):
    view = resolve("/mhsb/formlist_3/")
    self.assertEqual(view.view_name,"formlist_3")
    
  def test_post_formlist_4_url(self):
    view = resolve("/mhsb/formlist_4/")
    self.assertEqual(view.view_name,"formlist_4")