from django.urls import path
from mhsb import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('mhsb/weapon/', views.WeaponView.as_view(), name='weapon'),
    path('mhsb/sousyoku/', views.SousyokuView.as_view(), name='sousyoku'),
    path('mhsb/kyouka/', views.KyoukaView.as_view(), name='kyouka'),
    path('mhsb/form_1/', views.FormCreate_1, name='form_1'),
    path('mhsb/form_2/', views.FormCreate_2, name='form_2'),
    path('mhsb/form_3/', views.FormCreate_3, name='form_3'),
    path('mhsb/form_4/', views.FormCreate_4, name='form_4'),
    path('mhsb/post_detail_1/<int:pk>/', views.PostDetailView_1.as_view(), name='post_detail_1'),
    path('mhsb/post_detail_2/<int:pk>/', views.PostDetailView_2.as_view(), name='post_detail_2'),
    path('mhsb/post_detail_3/<int:pk>/', views.PostDetailView_3.as_view(), name='post_detail_3'),
    path('mhsb/post_detail_4/<int:pk>/', views.PostDetailView_4.as_view(), name='post_detail_4'),
    path('mhsb/comment_1/<int:post_pk>/', views.CommentCreate_1, name='commentcreate_1'),
    path('mhsb/comment_2/<int:post_pk>/', views.CommentCreate_2, name='commentcreate_2'),
    path('mhsb/comment_3/<int:post_pk>/', views.CommentCreate_3, name='commentcreate_3'),
    path('mhsb/comment_4/<int:post_pk>/', views.CommentCreate_4, name='commentcreate_4'),
    path('mhsb/formlist_1/', views.FormListView_1, name='formlist_1'),
    path('mhsb/formlist_2/', views.FormListView_2, name='formlist_2'),
    path('mhsb/formlist_3/', views.FormListView_3, name='formlist_3'),
    path('mhsb/formlist_4/', views.FormListView_4, name='formlist_4'),
]