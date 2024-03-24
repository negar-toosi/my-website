"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from mysite.sitemaps import StaticViewSitemap
from blog.sitemaps import BlogSitemap
from mysite import views
import debug_toolbar
from django.urls import include
from django.contrib.auth import views as auth_views
from django.http import HttpResponse

from django.views.generic import TemplateView
sitemaps = {
    'static': StaticViewSitemap,
    'blog': BlogSitemap,
}


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('mysite.urls')),
    path('blog/',include('blog.urls')),
    path('accounts/',include('accounts.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    path('summernote/', include('django_summernote.urls')),
    path('robots.txt', include('robots.urls')), 
    path('__debug__/', include(debug_toolbar.urls)),
    path('captcha/', include('captcha.urls')),
    path("accounts/", include("django.contrib.auth.urls")),  
]

if settings.MAINTENANCE_MODE:
   urlpatterns.insert(0, re_path(r'^', TemplateView.as_view(template_name='website/maintenance.html'), name='maintenance'))

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path(r'^__debug__/', include(debug_toolbar.urls)),
    ]

handler404 = 'mysite.views.custom_404'