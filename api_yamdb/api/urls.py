from django.urls import include, path

app_name = 'api'


urlpatterns = [
    path('', include('api.v1.urls'))
]
