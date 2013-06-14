from django.db import models
from django.contrib.contenttypes.models import ContentType

class InheritanceCastModel(models.Model):
    """
    An abstract base class that provides a ``real_type`` FK to ContentType.

    For use in trees of inherited models, to be able to downcast
    parent instances to their child types.

    """
    real_type = models.ForeignKey(ContentType, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.real_type = self._get_real_type()

        super(InheritanceCastModel, self).save(*args, **kwargs)

    def _get_real_type(self):
        return ContentType.objects.get_for_model(type(self))

    def cast(self):
        return self.real_type.get_object_for_this_type(pk=self.pk)

    class Meta:
        abstract = True

class Post(InheritanceCastModel):
    description = models.TextField(max_length=500)
    author = models.CharField(max_length=80)
    author_thumbnail_url = models.CharField(max_length=500)
    url = models.URLField()
    created_at = models.DateTimeField()
    original_id = models.CharField(max_length=800)
    featured = models.BooleanField(default=False)

    class Meta:
        abstract = True

class InstagramPost(Post):
    image_url = models.CharField(max_length=500)

class TwitterPost(Post):
    pass

class FacebookPost(Post):
    content = models.TextField()