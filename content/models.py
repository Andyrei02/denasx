from django.db import models


class HeaderContent(models.Model):
    gif = models.ImageField(upload_to='gifs/')
    comment = models.CharField(max_length=200)
    cover_image = models.ImageField(upload_to='covers/')
    video_link = models.URLField()

    def __str__(self):
        return f"Header Content: {self.comment[:20]}"
