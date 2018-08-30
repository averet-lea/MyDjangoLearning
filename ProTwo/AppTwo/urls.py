from django.conf.urls import url
from AppTwo import views

app_name = 'AppTwo'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^help/',views.help,name='help'),
    url(r'^users/',views.users,name='users'),
    url(r'^form/',views.form_name_view,name='form_name'),

    url(r'^base/',views.base,name='base'),
    url(r'^other/',views.other,name='other'),
    url(r'^url_templates/',views.url_templates,name='url_templates'),
]
