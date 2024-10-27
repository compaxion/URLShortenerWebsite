from django.db import models

from shortener.models import KirrURL

class ClickEventManager(models.Manager):
    def create_event(self, kirrInstance):
        if isinstance(kirrInstance, KirrURL):
            obj, created = self.get_or_create(kirr_url=kirrInstance)
            obj.count += 1
            obj.save()
            return obj.count
        return None


class ClickEvent(models.Model):
    kirr_url = models.OneToOneField(KirrURL, on_delete=models.DO_NOTHING)
    count = models.IntegerField(default=0)

    objects = ClickEventManager()

    def __str__(self):
        return "{i}".format(i=self.count)


