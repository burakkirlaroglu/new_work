from django.db import models


class StartModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        update_fields = kwargs.get('update_fields', None)
        if update_fields is not None:
            update_fields.append('updated_date', 'is_active')
        super(StartModel, self).save(*args, **kwargs)
