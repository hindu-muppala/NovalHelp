from django.shortcuts import render

# Create your views here.
# myapp/views.py
from django.shortcuts import render

def map_view(request):
    # Sample data
    data = [
        {
            "time": "2024-10-25T12:00:00Z",
            "latitude": 37.7749,
            "longitude": -122.4194,
            "text": "San Francisco",
            "object": "Location A"
        },
        {
            "time": "2024-10-25T15:30:00Z",
            "latitude": 34.0522,
            "longitude": -118.2437,
            "text": "Los Angeles",
            "object": "Location B"
        },
    ]
    return render(request, 'templates\survellence.html', {'data': data})
