from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
import uuid


@receiver(post_save, sender=User)
def create_permit_owner_on_user_create(sender, **kwargs):
    """
        Creates a PermitOwner when a new user is created
    """
    if kwargs.get('created', False):
        up = PermitOwner.objects.create(user=kwargs.get('instance'))


class PermitOwner(models.Model):
    user_uuid = models.UUIDField(primary_key=True,
                                 default=uuid.uuid4,
                                 editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='permit_owner')


class FOO_BAR(models.Model):
    """ Fake test model """
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              blank=True,
                              null=True,
                              related_name='foo_bar',
                              on_delete=models.CASCADE)
    foo = models.CharField('foo', max_length=32, default='foo')


class Permit(models.Model):
    """
    A Model for the permit data.
    """
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              blank=True,
                              null=True,
                              related_name='permit',
                              on_delete=models.CASCADE)
    permit_number = models.IntegerField('Permit Number', unique=True)
    master_use_permit = models.IntegerField('Master Use Permit',
                                            blank=True,
                                            null=True)
    action_type = models.CharField('Action Type',
                                   max_length=25,
                                   blank=True,
                                   null=True)
    address = models.CharField('Address', max_length=50, blank=True, null=True)
    applicant_name = models.CharField('Applicant Name',
                                      max_length=128,
                                      blank=True,
                                      null=True)
    date_created = models.DateField('Date Created', auto_now_add=True)
    date_modified = models.DateField('Date Modified', auto_now=True)
    application_date = models.DateTimeField('Application Date',
                                            blank=True,
                                            null=True)
    issue_date = models.DateTimeField('Issue Date', blank=True, null=True)
    final_date = models.DateTimeField('Final Date', blank=True, null=True)
    experation_date = models.DateTimeField('Experation Date',
                                           blank=True,
                                           null=True)
    category = models.CharField('Category',
                                max_length=24,
                                blank=True,
                                null=True)
    description = models.CharField('Description',
                                   max_length=255,
                                   blank=True,
                                   null=True)
    latitude = models.FloatField('Latitude', blank=True)
    longitude = models.FloatField('Longitude', blank=True)
    url = models.URLField('URL', blank=True, null=True)
    permit_type = models.CharField('Type',
                                   max_length=24,
                                   blank=True,
                                   null=True)
    status = models.CharField('Status', max_length=55, blank=True, null=True)
    value = models.FloatField('Value', blank=True, null=True)
    work_type = models.CharField('Work Type',
                                 max_length=24,
                                 blank=True,
                                 null=True)
    contractor = models.CharField('Contractor',
                                  max_length=128,
                                  blank=True,
                                  null=True)

    def __unicode__(self):
        return '{}'.format(self.permit_number)

    def __str__(self):
        return '{}'.format(self.permit_number)
