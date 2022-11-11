from django.db import models
from django.utils.text import slugify

SLUG_LENGTH = 50


def get_unique_slug(model_instance):
    slugified = slugify(model_instance.name, allow_unicode=True)
    if len(slugified) > SLUG_LENGTH:
        slug = slugified[:SLUG_LENGTH]
    else:
        slug = slugified
    slug_copy = slug
    num = 1
    while model_instance.__class__.objects.filter(slug=slug).exists():
        number_slug = '{0}-{1}'.format(slug_copy, num)
        if len(number_slug) > SLUG_LENGTH:
            trimmed_slug = slug_copy[:-(len(str(num))+1)]
            slug = '{0}-{1}'.format(trimmed_slug, num)
        else:
            slug = number_slug
        num += 1
    return slug


class SlugMixin:
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self)
        super().save(*args, **kwargs)


class Tag(SlugMixin, models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=50, blank=True)
    fathers = models.ManyToManyField('Tag', blank=True, related_name='children')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
