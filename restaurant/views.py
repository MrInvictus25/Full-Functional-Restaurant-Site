from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu
from django.core import serializers
from .models import Booking
from datetime import datetime
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import MenuSerializer, BookingSerializer

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def reservations(request):
    date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html',{"bookings":booking_json})

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add your code here to create new views
def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 

@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        data = json.load(request)
        exist = Booking.objects.filter(reservation_date = data['reservation_date']).filter(
            reservation_slot = data['reservation_slot']).exists()
        if exist == False:
            booking = Booking(
                first_name = data['first_name'],
                reservation_date = data['reservation_date'],
                reservation_slot = data['reservation_slot'],
            )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type = 'application/json')
    
    date = request.GET.get('date',datetime.today().date())
    
    if date == '':
        date = datetime.today().date()
    #print('TODAY', date)

    bookings = Booking.objects.all().filter(reservation_date = date)
    booking_json = serializers.serialize('json', bookings)

    return HttpResponse(booking_json, content_type ='application/json')

class bookingview(APIView):
    #permission_classes = [IsAuthenticated]
    def get(self, request):
        items = Booking.objects.all()
        serializer = BookingSerializer(items, many=True)
        return Response(serializer.data) # Return JSON
    
    def post(self, request):
        serializer = BookingSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"Status": "Success", "Data": serializer.data})

class menuview(APIView):
    #permission_classes = [IsAuthenticated]
    def get(self, request):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        return Response(serializer.data) # Return JSON
    
    # def post(self, request):
    #     serializer = MenuSerializer(data = request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"Status": "Success", "Data": serializer.data})
    
class Menuview(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuview(generics.RetrieveUpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

@api_view()
@permission_classes([IsAuthenticated])

def access(request):
    return Response({"message":"This view is protected"})