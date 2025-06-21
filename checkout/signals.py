from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Order, OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update the order total when an OrderLineItem is saved.
    """
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update the order total when an OrderLineItem is deleted.
    """
    instance.order.update_total()