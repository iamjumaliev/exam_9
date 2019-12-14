from django.shortcuts import redirect
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response

from webapp.models import Comment


from api.serializers import CommentSerializer





class CommentViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        self.comment = Comment.objects.get(pk=self.kwargs.get('pk'))
        return self.comment

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        elif self.request.method == "DELETE":
            if self.comment.author == self.request.user or self.request.user.has_perm("webapp.delete_comment"):
                return []
        return super().get_permissions()

@action(methods=['post'], detail=True)
def like_up(self, request, pk=None):
    if not request.user.is_authenticated:
        return redirect('webapp:login')
    else:
        photo = self.get_object()
        if request.user == photo.photo_liked.owner:
            photo.likes += 1
            photo.save()
            return Response({'id': photo.pk, 'likes': photo.likes})
        else:
            return Response({'error': 'you have already liked it'})




@action(methods=['post'], detail=True)
def like_down(self, request, pk=None):
    if not request.user.is_authenticated:
        return redirect('webapp:login')
    else:
        photo = self.get_object()
        if request.user == photo.photo_liked.owner:
            photo.likes -= 1
            photo.save()
            return Response({'id': photo.pk, 'likes': photo.likes})
        else:
            return Response({'error': 'you have already disliked'})