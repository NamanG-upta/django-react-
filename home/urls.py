from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
    path('assignments/', include('api.assignments.urls')),
    path('graded-assignments/', include('api.graded_assignments.urls')),
    path('users/', include('users.urls')),
    re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]
