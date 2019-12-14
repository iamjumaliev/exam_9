from django import forms


from webapp.models import Photo, Comment


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['author', 'created_at']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['author', 'created_at','picture']




