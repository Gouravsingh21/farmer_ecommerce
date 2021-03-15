from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from  .  import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path("about",views.about,name='about'),
    path("project",views.project,name='project'),
    path("contact",views.contact,name='contact'),
    path('Food/',include('Food.urls')),
    path('farmer/',include('farmer.urls')),
    path('transport/', include('transport.urls')),
 ] 
 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

