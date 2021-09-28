from django.contrib import admin
from django.urls import path, include

#change admin panel details
admin.site.site_header = "BlogSpot Admin"
admin.site.site_title = "BlogSpot Admin Panel"
admin.site.index_title = "Welcome to BlogSpot Admin Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
]
