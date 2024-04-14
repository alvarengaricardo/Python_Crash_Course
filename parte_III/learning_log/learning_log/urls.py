from django.urls import include, path

from django.contrib import admin

app_name = 'learning_logs'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('learning_logs.urls', 'learning_logs'), namespace='learning_logs')),
]

