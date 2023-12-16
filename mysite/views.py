from django.shortcuts import render
from blog.models import Post,Category
from django.http import HttpResponse,JsonResponse
from mysite.models import content
from mysite.forms import NameForm,cantactForm,newsletterForm
from django.http import HttpResponseRedirect 
from django.contrib import messages
def index_view(request):
    # show the last 6 posts in home page 
    posts = Post.objects.all().prefetch_related('category').order_by('-published_date')[:6]
    context = {'posts': posts}
    return render(request,'website/index.html',context)

def contact_view(request):
    
    if request.method == 'POST':
        form = cantactForm(request.POST)
        if form.is_valid():
            form.instance.name = 'unknown'
            form.save()
            messages.add_message(request,messages.SUCCESS,'your ticket submited successfully')
        else:
            messages.add_message(request,messages.ERROR,'your ticket didnt submit') 
    form = cantactForm()
    return render(request,'website/contact.html',{'form':form})

def about_view(request):
    return render(request,'website/about.html')

def elements_view(request):
    return render(request,'website/elements.html')

def newsletter_view(request):
    if request.method == 'POST':
        form = newsletterForm(request.POST)
        if form.is_valid(): 
            form.save()
            messages.add_message(request,messages.SUCCESS,'your ticket submited successfully')
        else:
            messages.add_message(request,messages.ERROR,'your ticket didnt submit')
    form = newsletterForm()
    return render(request,'website/test.html',{'form':form})
def test(request):
    if request.method == 'POST':
        form = cantactForm(request.POST)
        if form.is_valid(): 
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('not valid')
    form = cantactForm()
    return render(request,'website/test.html',{'form':form})