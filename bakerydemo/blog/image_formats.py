from wagtail.images.formats import Format, register_image_format

register_image_format(Format('halfwidth', 'HalfWidth', 'richtext-image halfwidth','height-300'))