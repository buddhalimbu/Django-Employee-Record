from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexpage,name='homepage'),
    path('signin',views.signin,name='signin'),
    path('load_form', views.load_form,name='loadform'),
    path('add', views.add,name='adduser'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('search/', views.search,name='search'),
    path('login',views.login,name='login'),
    path('signout',views.signout,name='signout'),
    path('about',views.about,name='about'),
    path('show-employee',views.show,name='show-employee'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)