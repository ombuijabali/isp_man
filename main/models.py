# isp/main/models.py
from django.db import models
import cloudinary.models
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class Notification(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField()
    is_read = models.BooleanField(default=False)
    changes = models.TextField() 

    def save(self, *args, **kwargs):
        # Check if the instance is being created or updated
        is_new = self._state.adding

        # Save the instance
        super().save(*args, **kwargs)

        # Create a new notification
        notification_content = f"Changes made to {self.__class__.__name__} with id {self.id}"
        notification_changes = "Include any specific details about the changes here."

        Notification.objects.create(
            content=notification_content,
            timestamp=timezone.now(),
            changes=notification_changes
        )
        
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "UserProfiles"


class Photo(models.Model):
    photo_name = models.CharField(max_length=255, unique=True)
    image = cloudinary.models.CloudinaryField('image', null=True, blank=True)

    fat = models.OneToOneField('Fats', on_delete=models.CASCADE, null=True, blank=True)
    splitter = models.OneToOneField('Splitters', on_delete=models.CASCADE, null=True, blank=True)
    closure = models.OneToOneField('Closures', on_delete=models.CASCADE, null=True, blank=True)
    center = models.OneToOneField('Center', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.photo_name


class Fats(models.Model):
    fat_name = models.CharField(max_length=254, default='', blank=True)
    installati = models.CharField(max_length=254, default='', blank=True)
    condition = models.CharField(max_length=254, default='', blank=True)
    latitude = models.FloatField(default='', null=True, blank=True)
    longitude = models.FloatField(default='', null=True, blank=True)
    photo_name = models.CharField(max_length=255, default='')
    photo_url = models.CharField(max_length=200, blank=True, null=True)
    geom = models.MultiPointField(srid=4326)

    def __str__(self):
        return self.fat_name

    class Meta:
        verbose_name_plural = "Fats"


class Closures(models.Model):
    closore_na = models.CharField(max_length=254, default='') 
    installati = models.CharField(max_length=254, default='', blank=True)
    condition = models.CharField(max_length=254, default='', blank=True)
    latitude = models.FloatField(default='', blank=True)
    longitude = models.FloatField(default='', blank=True)
    photo_name = models.CharField(max_length=255, default='')
    photo_url = models.CharField(max_length=200, blank=True, null=True)
    geom = models.MultiPointField(srid=4326)

    def __str__(self):
        return self.closore_na

    class Meta:
        verbose_name_plural = "Closures"


class Splitters(models.Model):
    spliter_na = models.CharField(max_length=254, default='', blank=True)
    spliter_ty = models.CharField(max_length=254, default='', blank=True)
    no_of_port = models.CharField(max_length=254, default='', blank=True)
    used_ports = models.IntegerField(default=0, blank=True)
    unused_por = models.IntegerField(default=0, blank=True)
    installati = models.CharField(max_length=254, default='', blank=True)
    condition = models.CharField(max_length=254, default='', blank=True)
    latitude = models.FloatField(default='', blank=True)
    longitude = models.FloatField(default='', blank=True)
    photo_name = models.CharField(max_length=255, default='')
    photo_url = models.CharField(max_length=200, blank=True, null=True)
    geom = models.MultiPointField(srid=4326)

    def __str__(self):
        return self.spliter_na

    class Meta:
        verbose_name_plural = "Splitters"


class Center(models.Model):
    main_route = models.CharField(max_length=100, null=True, default='', blank=True)
    code = models.CharField(max_length=100, null=True)
    descriptio = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, null=True)
    photo_name = models.CharField(max_length=255, default='')
    photo_url = models.CharField(max_length=200, blank=True, null=True)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.main_route

    class Meta:
        verbose_name_plural = "Centers"


class Routes(models.Model):
    route_name = models.CharField(max_length=100, default='', blank=True)
    length = models.FloatField(default=None, null=True, blank=True)
    service_av = models.CharField(max_length=100, default='', blank=True)
    installati = models.DateField(null=True)
    bandwidth = models.FloatField(null=True)
    status = models.CharField(max_length=100, default='', blank=True)
    olt = models.CharField(max_length=100, default='', blank=True)
    comment = models.CharField(max_length=100, default='', blank=True)
    infrasturc = models.CharField(max_length=100, default='', blank=True)
    types = models.CharField(max_length=100, default='', blank=True)
    geom = models.MultiLineStringField(srid=4326)

    def __str__(self):
        return self.route_name

    class Meta:
        verbose_name_plural = "Routes"


class Mains(models.Model):
    id = models.BigIntegerField(primary_key=True)
    main_name = models.CharField(max_length=100, default='', blank=True)
    types = models.CharField(max_length=100, default='', blank=True)
    length = models.FloatField(default=None, null=True, blank=True)
    comment = models.CharField(max_length=100, default='', blank=True)
    geom = models.MultiLineStringField(srid=4326)

    def __str__(self):
        return self.main_name

    class Meta:
        verbose_name_plural = "Mains"

class Zone(models.Model):
    input_fid = models.IntegerField()
    id_1 = models.BigIntegerField()
    spliter_id = models.BigIntegerField()
    spliter_na = models.CharField(max_length=254)
    spliter_ty = models.CharField(max_length=254)
    no_of_port = models.CharField(max_length=254)
    installati = models.CharField(max_length=254)
    condition = models.CharField(max_length=254)
    geom = models.MultiPolygonField(srid=4326)  
   
    
    def __str__(self):
        return self.spliter_ty

    class Meta:
        verbose_name_plural = "Zones"

class Clients(models.Model):
    pon_type = models.CharField(max_length=254, default='', blank=True, null=True)
    client_nam = models.CharField(max_length=254, default='', blank=True, null=True)
    olt = models.CharField(max_length=254, default='', blank=True, null=True)
    zone = models.CharField(max_length=254, default='', blank=True, null=True)
    address = models.CharField(max_length=254, default='', blank=True, null=True)
    building_t = models.CharField(max_length=254, default='', blank=True, null=True)  
    latitude = models.FloatField(default='', blank=True)
    longitude = models.FloatField(default='', blank=True)
    odb_split = models.CharField(max_length=254, default='', blank=True, null=True)  
    geom = models.MultiPointField(srid=4326)
    
    def __str__(self):
        return str(self.client_nam) if self.client_nam else f"Client {self.id}"

    class Meta:
        verbose_name_plural = "Clients"
   

@receiver(post_save, sender=Routes)
@receiver(post_save, sender=Fats)
@receiver(post_save, sender=Closures)
@receiver(post_save, sender=Mains)
@receiver(post_save, sender=Center)
@receiver(post_save, sender=Zone)
@receiver(post_save, sender=Splitters)
@receiver(post_save, sender=Clients)
@receiver(post_save, sender=Notification)
def track_changes(sender, instance, **kwargs):
    #Logic to track changes and update instance.changes
    instance.changes = "Details of changes made..."
    instance.save()
def notify_changes(sender, instance, **kwargs):
    # Create a notification instance for the changes
    Notification.objects.create(
        content=f"Change made to {sender.__name__} with ID {instance.id}",
        timestamp=timezone.now()
    )

