import os
from django.contrib.gis.utils import LayerMapping
from .models import Routes

# Assuming the shapefile is in the 'data' folder within the 'isp' app
route_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'new_connections.shp'))

routes_mapping = {
    'route_name': 'route_name',
    'length': 'length',
    'service_av': 'service_av',
    'installati': 'installati',
    'bandwidth': 'bandwidth',
    'status': 'status',
    'olt': 'OLT',
    'comment': 'comment',
    'infrasturc': 'infrasturc',
    'geom': 'MULTILINESTRING',
}

def run(verbose=True):
    lm = LayerMapping(Routes, route_shp, routes_mapping, transform=False, encoding='utf-8')
    lm.save(strict=True, verbose=verbose)




