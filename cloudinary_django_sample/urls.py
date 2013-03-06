from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

import photo_album.views as photo_album

urlpatterns = patterns('',
    url(r'^list$', photo_album.list),
    url(r'^upload$', photo_album.upload),
    url(r'^upload/backend$', photo_album.upload),
    url(r'^upload/complete$', photo_album.upload),
)
