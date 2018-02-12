from django.conf import settings
from django.db import models


class Photo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/orig')
    filtered_image = models.ImageField(upload_to='uploads/%Y/%m/%d/filtered', blank=True)
    content = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        self.image.delete()
        self.filtered_image.delete()
        super(Photo, self).delete(*args, **kwargs)
