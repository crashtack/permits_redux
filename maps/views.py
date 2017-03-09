# from django.shortcuts import render
import os
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.contrib.auth.models import User
from django.contrib.gis.geoip2 import GeoIP2
from maps.models import Permit


def index(request):
    return HttpResponse("Hello, world")


def user_location(request):
    context = {'name': 'fred'}
    context['googleapikey'] = os.environ.get('GOOGLE_MAPS_API_KEY')
    return render(request, 'maps/noisy.html', context)


class MapView(ListView):
    """
    Shows a Map and with plotted points.
    """
    model = User
    template_name = 'maps/map.html'

    def get_point(url):
        point = GeoIP2()
        return point.lat_lon(url)

    def get_context_data(self, **kwargs):
        context = super(MapView, self).get_context_data(**kwargs)
        context['googleapikey'] = os.environ.get('GOOGLE_MAPS_API_KEY')

        points = []
        for pp in Permit.objects.all():
            points.append({
                'lat': pp.latitude,
                'lng': pp.longitude,
                'num': pp.permit_number,
                'description': pp.description,
            })

        context['data'] = points
        # import pdb; pdb.set_trace()
        return context


class TestMapView(ListView):
    """
    Shows a Map and with plotted points.
    """
    model = User
    template_name = 'maps/map.html'

    def get_point(url):
        point = GeoIP2()
        return point.lat_lon(url)

    def get_context_data(self, **kwargs):
        context = super(TestMapView, self).get_context_data(**kwargs)
        context['googleapikey'] = os.environ.get('GOOGLE_MAPS_API_KEY')
        point = MapView.get_point(
            # 'ec2-35-160-27-154.us-west-2.compute.amazonaws.com'
            'www.uw.edu'
        )
        context['data'] = [{'lat': point[0], 'lng': point[1]}, ]
        # import pdb; pdb.set_trace()
        return context
