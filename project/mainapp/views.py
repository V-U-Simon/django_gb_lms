from django.views.generic import DetailView, ListView, TemplateView

from .models import Courses, CourseTeachers, Lesson, News


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


class CoursesPageView(ListView):
    template_name = "mainapp/courses_list.html"
    model = Courses
    context_object_name = "objects"


class CoursePageDetailView(DetailView):
    template_name = "mainapp/Course_detail.html"
    model = Courses
    context_object_name = "course_object"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lessons"] = Lesson.objects.filter(course=context["course_object"])
        context["teachers"] = CourseTeachers.objects.filter(course=context["course_object"])
        return context


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"
