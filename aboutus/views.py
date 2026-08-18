from django.views.generic import TemplateView
from .models import AboutUs, FunFact, TeamMember, Testimonial,SiteBackground

class AboutUsView(TemplateView):
    template_name = "aboutus/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = AboutUs.objects.first()
        context['fun_facts'] = FunFact.objects.all()
        context['team_members'] = TeamMember.objects.all()
        context['testimonials'] = Testimonial.objects.all()
        context['bg_setting'] = SiteBackground.objects.first()
        return context