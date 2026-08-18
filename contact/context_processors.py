from .form import ContactForm

def contact_form(request):
    return {'footer_contact_form': ContactForm()}