from rest_framework import viewsets
from .serializers import CandidateSerializer
from .models import Candidate


class CandidateViewSet(viewsets.ModelViewSet):
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all()
