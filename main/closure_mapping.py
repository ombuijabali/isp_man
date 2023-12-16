import os
from django.contrib.gis.utils import LayerMapping
from .models import Closures

# Assuming the shapefile is in the 'data' folder within the 'isp' app
closures_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'closure.shp'))

closures_mapping = {
    'closore_na': 'closore_na',
    'installati': 'installati',
    'condition': 'condition',
    'latitude': 'latitude',
    'longitude': 'longitude',
    'photo_url': 'photo_url',
    'geom': 'MULTIPOINT',
}

def run(verbose=True):
    lm = LayerMapping(Closures, closures_shp, closures_mapping, transform=False, encoding='utf-8')
    lm.save(strict=True, verbose=verbose)




