from django.shortcuts import render
from rest_framework import viewsets,filters,pagination
from. import models
from. import serializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.

    
class DesignationViewSet(viewsets.ModelViewSet) :
    queryset=models.Designation.objects.all()
    serializer_class=serializer.DesignationSerializer

class DoctorPagination(pagination.PageNumberPagination):
    page_size=1
    page_size_query_param=page_size
    max_page_size=100
class AvailabletimeSpeceficDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        doctor_id=request.query_params.get('doctor_id')
        if doctor_id:
            return queryset.filter(doctor=doctor_id)

        return queryset

class SpecializationViewSet(viewsets.ModelViewSet) :
    queryset=models.Specialization.objects.all()
    serializer_class=serializer.SpecializationSerializer

class AvailableTimeViewSet(viewsets.ModelViewSet) :
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset=models.AvailableTime.objects.all()
    serializer_class=serializer.AvailableTimeSerializer
    filter_backends=[AvailabletimeSpeceficDoctor]

class DoctorViewSet(viewsets.ModelViewSet) :
    queryset=models.Doctor.objects.all()
    serializer_class=serializer.DoctorSerializer
    filter_backends=[filters.SearchFilter]
    pagination_class=DoctorPagination
    search_fields=['user__first_name','user__email','designation__name','specialization__name']

class ReviewViewSet(viewsets.ModelViewSet) :
    queryset=models.Review.objects.all()
    serializer_class=serializer.ReviewSerializer


