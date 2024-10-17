from rest_framework import serializers
from .models import Post, Author

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

        def create(self, validated_data):
            return Post.objects.create(**validated_data)

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'