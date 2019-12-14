from webapp.models import Photo,Comment

from rest_framework import serializers



class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id','text','picture','author','created_at')


class PhotoSerializer(serializers.ModelSerializer):

    comment_picture = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Photo
        fields = ('id', 'picture', 'label' , 'created_at', 'author', 'likes' , 'comment_picture')