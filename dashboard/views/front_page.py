from django.views.generic import TemplateView


class FrontPage(TemplateView):
    template_name = 'dashboard/front_page.html'


front_page = FrontPage.as_view()
