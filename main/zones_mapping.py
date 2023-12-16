import os
from django.contrib.gis.utils import LayerMapping
from .models import Zone

# Assuming the shapefile is in the 'data' folder within the 'isp' app
zones_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'zones.shp'))

zones_mapping = {
    'input_fid': 'Input_FID',
    'id_1': 'id_1',
    'spliter_id': 'spliter_id',
    'spliter_na': 'spliter_na',
    'spliter_ty': 'spliter_ty',
    'no_of_port': 'no_of_port',
    'installati': 'installati',
    'condition': 'condition',
    'geom': 'MULTIPOLYGON',
}

def run(verbose=True):
    lm = LayerMapping(Zone, zones_shp, zones_mapping, transform=False, encoding='utf-8')

    # Print features before saving
    features_before = Zone.objects.all().count()
    print(f"Features before saving: {features_before}")

    # Save the features
    lm.save(strict=True, verbose=verbose)

    # Print features after saving
    features_after = Zone.objects.all().count()
    print(f"Features after saving: {features_after}")

    # Check if all features were saved
    if features_before == features_after:
        print("No new features were saved. Check your mapping and data.")
    else:
        print("Saving successful.")

# Run the script
run()
