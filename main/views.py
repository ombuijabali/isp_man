from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, UserProfileForm
from .models import Routes, Fats, UserProfile, Clients, Mains, Center, Closures, Notification, Splitters, Photo, Zone
from django.db import models 
import json
from django.db.models import Count, Q
from django.contrib.auth.decorators import login_required

def home(request):
    # Get the total number of mapped routes and fats.
    total_mapped_routes = Routes.objects.exclude(geom__isnull=True).count()
    total_mapped_fats = Fats.objects.exclude(geom__isnull=True).count()
    total_mapped_buildings = Clients.objects.exclude(geom__isnull=True).values('address').distinct().count()
    total_mapped_mains = Mains.objects.exclude(geom__isnull=True).count()
    total_mapped_centers = Center.objects.exclude(geom__isnull=True).count()
    total_mapped_closures = Closures.objects.exclude(geom__isnull=True).count()
    total_mapped_splitters = Closures.objects.exclude(geom__isnull=True).count()

    #Charts
    mains_data = Mains.objects.exclude(geom__isnull=True).values('main_name', 'length')
    splitters_types_count = list(Splitters.objects.exclude(spliter_ty__isnull=True).values('spliter_ty').annotate(count=models.Count('spliter_ty')))
    splitters_ports_count = list(Splitters.objects.exclude(no_of_port__isnull=True).values('no_of_port').annotate(count=models.Count('no_of_port')))
    buildings_count = list(Clients.objects.exclude(building_t__isnull=True).values('building_t').annotate(count=models.Count('building_t')))
    pon_types_count = list(Clients.objects.exclude(pon_type__isnull=True).values('pon_type').annotate(count=models.Count('pon_type')))
    total_connections = Clients.objects.count()


    # Convert the list to JSON manually
    splitter_types_json = json.dumps(splitters_types_count)
    splitter_ports_json = json.dumps(splitters_ports_count)
    building_types_json = json.dumps(buildings_count)
    pon_types_json = json.dumps(list(pon_types_count))
    mains_json = json.dumps(list(mains_data))

    # Initialize query variable
    query = request.GET.get('search_query')

    # Pass the total number of mapped routes and fats to the template.
    context = {
        'total_mapped_routes': total_mapped_routes,
        'total_mapped_fats': total_mapped_fats,
        'total_mapped_buildings': total_mapped_buildings,
        'total_mapped_mains': total_mapped_mains,
        'total_mapped_centers': total_mapped_centers,
        'total_mapped_closures': total_mapped_closures,
        'splitter_types': splitter_types_json,  
        'splitter_ports': splitter_ports_json, 
        'building_types': building_types_json,
        'pon_types': pon_types_json,
        'total_connections': total_connections,
        'mains_data': mains_json,
        'query': query  # Include the query in the context
    }


    if query:
        # Perform a case-insensitive search for building names
        buildings = Clients.objects.filter(
            Q(address__icontains=query) |
            Q(client_nam__icontains=query) |
            Q(olt__icontains=query) |
            Q(odb_split__icontains=query)
        )
        routes = Routes.objects.filter(route_name__icontains=query)
    else:
        # If no search query, display all buildings
        buildings = Clients.objects.all()
        routes = None

    return render(request, 'isp/home.html', {'buildings': buildings, 'routes': routes, 'query': query, **context})

def about(request):
    return render(request, 'isp/about.html')

def route_datasets(request):
    routes = serialize('geojson', Routes.objects.all())
    return HttpResponse(routes, content_type='application/json')

def fats_dataset(request):
    fats = serialize('geojson', Fats.objects.all())
    return HttpResponse(fats, content_type='application/json')

def spliters_dataset(request):
    spliters = serialize('geojson', Splitters.objects.all())
    return HttpResponse(spliters, content_type='application/json')

def closures_dataset(request):
    closures = serialize('geojson', Closures.objects.all())
    return HttpResponse(closures, content_type='application/json')

def buildings_dataset(request):
    buildings = serialize('geojson', Clients.objects.all())
    return HttpResponse(buildings, content_type='application/json')

def mains_dataset(request):
    mains = serialize('geojson', Mains.objects.all())
    return HttpResponse(mains, content_type='application/json')

def centers_dataset(request):
    centers = serialize('geojson', Center.objects.all())
    return HttpResponse(centers, content_type='application/json')

def zones_dataset(request):
    zones = serialize('geojson', Zone.objects.all())
    return HttpResponse(zones, content_type='application/json')

@login_required
def notifications(request, notification_id=None):
    if notification_id:
        notification = get_object_or_404(Notification, id=notification_id)
        notification.is_read = True
        notification.save()

        # Split changes into a list
        changes_list = notification.changes.split('\n')

        return render(request, 'isp/notification_detail.html', {'notification': notification, 'changes_list': changes_list})
    else:
        notifications = Notification.objects.all().order_by('-timestamp')
        unread_notification_count = Notification.objects.filter(is_read=False).count()
        return render(request, 'isp/notifications.html', {'notifications': notifications, 'unread_notification_count': unread_notification_count})

def settings(request):
    return render(request, 'isp/settings.html')

def update_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile successfully updated!')
            return redirect('update_profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)

    return render(request, 'isp/settings.html', {'form': form})
    
def faqs(request):
    faqs = [
        {
            'question': 'What is GIS?',
            'answer': 'GIS is a geographic information system that deals with location data also known as spatial data and allows manipulation, analysis, editing and visualization of the data for better decision making'
        },
        {
            'question': 'GIS in Fibre Network Analysis',
            'answer': 'GIS plays a crucial role in network management, enabling ISPs (Internet Service Providers) to visualize, plan, and maintain their fiber optic networks. By mapping fiber routes, FATs (Fiber Access Terminals), splitters, and other network elements, ISPs can optimize network performance, identify potential issues, and plan for future expansion.'
        },
         {
            'question': 'GIS Data Types?',
            'answer': 'GIS has various data types that support mapping of spatial data. They include points, polylines and polygons. Points are datasets with single dimensions, ie, coordinates. Polylines are datasets that are joined from points to form lines while polygons have shapes drawn on them.'
        },
         {
            'question': 'Data Types for varous datasets in the ISP Manager',
            'answer': 'Fibre routes are polylines, buildings are polygons while FATs,Splitters and Closure Kitsare all point data. Data Centers are polygons as well as they fall under buildings category'
        },
        {
            'question': 'What is QGIS and how to connect it with our database?',
            'answer': 'QGIS is a geospatial editting software that allows users to manipulate spatial data for analysis. It allows users to connect to their databases by creating new connections. Right click on postgres and add your connection. On the menu bar, proceed to DB Manager and import your data.'
        },
        {
            'question': 'How do I add a new route/FAT/Splitters/Closure Kits?',
            'answer': 'Open QGIS and enable toogle editing on the layer of intrest. After adding new information to your existing ones, save your edits. Connect with your database and import the new layer. This will create a new feature and the newly added information will dynamically be updated in the frontend of the application.'
        },
        {
            'question': 'What is Data Security and how is it protected?',
            'answer': 'Data Security is paramount in GIS due to sensitive and critical nature of the information used in the ISP industry. ISP Manager has implemented the best practices to enhance data security including: Privacy, Data Integrity, Compliance and Business Continuity preventing data vreaches or loss of any critical information.'
        },
        {
            'question': 'Why is GIS important in ISP network management?',
            'answer': 'GIS provides a spatial understanding of network infrastructure, helping ISPs make informed decisions, optimize resources, and enhance overall network efficiency. It enables visualizing network elements on a map, which is crucial for planning, monitoring, and maintenance.'
        },
        {
            'question': 'Can I customize the map view?',
            'answer': 'Yes, you can customize the map view based on your preferences. The application allows users to toggle between different map layers, adjust zoom levels, and apply filters to focus on specific elements like fiber routes, FATs, or buildings.'
        },
        {
            'question': 'How does GIS assist in network expansion?',
            'answer': 'GIS aids in identifying potential areas for network expansion by analyzing existing coverage, population density, and demand. This data-driven approach helps ISPs plan new routes and infrastructure deployment to meet growing connectivity needs.'
        },
        {
            'question': 'What information is available for each network feature?',
            'answer': 'For each feature such as fiber routes, FATs, Splitters, Closure Kits, and buildings, the application provides detailed attribute information. This includes names, descriptions, timestamps, and other relevant data to help users understand the characteristics of each element.'
        },
        {
            'question': 'Is the GIS data real-time?',
            'answer': 'The GIS data is updated regularly, but it might not always reflect real-time changes. The frequency of updates depends on the data source and the network management practices. Users can rely on the most recent available data for decision-making.'
        },
        {
            'question': 'How can I report issues or suggest improvements?',
            'answer': 'To report issues or suggest improvements, users can utilize the feedback or contact options provided in the application. The development team values user input and actively considers feedback for enhancing the functionality and user experience.'
        },
        {
            'question': 'Can I export GIS data for analysis?',
            'answer': 'Yes, the application supports exporting GIS data for further analysis. Users can export data in various formats, such as CSV or GeoJSON, depending on their analysis requirements. This feature enhances the compatibility of GIS data with other tools.'
        },
    ]

    return render(request, 'isp/faqs.html', {"faqs": faqs})


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})
