
from django.urls import path,include
from . import views
from django.urls import path,include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name="index"),
    path('movie/<int:id>',views.moviedetails,name='moviedetails'),
    path('category/<str:category>',views.category,name='category'),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('login/',views.userlogin,name="login"),
    path('logout/',views.userlogout,name="logout"),
    path('administration/',views.administration,name="dashboard"),
    path('administration/addmovie/',views.Addmovie,name="addmovie"),
    path('administration/category/',views.category_admin,name="category-admin"),
    path('administration/editmovie/<int:id>',views.Editmovie,name="movieupdate"),
    path('administration/deletemovie/<int:id>',views.Deletemovie,name="moviedelete"),
    path('administration/siteinfo/',views.siteInfo,name="siteinfo"),
    path('administration/editinfo/',views.updateInfo,name="editinfo"),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)