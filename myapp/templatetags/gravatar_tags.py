# Create this file in your Django app (e.g., myapp/templatetags/gravatar_tags.py)

import hashlib
from django import template

register = template.Library()

@register.filter(name='md5')
def md5_email(email):
    return hashlib.md5(email.encode('utf-8')).hexdigest()
