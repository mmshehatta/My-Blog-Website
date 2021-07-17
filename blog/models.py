from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from PIL import Image



# *********************************** Post Model **********
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    date_posted = models.DateTimeField(default=timezone.now)
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length = 50 , blank=True , null=True , allow_unicode=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            if not self.slug:
                self.slug = arabic_slugify(self.title)
        # self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-home')

    class Meta:
        ordering=('-date_posted',)


def arabic_slugify(str):
    str = str.replace(" ", "-")
    str = str.replace(",", "-")
    str = str.replace("(", "-")
    str = str.replace(")", "")
    str = str.replace("؟", "")
    return str

# *********************************** Comment Model **********

class Comment(models.Model):
    name=models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    user_image = models.ImageField(default='default.jpg', upload_to='user_comment_pics')
    post = models.ForeignKey(Post , on_delete=models.CASCADE , related_name='comments')

    def __str__(self):
        return '{} comment on {} '.format(self.name , self.post)
    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)
        img = Image.open(self.user_image.path)

        if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.user_image.path)
    class Meta:
        ordering = ('comment_date', )

