from django.conf.urls import url

from ratelimitbackend import admin
from ratelimitbackend.views import login

from .forms import CustomAuthForm


urlpatterns = [
    url(r'^login/$', login,
        {'template_name': 'admin/login.html'}, name='login'),
    url(r'^custom_login/$', login,
        {'template_name': 'custom_login.html',
         'authentication_form': CustomAuthForm},
        name='custom_login'),
    url(r'^admin/', admin.site.urls),
]
