from django.urls import path
from .views import CareerView, CareerRetrieveUpdateDeleteView


urlpatterns = [
    path('careers/', CareerView.as_view({'get': 'list', 'post': 'create'}), name='get-post-careers'),
    path('careers/<int:pk>/', CareerRetrieveUpdateDeleteView.as_view(), name='retrieve-put-delete-careers'),
]
