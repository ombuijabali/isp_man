import os
from django.core.management.base import BaseCommand
from main.models import Photo
import cloudinary.uploader

class Command(BaseCommand):
    help = 'Upload images to Cloudinary and populate the Photo model'

    def handle(self, *args, **options):
        # Replace 'static/images' with the actual path to your folder containing images
        images_folder = 'static/centers'

        # Iterate over files in the folder
        for filename in os.listdir(images_folder):
            if filename.endswith(('.jpg', '.jpeg', '.png', 'JPG')):
                image_path = os.path.join(images_folder, filename)

                # Upload the image to Cloudinary
                result = cloudinary.uploader.upload(image_path)

                # Check if a Photo with the same photo_name already exists
                existing_photo = Photo.objects.filter(photo_name=filename).first()

                if existing_photo:
                    # Update the existing Photo with the new image URL
                    existing_photo.image = result['secure_url']
                    existing_photo.save()
                else:
                    # Create a new Photo instance with the image URL
                    photo = Photo.objects.create(photo_name=filename, image=result['secure_url'])
                    self.stdout.write(self.style.SUCCESS(f"Image URL for {filename}: {result['secure_url']}"))
