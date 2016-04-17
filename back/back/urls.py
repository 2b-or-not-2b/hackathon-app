"""back URL Configuration

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
from django.conf.urls import include, url
from cashtag.views import profile_view, feed_view, cashtag_view
from users.views import user_view
# from django.contrib import admin
from visa_api.views import test_push_pull_view

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^api/profile/?', profile_view),
    url(r'^api/feed/?', feed_view),
    url(r'^api/cashtag/?', cashtag_view),
    url(r'^api/user/?', user_view),
    url(r'^api/test_visa/?', test_push_pull_view),
    url(r'^api/pay/?', test_push_pull_view),
]
