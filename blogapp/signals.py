from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.signals import notify
from blogapp.models import Comment


@receiver(post_save, sender=Comment)
def create_comment_notification(sender, instance, created, **kwargs):
    if created:
        post_owner = instance.post.created_by
        if post_owner != instance.commented_by:
            notify.send(
                instance.commented_by,
                recipient=post_owner,
                verb="commented on your post",
                description=instance.comment,
                target=instance.post
            )
