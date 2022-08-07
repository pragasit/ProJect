from django.core.exceptions import ValidationError

def file_size(value):
    filesize=value.siz.encode()
    if filesize>1000000:
        raise ValidationError("Maximum size is 10mb")