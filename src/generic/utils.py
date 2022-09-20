from django.core.mail import send_mail
from django.conf import settings


def contact(request):
    if 'contactButton' in request.POST:
        email = request.POST['email']
        subject = f"New Hero's Contact - {email}"
        message = request.POST['message']
        send_mail(subject, message, settings.CONTACT_EMAIL,
                  settings.ADMIN_EMAILS)
