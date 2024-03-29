"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
# from graphene_django.views import GraphQLView
from graphene_file_upload.django import FileUploadGraphQLView
from graphql.backend.core import GraphQLCoreBackend

router = routers.DefaultRouter()


class GraphQLCustomCoreBackend(GraphQLCoreBackend):
    def __init__(self, executor=None):
        # type: (Optional[Any]) -> None
        super().__init__(executor)
        self.execute_params['allow_subscriptions'] = True


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    # path("api/graphql/", GraphQLView.as_view(graphiql=True)),
    path("api/graphql/", FileUploadGraphQLView.as_view(graphiql=True,
         backend=GraphQLCustomCoreBackend())),
]
