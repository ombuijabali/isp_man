import os
from django.contrib.gis.utils import LayerMapping
from .models import Center

# Assuming the shapefile is in the 'data' folder within the 'isp' app
center_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'centers.shp'))

centers_mapping = {
    'main_route': 'main_route',
    'code': 'code',
    'descriptio': 'descriptio',
    'status': 'status',
    'photo_url': 'photo_url',
    'geom': 'MULTIPOLYGON',
}

def run(verbose=True):
    lm = LayerMapping(Center, center_shp, centers_mapping, transform=False, encoding='utf-8')
    lm.save(strict=True, verbose=verbose)




