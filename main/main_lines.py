import os
from django.contrib.gis.utils import LayerMapping
from .models import Mains

# Assuming the shapefile is in the 'data' folder within the 'isp' app
mains_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'main.shp'))

mains_mapping = {
    'id': 'id',
    'main_name': 'main_name',
    'types': 'types',
    'length': 'length',
    'comment': 'comment',
    'geom': 'MULTILINESTRING',
}

def run(verbose=True):
    lm = LayerMapping(Mains, mains_shp, mains_mapping, transform=False, encoding='utf-8')
    lm.save(strict=True, verbose=verbose)




