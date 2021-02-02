from django import template

from wagtail.images.models import Image

register = template.Library()


# Retrieves a single gallery item and returns a gallery of images
@register.inclusion_tag('tags/gallery2.html', takes_context=True)
def gallery2(context, gallery):
    images = Image.objects.filter(collection=gallery)

    return {
        'images': images,
        'request': context['request'],
    }
