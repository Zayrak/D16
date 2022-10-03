from django.db.models.signals import post_save

from django.core.mail import EmailMultiAlternatives

from django.template.loader import render_to_string

from django.dispatch import receiver

from .models import Response


@receiver(post_save, sender=Response)
def notify_managers_appointment(sender, instance, created, **kwargs):
    html_content = render_to_string('mail_response.html', {'response': instance, })
    mail_subject = ''
    user = None

    if instance.accepted:
        user = instance.id_user
        mail_subject = f'{user}, Ваш отзыв на статью "{instance.id_advert}" принят!'
    else:
        user = instance.id_advert.id_user
        mail_subject = f'{user}! К вашей статье "{instance.id_advert}" оставлен новый комментарий!'

    msg = EmailMultiAlternatives(
        subject=mail_subject,
        body='',
        from_email='*****@yandex.ru',
        to=[user.email],
    )

    msg.attach_alternative(html_content, "text/html")
    msg.send()
