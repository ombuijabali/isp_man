import os
from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.geos import GEOSGeometry
from .models import Clients

# Assuming the shapefile is in the 'data' folder within the 'isp' app
client_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'buildings.shp'))

clients_mapping = {
    'pon_type': 'pon_type',
    'client_nam': 'client_nam',
    'olt': 'olt',
    'zone': 'zone',
    'address': 'address',
    'building_t': 'building_t',
    'latitude': 'latitude',
    'longitude': 'longitude',
    'odb_split': 'odb_split',
    'geom': 'MULTIPOINT',
}

def run(verbose=True):
    lm = LayerMapping(Clients, client_shp, clients_mapping, transform=False, encoding='utf-8', unique=['address', 'name'])
    lm.save(strict=True, verbose=verbose)

