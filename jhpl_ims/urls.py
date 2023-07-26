from django.urls import path, reverse_lazy
from . import views

app_name = 'jhpl_ims'

urlpatterns = [

    path('', views.index.as_view(), name='index'),
    path('procedures/<int:pk>', views.procedures.as_view(), name='procedures'),
    path('master-list/<int:pk>/update', views.MasterUpdateView.as_view(
        success_url=reverse_lazy('jhpl_ims:index')), name='jhplmaster_update'),
    path('sop/<int:pk>/comment', views.NotesCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/delete', views.NotesDeleteView.as_view(success_url=reverse_lazy('jhpl_ims:index')), name='comment_delete'),
    path('incidents', views.IncidentListView.as_view(), name='incident_list'),
    path('incidentdetail/<int:pk>', views.IncidentDetailView.as_view(), name='incident_detail'),
    path('incident/<int:pk>/delete', views.IncidentDeleteView.as_view(success_url=reverse_lazy('jhpl_ims:incident_list')), name='incident_delete'),
    path('incident/create', views.IncidentCreateView.as_view(), name='incident_create'),
    path('incident_picture/<int:pk>', views.stream_file, name='incident_picture'),
    path('incident/<int:pk>/update',views.IncidentUpdateView.as_view(success_url=reverse_lazy('jhpl_ims:incident_list')), name='incident_update'),
    
    
]
