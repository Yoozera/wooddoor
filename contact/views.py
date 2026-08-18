from django.shortcuts import redirect
from django.contrib import messages
from .form import ContactForm
from .models import ContactMessage

def submit_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                phone=form.cleaned_data['phone']
            )
            messages.success(request, 'پیام شما با موفقیت ثبت شد.')
        else:
            messages.error(request, 'لطفاً اطلاعات را به‌درستی وارد کنید.')
    return redirect(request.META.get('HTTP_REFERER', '/'))