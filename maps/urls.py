from django.conf.urls import url
from . import views
from maps.views import MapView, TestMapView, user_location


urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^form/$',
    #     EditUserLocationView.as_view(),
    #     name='form'),
    # url(r'^location/$',
    #     user_location,
    #     name='user_location'),
    url(
        # r'^map/(?P<pk>[0-9]+)$',
        r'^map/$',
        MapView.as_view(),
        name='map'
    ),
    url(
        r'^test/$',
        TestMapView.as_view(),
        name='test'
    ),

]
