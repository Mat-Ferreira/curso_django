from django.urls import path
from recipes import views as v


urlpatterns = [
    path('', v.home),
    path('about/', v.about),
    path('contact/', v.contact)
]
