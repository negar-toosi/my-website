from django.shortcuts import render,get_object_or_404,redirect 
from blog.models import Post,Category,Comments
from django.http import HttpResponse,JsonResponse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from blog.forms import commentsForm 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from datetime import datetime
from django.utils import timezone
def blog_view(request,**kwargs):
    
    posts = Post.objects.filter(status = 1) #.order_by('id')
    
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])

    # posts = Paginator(posts,2)
    # page_number = request.GET.get('page')
    # try:
    #     posts = posts.get_page(page_number)
    # except PageNotAnInteger:
    #     posts = posts.get_page(1)
    # except EmptyPage:
    #     posts = posts.get_page(1)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    if request.method == 'POST':
        form = commentsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your ticket submited successfully')
        else:
            messages.add_message(request,messages.ERROR,'your ticket didnt submited successfully')
    
    post = get_object_or_404(Post,id=pid,status=1)
    # increase the view of post when user refreshes the page
    if post:
        post.views = post.views + 1
        post.save()
    if not post.login_require:
        comments = Comments.objects.filter(post=post.id,approved=True).order_by('-created_date')
        form = commentsForm()
        context = {'post': post,'comments':comments,'form':form}
        return render(request,'blog/blog-single.html',context)
    else:
        return HttpResponseRedirect(reverse('accounts:login'))

def blog_search(request):
    posts = Post.objects.filter(status = 1)
    if request.method == 'GET':
        if s := request.GET.get('s'): 
            posts = posts.filter(content__contains=request.GET.get('s'))
    context = {'posts': posts}
    return render(request,'blog/blog-home.html',context)

def test(request):
    posts = Post.objects.all().values('title','image')
    post_list = list(posts)
    return JsonResponse(post_list, safe=False)
    
    