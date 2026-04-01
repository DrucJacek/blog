from rest_framework import serializers
from .models import Blog, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class BlogSerializer(serializers.ModelSerializer):
    queryset = Tag.objects.all()
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=queryset)

    class Meta:
        model = Blog
        fields = ['id','title', 'date', 'content', 'tags']

    def validate_tags(self, data):
        if len(data) == 0:
            raise serializers.ValidationError("You must choose at least one tag")

        for i in data:
            if data[i] == 0:
                raise serializers.ValidationError("You must choose a valid tag")
                
        return data

