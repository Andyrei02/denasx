from django.db import models


# class SocialLink(models.Model):
#     name = models.CharField(max_length=50)
#     url = models.URLField()

#     def __str__(self):
#         return self.name

# class ImageAsset(models.Model):
#     name = models.CharField(max_length=50)
#     image = models.ImageField(upload_to='images/')

#     def __str__(self):
#         return self.name

# class Description(models.Model):
#     text = models.TextField()

#     def __str__(self):
#         return "Site Description"


class HeaderContent(models.Model):
    gif = models.ImageField(upload_to='gifs/')
    comment = models.CharField(max_length=200)
    cover_image = models.ImageField(upload_to='covers/')
    video_link = models.URLField()

    def __str__(self):
        return f"Header Content: {self.comment[:20]}"
