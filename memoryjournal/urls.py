from django.contrib import admin
from django.urls import path
from memoryjournalapi.views import register_user, check_user
from memoryjournalapi.views import ListView, ItemView, InspirationArticleView, CategoryView, ListItemView, UserView
from django.conf.urls import include
from rest_framework import routers


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'lists', ListView, 'list')
router.register(r'items', ItemView, 'item')
router.register(r'listitems', ListItemView, 'listitem')
# router.register(r'categories', CategoryView, 'category')
router.register(r'inspirationarticles', InspirationArticleView, 'inspirationarticle')
router.register(r'users', UserView, 'user')

urlpatterns = [
    path('register', register_user),
    path('checkuser', check_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
