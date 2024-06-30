from rest_framework import serializers
from ..models import *

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        # fields = '__all__'
        exclude = ('watchlist',)

class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = WatchList
        fields = '__all__'


class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = '__all__'


# v3
# class StreamPlatformSerializer(serializers.ModelSerializer):
#     watchlist = WatchListSerializer(many=True, read_only=True)
#     # watchlist = serializers.StringRelatedField(many=True)
#     # watchlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='movie-detail')
    
#     class Meta:
#         model = StreamPlatform
#         fields = '__all__'


# V2
# class MovieSerializer(serializers.ModelSerializer):
#     len_name = serializers.SerializerMethodField()
    
#     class Meta:
#         model = Movie
#         fields = '__all__'
    
#     def get_len_name(self, object):
#         length = len(object.name)
#         return length
        
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Title and Description should be different')
#         else:
#             return data
    
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError('Title is too short')
#         else:
#             return value

# V1
# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError('Title is too short')
#     else:
#         return value

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Title and Description should be different')
#         else:
#             return data
    
#     # V0
#     # def validate_name(self, value):
#     #     if len(value) < 2:
#     #         raise serializers.ValidationError('Title is too short')
#     #     else:
#     #         return value