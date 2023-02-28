from django.contrib import admin
from django.urls import path
from memoryjournalapi.views import register_user, check_user
from django.conf.urls import include
from rest_framework import routers
from memoryjournalapi.views import ListView, ItemView, InspirationArticleView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'lists', ListView, 'lists')
router.register(r'items', ItemView, 'items')
router.register(r'inspirationarticles', InspirationArticleView, 'inspirationarticles')

urlpatterns = [
    path('register', register_user),
    path('checkuser', check_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
