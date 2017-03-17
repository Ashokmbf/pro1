from django.conf.urls import url
from . import views
#from django.core.urlresolvers import reverse


urlpatterns = [
   
    url(r'^$',views.home,name='home'),
    
    #url(r'^create/$',views.create,name='create'),^address_edit/(\d+)/$
     url(r'^edit/(\d+)/$',views.edit,name='edit'),
     url(r'^delete/(\d+)/$',views.delete,name='delete'),
     #url(r'^update/$',views.update,name='update'),
]