from django.contrib import admin
from django.urls import path

from webapp.views import PhotoListView, PhotoCreateView, PhotoView, PhotoUpdateView, PhotoDeleteView, login_view, \
    logout_view

app_name = 'webapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PhotoListView.as_view(), name='index'),
    path('photo/<int:pk>/', PhotoView.as_view(), name='photo_view'),
    path('add/photo/', PhotoCreateView.as_view(), name='photo_add'),
    path('photo/<int:pk>/update/', PhotoUpdateView.as_view(), name='photo_update'),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('login/',login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout')
]