from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import AcademicSession, AcademicTerm


@receiver(post_save, sender=AcademicSession)
def after_saving_session(sender, created, instance, *args, **kwargs):
    """Change all academic sessions to false if this is true"""
    if instance.current is True:
        AcademicSession.objects.exclude(pk=instance.id).update(current=False)


@receiver(post_save, sender=AcademicTerm)
def after_saving_term(sender, created, instance, *args, **kwargs):
    """Change all academic terms to false if this is true."""
    if instance.current is True:
        AcademicTerm.objects.exclude(pk=instance.id).update(current=False)
