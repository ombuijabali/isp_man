from django.urls import path, include
from . import views 
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .views import home, about, faqs, signup, settings, notifications, route_datasets, fats_dataset, buildings_dataset, mains_dataset, centers_dataset, update_profile, spliters_dataset, closures_dataset

urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),  # Landing page is the login view
    path('about/', login_required(about), name='about'),
    path('route_data/', route_datasets, name='routes'),
    path('fats_data/', fats_dataset, name='fats'),
    path('buildings_data/', buildings_dataset, name='buildings'),  
    path('mains_data/', mains_dataset, name='mains'), 
    path('centers_data/', centers_dataset, name='centers'),
    path('spliters_data/', spliters_dataset, name='spliters'),
    path('closures_data/', closures_dataset, name='closure'),
     # Update endpoints
    path('route_data/<int:feature_id>/update/', route_datasets, name='update_route'),
    path('fats_data/<int:feature_id>/update/', fats_dataset, name='update_fat'),
    path('buildings_data/<int:feature_id>/update/', buildings_dataset, name='update_building'),
    path('mains_data/<int:feature_id>/update/', mains_dataset, name='update_main'),
    path('centers_data/<int:feature_id>/update/', centers_dataset, name='update_center'),
    path('spliters_data/<int:feature_id>/update/', spliters_dataset, name='update_spliter'),
    path('closures_data/<int:feature_id>/update/', closures_dataset, name='update_closure'),
    
    #USER URLS
    path('faqs/', login_required(faqs), name='faqs'),
    path('home/', login_required(home), name='home'),
    path('notifications/', login_required(notifications), name='notifications'),
    path('notifications/<int:notification_id>/', login_required(notifications), name='notification_detail'),
    path('settings/', login_required(settings), name='settings'),
    path('update_profile/', update_profile, name='update_profile'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
