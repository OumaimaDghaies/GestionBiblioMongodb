from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('abonnes/', views.abonne_list, name='abonne_list'),
    path('abonnes/create/', views.abonne_create, name='abonne_create'),
    path('abonnes/update/<int:id>/', views.abonne_update, name='abonne_update'),
    path('abonnes/delete/<int:id>/', views.abonne_delete, name='abonne_delete'),

    path('documents/', views.document_list, name='document_list'),
    path('documents/create/', views.document_create, name='document_create'),
    path('documents/update/<int:id>/', views.document_update, name='document_update'),
    path('documents/delete/<int:id>/', views.document_delete, name='document_delete'),

    path('emprunts/', views.emprunt_list, name='emprunt_list'),
    path('emprunts/create/', views.emprunt_create, name='emprunt_create'),
    path('emprunts/update/<int:id>/', views.emprunt_update, name='emprunt_update'),
    path('emprunts/delete/<int:id>/', views.emprunt_delete, name='emprunt_delete'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)