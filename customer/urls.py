# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views



router = routers.DefaultRouter()
router.register(r'customers', views.CustomerViewSet, basename='customer')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('customers/', views.customer_list),
    #path('customers/<int:pk>', views.customer_detail),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
#urlpatterns = format_suffix_patterns(urlpatterns)
