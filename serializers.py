from rest_framework import serializers
from avi.models import TutorialModel

class TutorialModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = TutorialModel
        fields = '__all__'
        depth = 2
