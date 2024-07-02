from rest_framework import serializers
from ..models import *

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Review
        # fields = '__all__'
        exclude = ('watchlist',)

class WatchListSerializer(serializers.ModelSerializer):
    platform = serializers.CharField(source='platform.name')
    
    class Meta:
        model = WatchList
        fields = '__all__'


class StreamPlatformSerializer(serializers.Serializer): # for hyperlinked API use serializers.HyperlinkedModelSerializer
    watchlist = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = '__all__'
