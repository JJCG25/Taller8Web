from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('tiposd/',views.tiposd,name='tiposd'),
    path('nuevo/', views.create_tiposd, name='crear_tipodocumento'),
    path('editar/<int:pk>/', views.edit_tiposd, name='editar_tipodocumento'),
    path('eliminar/<int:pk>/', views.delete_tiposd, name='delete_tipodocumento'),
    path('registro/',views.registro,name='registro_persona'),
    path('ciudades/', views.ciudades, name='ciudades'),
    path('ciudades/nueva/', views.create_ciudad, name='create_ciudad'),
    path('ciudades/editar/<int:pk>/', views.edit_ciudad, name='edit_ciudad'),
    path('ciudades/eliminar/<int:pk>/', views.delete_ciudad, name='delete_ciudad'),
    path('', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(template_name='persona/logout.html'), name='logout'),
]