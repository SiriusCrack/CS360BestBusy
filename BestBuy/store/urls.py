from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.ProductListView.as_view(), name='products'),
    path('exact-match', views.exactMatch, name='exactMatch'),
    path('priority-criteria', views.priorityCriteria, name="priorityCrit"),
    path('service-requirements', views.serviceRequirements, name="serviceReq"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)