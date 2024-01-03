# # gravatar_tags.py
import hashlib
import urllib.parse
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def gravatar_url(email, size=40):
    default = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSIWQALj-EQkmJDYNOQKQPi3qA2ctjIYbrowRMegbJjWqC6t8eg-OFkmRoivSXSPuwjDyg&usqp=CAU"
    hash_value = hashlib.md5(email.lower().encode('utf-8')).hexdigest()
    params = urllib.parse.urlencode({'d': default, 's': str(size)})
    return f"https://www.gravatar.com/avatar/{hash_value}?{params}"

@register.filter
def gravatar(email, size=40):
    url = gravatar_url(email, size)
    return mark_safe(f'<img src="{url}" width="{size}" height="{size}">')
