from pioneros.models import *
from django.utils.text import slugify

for obj in News_Events.objects.all():
    obj.slug = slugify(obj.title)
    obj.save()