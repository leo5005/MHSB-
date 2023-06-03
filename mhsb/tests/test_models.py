from django.test import TestCase
from mhsb.models import Post_1,Post_2,Post_3,Post_4,Comment_1,Comment_2,Comment_3,Comment_4

class FormTest_1(TestCase):
    def test_form_object(self):
        """投稿内容を一件保存"""
        post = Post_1(
            user = 'test_user',
            content = 'test_content',
            picture = 'test_picture',
        )
        post.save()
        saved_posts = Post_1.objects.all()

        self.assertEqual(saved_posts.count(),1)
        
    def test_saving_and_retrieving_post(self):
        """内容を指定してデータを保存し、すぐに取り出した時に保存した時と同じ値が返されることをテスト"""
        post = Post_1()
        user= 'test_user_to_retrieve'
        content = 'test_content_to_retrieve'
        picture = 'test_picture_to_retrieve'
        post.user = user
        post.content = content
        post.picture = picture
        post.save()

        saved_posts = Post_1.objects.all()
        actual_post = saved_posts[0]

        self.assertEqual(actual_post.user, user)
        self.assertEqual(actual_post.content, content)
        self.assertEqual(actual_post.picture, picture)
        
    def test_Comment_object(self):
        """投稿内容を保存しその投稿内容にコメントをする"""
        post = Post_1(
            user = 'test_user',
            content = 'test_content',
            picture = 'test_picture',
        )
        post.save()
        
        comment = Comment_1(
            user = 'test_user',
            message = 'test_message',
            target = post,
        )
        
        comment.save()
        saved_comments = Comment_1.objects.all()
        
        self.assertEqual(saved_comments.count(),1)
            
        
class FormTest_2(TestCase):
       
    def test_form_object(self):
        """投稿内容を一件保存"""
        post = Post_2(
            user = 'test_user',
            content = 'test_content',
            picture = 'test_picture',
        )
        post.save()
        saved_posts = Post_2.objects.all()

        self.assertEqual(saved_posts.count(),1)
        
    def test_saving_and_retrieving_post(self):
        """内容を指定してデータを保存し、すぐに取り出した時に保存した時と同じ値が返されることをテスト"""
        post = Post_2()
        user= 'test_user_to_retrieve'
        content = 'test_content_to_retrieve'
        picture = 'test_picture_to_retrieve'
        post.user = user
        post.content = content
        post.picture = picture
        post.save()

        saved_posts = Post_2.objects.all()
        actual_post = saved_posts[0]

        self.assertEqual(actual_post.user, user)
        self.assertEqual(actual_post.content, content)
        self.assertEqual(actual_post.picture, picture)
        
    def test_Comment_object(self):
        """投稿内容を保存しその投稿内容にコメントをする"""
        post = Post_2(
            user = 'test_user',
            content = 'test_content',
            picture = 'test_picture',
        )
        post.save()
        
        comment = Comment_2(
            user = 'test_user',
            message = 'test_message',
            target = post,
        )
        
        comment.save()
        saved_comments = Comment_2.objects.all()
        
        self.assertEqual(saved_comments.count(),1)
        
class FormTest_3(TestCase):
       
    def test_form_object(self):
        """投稿内容を一件保存"""
        post = Post_3(
            user = 'test_user',
            content = 'test_content',
            picture = 'test_picture',
        )
        post.save()
        saved_posts = Post_3.objects.all()

        self.assertEqual(saved_posts.count(),1)
        
    def test_saving_and_retrieving_post(self):
        """内容を指定してデータを保存し、すぐに取り出した時に保存した時と同じ値が返されることをテスト"""
        post = Post_3()
        user= 'test_user_to_retrieve'
        content = 'test_content_to_retrieve'
        picture = 'test_picture_to_retrieve'
        post.user = user
        post.content = content
        post.picture = picture
        post.save()

        saved_posts = Post_3.objects.all()
        actual_post = saved_posts[0]

        self.assertEqual(actual_post.user, user)
        self.assertEqual(actual_post.content, content)
        self.assertEqual(actual_post.picture, picture)
        
    def test_Comment_object(self):
        """投稿内容を保存しその投稿内容にコメントをする"""
        post = Post_3(
            user = 'test_user',
            content = 'test_content',
            picture = 'test_picture',
        )
        post.save()
        
        comment = Comment_3(
            user = 'test_user',
            message = 'test_message',
            target = post,
        )
        
        comment.save()
        saved_comments = Comment_3.objects.all()
        
        self.assertEqual(saved_comments.count(),1)    
        
class FormTest_4(TestCase):
       
    def test_form_object(self):
        """投稿内容を一件保存"""
        post = Post_4(
            user = 'test_user',
            content = 'test_content',
            picture = 'test_picture',
        )
        post.save()
        saved_posts = Post_4.objects.all()

        self.assertEqual(saved_posts.count(),1)
        
    def test_saving_and_retrieving_post(self):
        """内容を指定してデータを保存し、すぐに取り出した時に保存した時と同じ値が返されることをテスト"""
        post = Post_4()
        user= 'test_user_to_retrieve'
        content = 'test_content_to_retrieve'
        picture = 'test_picture_to_retrieve'
        post.user = user
        post.content = content
        post.picture = picture
        post.save()

        saved_posts = Post_4.objects.all()
        actual_post = saved_posts[0]

        self.assertEqual(actual_post.user, user)
        self.assertEqual(actual_post.content, content)
        self.assertEqual(actual_post.picture, picture)
        
    def test_Comment_object(self):
        """投稿内容を保存しその投稿内容にコメントをする"""
        post = Post_4(
            user = 'test_user',
            content = 'test_content',
            picture = 'test_picture',
        )
        post.save()
        
        comment = Comment_4(
            user = 'test_user',
            message = 'test_message',
            target = post,
        )
        
        comment.save()
        saved_comments = Comment_4.objects.all()
        
        self.assertEqual(saved_comments.count(),1)
        