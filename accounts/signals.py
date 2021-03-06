from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Account


@receiver(post_save, sender=User)
def create_user_account(sender, instance, **kwargs):
    try:
        instance.account.save()
    except ObjectDoesNotExist:
        Account.objects.create(user=instance)


@receiver(pre_delete, sender=User)
def delete_user_account(sender, instance, **kwargs):
    instance.account.delete()
