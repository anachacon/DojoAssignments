from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^books$', views.books),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^books/add$', views.add),
    url(r'^book_add$', views.book_add),
    url(r'^new_review$', views.review_add),
    url(r'^books/(?P<id>\d+)$', views.book, name="book-view"),
    url(r'^users/(?P<id>\d+)$', views.user),
    url(r'^reviews/delete/(?P<id>\d+)$', views.delete),
]