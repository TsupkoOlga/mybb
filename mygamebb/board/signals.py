from django.db.models.signals import post_save
from django.template.loader import render_to_string
from django.conf import settings
from django.dispatch import receiver
from .views import *
from .models import *
from django.core.mail import EmailMultiAlternatives


@receiver(post_save, sender=Comment)
def notify_reply(sender, instance, created, **kwargs):
    if created:
        html_content = render_to_string(
            'new_comment_email.html',
            {'link': f'{settings.SITE_URL}/accounts/profile/'}
        )
        replies=Comment.objects.all()
        person = [replies[0].bulletin.user.email]
        status='Получен новый отклик'
    else:
        html_content = render_to_string('confirm_comment_email.html')

        person = [User.objects.filter(id=instance.user.id)[0].email]
        status = 'Одобрен отклик'

    msg = EmailMultiAlternatives(
        subject=status,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=person
    )

    msg.attach_alternative(html_content, "text/html")
    msg.send()

@receiver(post_save, sender=News)
def notify_new(sender, instance, **kwargs):
    html_content = render_to_string(
        'new_email.html',
        {
            'link': f'{settings.SITE_URL}/news/'
        }
    )
    persons = set(User.objects.all().values_list('email', flat=True))

    msg = EmailMultiAlternatives(
        subject='Опубликована свежая новость',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=persons
    )

    msg.attach_alternative(html_content, "text/html")
    msg.send()

