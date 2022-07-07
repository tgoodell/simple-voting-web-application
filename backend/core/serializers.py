from rest_framework import serializers
from .models import Candidate


class CandidateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Candidate
        fields = ("id", "title", "picture", "author", "category", "description", "votes")