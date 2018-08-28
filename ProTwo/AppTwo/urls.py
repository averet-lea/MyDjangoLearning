from django.conf.urls import url
from AppTwo import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^help/',views.help,name='help'),
    url(r'^users/',views.users,name='users'),
    url(r'^form/',views.form_name_view,name='form_name'),
]
