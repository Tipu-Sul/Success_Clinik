from rest_framework.routers import DefaultRouter
from. import views
from django.urls import path,include

router=DefaultRouter()
router.register('doctor_list',views.DoctorViewSet)
router.register('designation_list',views.DesignationViewSet)
router.register('specialization_list',views.SpecializationViewSet)
router.register('available_time_list',views.AvailableTimeViewSet)
router.register('review_list',views.ReviewViewSet)

urlpatterns = [
    path('', include(router.urls))
]


