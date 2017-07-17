from django.conf.urls import url

from .views import product_details

urlpatterns = [

    # ?p<id> means capture the digits in the url and pass them to product_details view in the 'id' argument
    url(r'^(?P<id>\d+)', product_details, name='product'),

]
