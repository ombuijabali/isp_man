from django.urls import path, include
from . import views 
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Authentication URLs
    path('', auth_views.LoginView.as_view(), name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Feature Data URLs - Combined list and detail endpoints
    path('route_data/', login_required(views.route_datasets), name='routes'),
    path('route_data/<int:feature_id>/', login_required(views.route_datasets), name='route_detail'),
    
    path('fats_data/', login_required(views.fats_dataset), name='fats'),
    path('fats_data/<int:feature_id>/', login_required(views.fats_dataset), name='fat_detail'),
    
    path('buildings_data/', login_required(views.buildings_dataset), name='buildings'),
    path('buildings_data/<int:feature_id>/', login_required(views.buildings_dataset), name='building_detail'),
    
    path('mains_data/', login_required(views.mains_dataset), name='mains'),
    path('mains_data/<int:feature_id>/', login_required(views.mains_dataset), name='main_detail'),
    
    path('centers_data/', login_required(views.centers_dataset), name='centers'),
    path('centers_data/<int:feature_id>/', login_required(views.centers_dataset), name='center_detail'),
    
    path('spliters_data/', login_required(views.spliters_dataset), name='spliters'),
    path('spliters_data/<int:feature_id>/', login_required(views.spliters_dataset), name='spliter_detail'),
    
    path('closures_data/', login_required(views.closures_dataset), name='closure'),
    path('closures_data/<int:feature_id>/', login_required(views.closures_dataset), name='closure_detail'),
    
    # User Interface URLs
    path('home/', login_required(views.home), name='home'),
    path('about/', login_required(views.about), name='about'),
    path('faqs/', login_required(views.faqs), name='faqs'),
    path('settings/', login_required(views.settings), name='settings'),
    path('update_profile/', login_required(views.update_profile), name='update_profile'),
    
    # Notifications
    path('notifications/', login_required(views.notifications), name='notifications'),
    path('notifications/<int:notification_id>/', login_required(views.notifications), name='notification_detail'),
]
