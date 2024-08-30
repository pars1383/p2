from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from jobs import views

router = DefaultRouter()
router.register(r'jobads', views.JobAdViewSet)
router.register(r'applications', views.JobApplicationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
