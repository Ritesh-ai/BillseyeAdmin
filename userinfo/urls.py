from django.conf.urls import url
from . import views as userinfo_views

app_name = 'userinfo'

urlpatterns = [
    url(r'dashboard/',userinfo_views.dashboard,name='dashboard'),
    url(r'default/',userinfo_views.default,name='default'),
    url(r'register/',userinfo_views.register,name='register'),
    url(r'login/',userinfo_views.user_login,name='user_login'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',userinfo_views.activate, name='activate'),
    url(r'verify/',userinfo_views.contact_verify,name='contact_verify'),
    url(r'contact/',userinfo_views.contact,name='contact'),
    url(r'logout/',userinfo_views.user_logout,name='user_logout'),

]
