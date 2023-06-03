from django.shortcuts import render
from django.views.generic import View
from .models import Post

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mhsb/index.html')
    
class WeaponView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mhsb/weapon.html')
    
class KyoukaView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mhsb/kyouka.html') 
    
    
    
    
    
    
#form_1
                       
class PostFormView_1(ListView,FormMixin):
    model = Post_1
    form_class = PostForm_1
    template_name = 'mhsb/form_1.html'
    success_url = 'mhsb/form_1/'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post_1.objects.order_by('-created')
        context['form'] = PostForm_1()
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            # <process form cleaned data>
            post = form.cleaned_data
            obj = Post_1(**post)
            obj.save()
            return HttpResponseRedirect('/mhsb/form_1/')

        return render(request, 'mhsb/form_1.html', {'form': form})
    
    
    
    
class PostDetailView_1(DetailView):
    model = Post_1
    form_class = CommentForm_1
    template_name = 'mhsb/post_detail_1.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post_1, pk=self.kwargs['pk'])
        context['comment'] = Comment_1.objects.order_by('-created_at')
        context['comment_form'] = CommentForm_1
        return context
    
    
def CommentCreate_1(request,post_pk):
    post = get_object_or_404(Post_1, pk=post_pk)
    form = CommentForm_1(request.POST or None)
    
    if request.method == 'POST':
        comment = form.save(commit=False)
        comment.target = post
        comment.save()
        return redirect('post_detail_1', pk=post.pk)
    
    return render(request,'mhsb/post_detail_1')
 
 
 
      
      
#form_2

class PostFormView_2(ListView,FormMixin):
    model = Post_2
    form_class = PostForm_2
    template_name = 'mhsb/form_2.html'
    success_url = 'mhsb/form_2/'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post_2.objects.order_by('-id')
        context['form'] = PostForm_2()
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            # <process form cleaned data>
            post_data = form.cleaned_data
            obj = Post_2(**post_data)
            obj.save()
            return HttpResponseRedirect('/mhsb/form_2/')

        return render(request, 'mhsb/form_2.html', {'form': form})
    
class PostDetailView_2(View):
    def get(self, request, *args, **kwargs):
        post_data = Post_2.objects.get(id=self.kwargs['pk'])
        return render(request, "mhsb/post_detail_2.html", {
            "post_data": post_data
        })

#コメント投稿ページのビュー
class CommentView_2(CreateView):
    template_name = 'mhsb/comment_form_2.html'
    model = Comment_2
    form_class = CommentForm_2

#フォームに入力された情報が正しい場合の処理
    def form_valid(self, form):
        post_pk = self.kwargs['pk']
        post_data = get_object_or_404(CommentForm_2, pk=post_pk)
        comment = form.save(commit=False)
        comment.target = post_data
        comment.save()
        return redirect('mhsb:post_detail_2', pk=post_pk)

#htmlテンプレートに渡すデータを定義
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_data'] = get_object_or_404(CommentForm_2, pk=self.kwargs['pk'])
        return context    
    
    
    
    
    
    
    
        
#form_3

class PostFormView_3(ListView,FormMixin):
    model = Post_3
    form_class = PostForm_3
    template_name = 'mhsb/form_3.html'
    success_url = 'mhsb/form_3/'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['post_data'] = Post_3.objects.order_by('-id')
        context['form'] = PostForm_3()
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            # <process form cleaned data>
            post_data = form.cleaned_data
            obj = Post_3(**post_data)
            obj.save()
            return HttpResponseRedirect('/mhsb/form_3/')

        return render(request, 'mhsb/form_3.html', {'form': form})
    
class PostDetailView_3(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mhsb/rensei.html')
    
class WeaponView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mhsb/weapon.html')
        