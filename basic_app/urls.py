from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from basic_app import views

app_name = 'basic_app'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^register/', views.register, name='register'),
	url(r'^user_login/$', views.user_login, name='user_login'),
]