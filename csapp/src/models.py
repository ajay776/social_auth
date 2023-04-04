from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField

# Create your models here.
class Blog(models.Model):
       title = models.CharField(max_length=1000)
       author = models.ForeignKey(User, on_delete=models.CASCADE)
       thumbnail  = models.ImageField(upload_to ='thumbnails/', null=True , blank=True)
       content = FroalaField()
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)


       def __str__(self):
           return self.title + "--------------> BY " + self.author.username


class Comment(models.Model):
    comment_text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    sub_comment_of = models.ForeignKey("Comment", on_delete=models.CASCADE, null=True, blank=True, default=None)
    blog  = models.ForeignKey(Blog, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author.username + " " + self.comment_text[:20] + "...." 
    