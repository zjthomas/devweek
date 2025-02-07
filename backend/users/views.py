from rest_framework import viewsets

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# For testing purposes

from django.http import JsonResponse
from .fingerprint_integration import get_fingerprint_data

# Create a view to handle fingerprint API call
def fingerprint_view(request):
    try:
        # Fetch the visitor data using the Fingerprint API
        visitor_data = get_fingerprint_data()

        # Return the data as a JSON response
        return JsonResponse(visitor_data, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# For testing purposes
