import os
from django.contrib.gis.utils import LayerMapping
from .models import Splitters

# Assuming the shapefile is in the 'data' folder within the 'isp' app
splitters_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'spliters.shp'))

splitters_mapping = {
    'spliter_na': 'spliter_na',
    'spliter_ty': 'spliter_ty',
    'no_of_port': 'no_of_port',
    'installati': 'installati',
    'condition': 'condition',
    'latitude': 'latitude',
    'longitude': 'longitude',
    'photo_url': 'photo_url',
    'geom': 'MULTIPOINT',
}

def run(verbose=True):
    lm = LayerMapping(Splitters, splitters_shp, splitters_mapping, transform=False, encoding='utf-8')
    lm.save(strict=True, verbose=verbose)




