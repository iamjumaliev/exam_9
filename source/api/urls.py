from django.urls import include, path

from rest_framework import routers

from api import views
from rest_framework.authtoken.views import obtain_auth_token

from api.views import like_up, like_down

router = routers.DefaultRouter()

router.register(r'comments', views.CommentViewSet)

app_name = 'api'

urlpatterns = [

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('like/add', like_up, name = 'like_add'),
    path('like/del', like_down, name = 'like_del')

]