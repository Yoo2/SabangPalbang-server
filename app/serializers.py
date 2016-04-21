from rest_framework import serializers
from app.models import Room, RoomImage, User, Board, BoardImage, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'user')

class RoomSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Room
        fields = ('id', 'floor', 'security_deposit', 'month_price', 'management_cost', 'air_conditioner', 'washer', 'bed', 'fire_type', 'desk', 'term', 'hash1', 'hash2', 'hash3', 'detail', 'veranda', 'kitchen', 'tv', 'microwave', 'two_room', 'area', 'images', 'size', 'elevator', 'wardrobe')

class BoardSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many=True)
    user = serializers.ReadOnlyField(source='user.user', read_only=True)
    
    class Meta:
        model = Board
        fields = ( 'id', 'user', 'title', 'content', 'cost', 'item', 'date', 'images')

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.user', read_only=True)
        
    class Meta:
        model = Comment
        fields = ('user', 'content', 'date')

class BoardDetailSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many=True)
    user = serializers.ReadOnlyField(source='user.user', read_only=True)
    comments = CommentSerializer(many=True)
    
    class Meta:
        model = Board
        fields = ( 'id', 'user', 'title', 'content', 'cost', 'item', 'date', 'images', 'comments')

