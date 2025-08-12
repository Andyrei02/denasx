from django.contrib import admin
# from .models import SocialLink, ImageAsset, Description


# admin.site.register(SocialLink)
# admin.site.register(ImageAsset)
# admin.site.register(Description)

from .models import HeaderContent

@admin.register(HeaderContent)
class HeaderContentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'video_link')

    readonly_fields = ('gif_preview', 'cover_preview')

    def gif_preview(self, obj):
        if obj.gif:
            return f'<img src="{obj.gif.url}" style="max-height:150px;">'
        return "-"
    gif_preview.allow_tags = True

    def cover_preview(self, obj):
        if obj.cover_image:
            return f'<img src="{obj.cover_image.url}" style="max-height:150px;">'
        return "-"
    cover_preview.allow_tags = True
