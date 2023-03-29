from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings


def send_email(subject: str, template_name: str, token: str, email: str) -> None:
    """
    The 'send_email' function sends an email to a specified email address using Django email backend
    It requires the following parameters:

    :param subject: The subject of the email.
    :param template_name: The name of the email template to use
    :param token: The token to be included in the email message.
    :param email: The email address to which the message will be sent.
    :return: None
    """
    template = render_to_string(template_name,
                                {'token': token})
    subject_email = subject
    email = EmailMessage(
        subject_email,
        template,
        settings.EMAIL_HOST_USER,
        [email]
    )
    email.fail_silently = False
    email.send()