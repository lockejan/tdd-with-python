from django.conf import settings
from django.db import models
from django.urls import reverse
from django.conf import settings


class List(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("view_list", args=[self.id])

    @staticmethod
    def create_new(first_item_text, owner=None):
        new_list = List.objects.create(owner=owner)
        Item.objects.create(text=first_item_text, list=new_list)
        return new_list

    @property
    def name(self):
        return self.item_set.first().text


class Item(models.Model):
    text = models.TextField(default="")
    list = models.ForeignKey(List, default=None)

    class Meta:
        ordering = ["id"]
        unique_together = (("list", "text"),)

    def __str__(self):
        return self.text
