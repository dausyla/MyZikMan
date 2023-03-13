from django.contrib import admin
from django.urls import path
from user import views

urlpatterns = [
    path('register', views.register),
    path('login', views.loginUser),
    path('logout', views.logoutUser),

    path('requests', views.requests),

    path('createRequest', views.createRequest),
    path('editRequest/<int:requestId>', views.editRequest),
    path('deleteRequest/<int:requestId>', views.deleteRequest),

    path('seeRequest/<int:requestId>', views.seeRequest)
]
