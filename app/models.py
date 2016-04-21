from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible
from django.conf import settings

@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(self.path, filename)
    
class User(models.Model):
    user = models.CharField(max_length=200)
    device_token = models.CharField(max_length=200, null=True)

class Option():
    user = models.ForeignKey(User, related_name='options')
    use = models.IntegerField(default=0)
    area = models.IntegerField(default=1)
    security_deposit = models.IntegerField(default=0)
    month_price = models.IntegerField(default=0)
    
class Board(models.Model):
    user = models.ForeignKey(User, related_name='boards')
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    cost = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    date = models.CharField(max_length=200)

class BoardImage(models.Model):
    board = models.ForeignKey(Board, related_name='images')
    image = models.ImageField(
        upload_to=PathAndRename('board_img'),
        height_field="image_height",
        width_field="image_width",
        null=True,
        blank=True,
        editable=True,
        help_text="Board Picture",
        verbose_name="Board Picture"
        )
    image_height = models.PositiveIntegerField(null=True, blank=True, editable=False, default="100")
    image_width = models.PositiveIntegerField(null=True, blank=True, editable=False, default="100")
    class Meta:
        unique_together = ('image',)

    def __unicode__(self):
        a = 'http://hanyang24.vps.phps.kr/media/' + str(self.image)
        return '%s' % (a)

class Comment(models.Model):
    board = models.ForeignKey(Board, related_name='comments')
    user = models.ForeignKey(User, related_name='comments')
    content = models.CharField(max_length=200)
    date = models.CharField(max_length=200)

class Room(models.Model):
    floor = models.IntegerField()
    security_deposit = models.IntegerField()
    month_price = models.IntegerField()
    management_cost = models.IntegerField(null=True)
    air_conditioner = models.IntegerField(null=True)
    washer = models.IntegerField(null=True)
    bed = models.IntegerField(null=True)
    fire_type = models.IntegerField(null=True)
    desk = models.IntegerField(null=True)
    term = models.CharField(max_length=200)
    hash1 = models.CharField(max_length=200, null=True)
    hash2 = models.CharField(max_length=200, null=True)
    hash3 = models.CharField(max_length=200, null=True)
    detail = models.TextField(null=True)
    veranda = models.IntegerField()
    kitchen = models.IntegerField()
    tv = models.IntegerField()
    microwave = models.IntegerField()
    two_room = models.IntegerField()
    area = models.IntegerField(default=1)
    size = models.IntegerField(default=0)
    elevator = models.IntegerField(default=0)
    wardrobe = models.IntegerField(default=0)
    
class RoomImage(models.Model):
    room = models.ForeignKey(Room, related_name='images')
    image = models.ImageField(
        upload_to=PathAndRename('room_img'),
        height_field="image_height",
        width_field="image_width",
        null=True,
        blank=True,
        editable=True,
        help_text="Room Picture",
        verbose_name="Room Picture"
        )
    image_height = models.PositiveIntegerField(null=True, blank=True, editable=False, default="100")
    image_width = models.PositiveIntegerField(null=True, blank=True, editable=False, default="100")
    class Meta:
        unique_together = ('image',)

    def __unicode__(self):
        a = 'http://hanyang24.vps.phps.kr/media/' + str(self.image)
        return '%s' % (a)
