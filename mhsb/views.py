from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View,DetailView
from django.urls import reverse_lazy, reverse
from .models import Post_1,Post_2,Post_3,Post_4,Comment_1,Comment_2,Comment_3,Comment_4
from .forms import PostForm_1,PostForm_2,PostForm_3,PostForm_4,CommentForm_1,CommentForm_2,CommentForm_3,CommentForm_4
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mhsb/index.html')
    
class WeaponView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mhsb/weapon.html')
    
class SousyokuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mhsb/sousyoku.html') 
    
class KyoukaView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mhsb/kyouka.html') 
    
    
    
    
    
    
#formlist_1
                    
def FormListView_1(request):
    """フォーム画面、ページオブジェクト、投稿内容を渡す"""
    post = Post_1.objects.order_by('-created')
    page_obj = paginate_queryset(request, post, 20)
    form = PostForm_1
    context = {
        'form': form,
        'page_obj': page_obj,
        'post_list' : page_obj.object_list,
    }

    return render(request, 'mhsb/formlist_1.html', context)
    
def paginate_queryset(request, queryset, count):
    """ページネーションをするためのメソッド"""
    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj

def FormCreate_1(request):
    """フォーム投稿時の処理"""
    form = PostForm_1(request.POST,request.FILES)
    ctx = {"form": form}
    if request.POST:
        if form.is_valid():
            post_list = form.cleaned_data
            obj = Post_1(**post_list)
            obj.save()
            messages.success(request, '投稿しました')
            return redirect("formlist_1")
        
        else:    
            messages.error(request, '投稿できませんでした')
            return render(request, 'mhsb/formlist_1.html', ctx)
 
    
    
    
    
    
#post_detail_1    
    
class PostDetailView_1(DetailView):
    model = Post_1
    form_class = CommentForm_1
    template_name = 'mhsb/post_detail_1.html'
    
    def get_context_data(self, **kwargs):
        """投稿詳細、コメント、フォーム画面を渡す"""
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post_1, pk=self.kwargs['pk'])
        context['comment'] = Comment_1.objects.order_by('-created_at')
        context['comment_form'] = CommentForm_1
        return context
    
def CommentCreate_1(request,post_pk):
    """フォーム投稿時の処理"""
    post = get_object_or_404(Post_1, pk=post_pk)
    form = CommentForm_1(request.POST or None)
    
    if request.method == 'POST':
        comment = form.save(commit=False)
        comment.target = post
        comment.save()
        messages.success(request, 'コメントしました')
        return redirect('post_detail_1', pk=post.pk)

    return render(request,'mhsb/post_detail_1')
 
 
 
 
 
      
      
#formlist_2
    
def FormListView_2(request):
    """フォーム画面、ページオブジェクト、投稿内容を渡す"""
    post = Post_2.objects.order_by('-created')
    page_obj = paginate_queryset(request, post, 20)
    form = PostForm_2
    context = {
        'form': form,
        'page_obj': page_obj,
        'post_list' : page_obj.object_list,
    }

    return render(request, 'mhsb/formlist_2.html', context) 
    
def paginate_queryset(request, queryset, count):
    """ページネーションをするためのメソッド"""
    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj

def FormCreate_2(request):
    """フォーム投稿時の処理"""
    form = PostForm_2(request.POST,request.FILES)
    ctx = {"form": form}
    if request.POST:
        if form.is_valid():
            post_list = form.cleaned_data
            obj = Post_2(**post_list)
            obj.save()
            messages.success(request, '投稿しました')
            return redirect("formlist_2")
        
        else:
            messages.error(request, '投稿できませんでした')    
            return render(request, 'mhsb/formlist_2.html', ctx)
 
    
    
    
    
#post_detail_2    
    
class PostDetailView_2(DetailView):
    model = Post_2
    form_class = CommentForm_2
    template_name = 'mhsb/post_detail_2.html'
    
    def get_context_data(self, **kwargs):
        """投稿詳細、コメント、フォーム画面を渡す"""
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post_2, pk=self.kwargs['pk'])
        context['comment'] = Comment_2.objects.order_by('-created_at')
        context['comment_form'] = CommentForm_2
        return context
    
def CommentCreate_2(request,post_pk):
    """フォーム投稿時の処理"""
    post = get_object_or_404(Post_2, pk=post_pk)
    form = CommentForm_2(request.POST or None)
    
    if request.method == 'POST':
        comment = form.save(commit=False)
        comment.target = post
        comment.save()
        messages.success(request, 'コメントしました')
        return redirect('post_detail_2', pk=post.pk)
    
    return render(request,'mhsb/post_detail_2')
      
      
      
      
      
      
      
      
      
#formlist_3

def FormListView_3(request):
    """フォーム画面、ページオブジェクト、投稿内容を渡す"""
    post = Post_3.objects.order_by('-created')
    page_obj = paginate_queryset(request, post, 20)
    form = PostForm_3
    context = {
        'form': form,
        'page_obj': page_obj,
        'post_list' : page_obj.object_list,
    }

    return render(request, 'mhsb/formlist_3.html', context) 
    
    
def paginate_queryset(request, queryset, count):
    """ページネーションをするためのメソッド"""
    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj


def FormCreate_3(request):
    """フォーム投稿時の処理"""
    form = PostForm_3(request.POST,request.FILES)
    ctx = {"form": form}
    if request.POST:
        if form.is_valid():
            post_list = form.cleaned_data
            obj = Post_3(**post_list)
            obj.save()
            messages.success(request, '投稿しました')
            return redirect("formlist_3")
        
        else:
            messages.error(request, '投稿できませんでした')
            return render(request, 'mhsb/formlist_3.html', ctx)
 
    
    
    
    
#post_detail_3    
    
class PostDetailView_3(DetailView):
    model = Post_3
    form_class = CommentForm_3
    template_name = 'mhsb/post_detail_3.html'
    
    def get_context_data(self, **kwargs):
        """投稿詳細、コメント、フォーム画面を渡す"""
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post_3, pk=self.kwargs['pk'])
        context['comment'] = Comment_3.objects.order_by('-created_at')
        context['comment_form'] = CommentForm_3
        return context
    
def CommentCreate_3(request,post_pk):
    """フォーム投稿時の処理"""
    post = get_object_or_404(Post_3, pk=post_pk)
    form = CommentForm_3(request.POST or None)
    
    if request.method == 'POST':
        comment = form.save(commit=False)
        comment.target = post
        comment.save()
        messages.success(request, 'コメントしました')
        return redirect('post_detail_3', pk=post.pk)

    return render(request,'mhsb/post_detail_3')
    
    
    
    
    
    
    
                
#formlist_4        

def FormListView_4(request):
    """フォーム画面、ページオブジェクト、投稿内容を渡す"""
    post = Post_4.objects.order_by('-created')
    page_obj = paginate_queryset(request, post, 20)
    form = PostForm_4
    context = {
        'form': form,
        'page_obj': page_obj,
        'post_list' : page_obj.object_list,
    }

    return render(request, 'mhsb/formlist_4.html', context) 
    
    
def paginate_queryset(request, queryset, count):
    """ページネーションをするためのメソッド"""
    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj


def FormCreate_4(request):
    """フォーム投稿時の処理"""
    form = PostForm_4(request.POST,request.FILES)
    ctx = {"form": form}
    if request.POST:
        if form.is_valid():
            post_list = form.cleaned_data
            obj = Post_4(**post_list)
            obj.save()
            messages.success(request, '投稿しました')
            return redirect("formlist_4")
        else:
            messages.error(request, '投稿できませんでした')
            return render(request, 'mhsb/formlist_4.html', ctx)
 
    
#post_detail_4    
    
class PostDetailView_4(DetailView):
    model = Post_4
    form_class = CommentForm_4
    template_name = 'mhsb/post_detail_4.html'
    
    def get_context_data(self, **kwargs):
        """投稿詳細、コメント、フォーム画面を渡す"""
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post_4, pk=self.kwargs['pk'])
        context['comment'] = Comment_4.objects.order_by('-created_at')
        context['comment_form'] = CommentForm_4
        return context  
    
def CommentCreate_4(request,post_pk):
    """フォーム投稿時の処理"""
    post = get_object_or_404(Post_4, pk=post_pk)
    form = CommentForm_4(request.POST or None)
    
    if request.method == 'POST':
        comment = form.save(commit=False)
        comment.target = post
        comment.save()
        messages.success(request, 'コメントしました')
        return redirect('post_detail_4', pk=post.pk)
    
    return render(request,'mhsb/post_detail_4')