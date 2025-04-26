from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'product', views.ProductViewSet)

urlpatterns = [
    path(
        'products/',
        views.ProductListCreate.as_view(),
        name='product_list_and_create',
    ),
    path(
        'products/<int:pk>/',
        views.ProductRetrieveUpdateDestroy.as_view(),
        name="product_delete_and_update"
    ),
    path('', include(router.urls)),
]
