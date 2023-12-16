import os
from django.contrib.gis.utils import LayerMapping
from .models import Fats

# Assuming the shapefile is in the 'data' folder within the 'isp' app
fats_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'fat.shp'))

fats_mapping = {
    'fat_name': 'fat_name',
    'installati': 'installati',
    'condition': 'condition',
    'latitude': 'latitude',
    'longitude': 'longitude',
    'photo_name': 'photo_name',
    'photo_url': 'photo_url',
    'geom': 'MULTIPOINT',
}

def run(verbose=True):
    lm = LayerMapping(Fats, fats_shp, fats_mapping, transform=False, encoding='utf-8')
    lm.save(strict=True, verbose=verbose)




