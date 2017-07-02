from django.conf.urls import url 

from . import views

urlpatterns = [
				url(r'^$', views.home_page, name = 'home'),
				url(r'^(?P<todo_id>[0-9]+)/$', views.todo_detail, name = 'detail'),
				url(r'^post/$', views.post_todo, name = 'post'),
				url(r'^delete/(?P<todo_id>[0-9]+)/$', views.delete_todo, name = 'delete'),
				url(r'^edit/(?P<todo_id>[0-9]+)/$', views.edit_todo, name = 'edit'),
				]