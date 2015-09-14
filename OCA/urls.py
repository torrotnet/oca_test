"""OCA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'oca_test.views.home', name='home'),
    # url(r'^user_data/$', 'oca_test.views.user_data', name='user_data'),
    url(r'^test/$', 'oca_test.views.test', name='test'),
    url(r'^results/$', 'oca_test.views.results', name='results'),
    url(r'^results/(?P<id>[0-9])/$', 'oca_test.views.result', name='result'),
    url(r'^instructions/$', 'oca_test.views.instructions', name='instructions'),
    url(r'^logout/$', 'oca_test.views.log_out', name='log_out'),
    url(r'^login/$', 'oca_test.views.log_in', name='log_in'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
