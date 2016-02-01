from django.conf.urls import url

from . import views

app_name = 'api'

urlpatterns = [
	#url(r'^$',views.index,name='index'),
	url(r'^$',views.index,name='index'),
	url(r'^add_news/$',views.add_news,name='add_news'),
	
 ]