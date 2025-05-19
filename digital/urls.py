from django.urls import path
from django.contrib import admin 
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path('seo/', views.seo_view, name='seo'),
    path('digital/', views.digital_view, name='digital'),
    path('data/', views.data_view, name='data'),
    path('web/', views.web_view, name='web'),
    path('app/', views.app_view, name='app'),
    path('product/', views.product_view, name='product'),
    path('blogs/', views.blog_list, name='blog_list'),  # list of blogs (can be same as above)
    path('blogs/<slug:slug>/', views.blog_detail, name='blog_detail'),  # blog detail page
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # path("",views.home, name="home"),
    # path('submit/', views.submit, name='submit'),

    # path('registration-success/', views.registration_success, name='registration_success'),

