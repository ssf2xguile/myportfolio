from django.urls import path
from .views import IndexView, DetailPageView, AboutView, WorksView, ContactView, ContactResultView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('detail/<int:pk>/', DetailPageView.as_view(), name='detail'),
    path('about/', AboutView.as_view(), name='about'),
    path('works/', WorksView.as_view(), name='works'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact/result/', ContactResultView.as_view(), name='contact_result')
]