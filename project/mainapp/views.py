from django.views.generic import DetailView, TemplateView

from .models import News


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["news_qs"] = News.objects.all()[:5]
        return context


class NewsPageDetailView(DetailView):
    template_name = "mainapp/news_detail.html"
    model = News
    context_object_name = "news_object"


class NewsWithPaginatorView(NewsPageView):
    def get_context_data(self, page, **kwargs):
        context = super().get_context_data(page=page, **kwargs)
        context["page_num"] = page
        context["page_total"] = 3
        context["previous"] = page - 1 if page else None
        context["next"] = page = page + 1 if page < context["page_total"] else None
        return context


class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"
