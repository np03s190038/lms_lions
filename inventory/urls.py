from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('home',views.home, name="home"),
    path('addbook', views.addbook, name="addbook"),
    path('updateBooks/<str:pk>', views.updateBooks, name="updateBooks"),
    path('deleteBook/<str:pk>', views.deleteBook, name="deleteBook"),
    path('searchBook', views.searchBook, name="searchBook"),
    path('issuebook',views.issuebook, name="issuebook"),
    path('download',views.download, name="download"),
    path('dashboard',views.dashboard, name="dashboard"),
    path('download-csv', views.bookDownload, name="bookDownload")
    

]