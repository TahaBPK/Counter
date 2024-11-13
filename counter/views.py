from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Counter
from .serializers import CounterSerializer

class CounterView(APIView):
    def get(self, request):
        # Get the counter object, or create it if it doesn't exist
        counter, created = Counter.objects.get_or_create(id=1)
        # Increment the counter
        counter.value += 1
        counter.save()
        # Serialize the response
        serializer = CounterSerializer(counter)
        return Response(serializer.data)

