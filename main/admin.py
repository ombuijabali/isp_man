from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Routes, Fats, UserProfile, Clients, Mains, Center, Closures, Notification, Splitters, Photo

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('content', 'timestamp')
    search_fields = ('content',)
    readonly_fields = ('content', 'timestamp')

@admin.register(Routes)
class RoutesAdmin(LeafletGeoAdmin):
    list_display = ('route_name',)
    search_fields = ('route_name',)

    def save_model(self, request, obj, form, change):    
        super().save_model(request, obj, form, change)

@admin.register(Mains)
class MainsAdmin(LeafletGeoAdmin):
    list_display = ('main_name',)
    search_fields = ('main_name',)

    def save_model(self, request, obj, form, change):    
        super().save_model(request, obj, form, change)

@admin.register(Fats)
class FatsAdmin(LeafletGeoAdmin):
    list_display = ('fat_name',)
    search_fields = ('fat_name',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

@admin.register(Closures)
class ClosuresAdmin(LeafletGeoAdmin):
    list_display = ('closore_na',)
    search_fields = ('closore_na',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

@admin.register(Splitters)
class SplitersAdmin(LeafletGeoAdmin):
    list_display = ('spliter_na',)
    search_fields = ('spliter_na',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

@admin.register(Center)
class CentersAdmin(LeafletGeoAdmin):
    list_display = ('main_route',)
    search_fields = ('main_route',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

@admin.register(Clients)
class ClientsAdmin(LeafletGeoAdmin):
    list_display = ('address', 'client_nam',)
    search_fields = ('address', 'client_nam',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

admin.site.register(Photo)
        
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email', 'phone_number')
    search_fields = ('user__username', 'first_name', 'last_name', 'email', 'phone_number')
