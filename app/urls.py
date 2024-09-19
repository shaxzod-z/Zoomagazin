from django.urls import path
from app.views import IndexView, PostDetailView, AboutView, ServicesView, ProductView, PriceView, TeamView, TestView, \
    PostView, ContactView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('blog/', PostView.as_view(), name='blog'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('detail/<int:pk>', PostDetailView.as_view(), name='detail'),
    path('price/', PriceView.as_view(), name='price'),
    path('product/', ProductView.as_view(), name='product'),
    path('service/', ServicesView.as_view(), name='service'),
    path('team/', TeamView.as_view(), name='team'),
    path('testimonial/', TestView.as_view(), name='testimonial'),
]
