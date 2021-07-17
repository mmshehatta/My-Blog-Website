
from django import forms
from .models import Post , Comment
# ***********  Post Form **************
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        exclude=('author','date_posted' , 'slug')


# ******************* Comment Form **************

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name' , 'email' , 'body', 'user_image']



