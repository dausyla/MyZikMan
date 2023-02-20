from django.contrib import admin
from django.urls import path
from user import views

urlpatterns = [
    path('createUser', views.createUser),
    path('createBand', views.createBand),

    path('read', views.read),

    path('editUser/<int:id>', views.editUser),
    path('editBand/<int:id>', views.editBand),

    path('updateUser/<int:id>', views.updateUser),
    path('updateBand/<int:id>', views.updateBand),

    path('deleteUser/<int:id>', views.destroyUser),
    path('deleteBand/<int:id>', views.destroyBand),
]