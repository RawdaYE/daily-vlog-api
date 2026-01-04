from rest_framework import generics, permissions
from .models import Vlog
from .serializers import VlogSerializer

# List all vlogs (optional: filter by user later)
class VlogListCreateView(generics.ListCreateAPIView):
    queryset = Vlog.objects.all().order_by('-created_at')
    serializer_class = VlogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Retrieve, update, delete a single vlog
class VlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vlog.objects.all()
    serializer_class = VlogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Users can only update/delete their own vlogs
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return Vlog.objects.filter(user=self.request.user)
        return Vlog.objects.all()
