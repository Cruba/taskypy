from django.conf.urls import url
from .views import home, post_list

urlpatterns =[
    url(r'home$',home),
        url(r'blog$',post_list)

]