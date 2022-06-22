from django.core.mail import send_mail


def send_activation_code(email, activation_code):
    activation_url = f'http://localhost:8000/api/v1/account/activate/{activation_code}'
    message = f"""
        Thank you for registrate in our Online Shop !
        To activate your account click here {activation_url}
        """
    send_mail('Activate your account',
              message,
              'admin@admin.com',
              [email, ],
              fail_silently=False, )
