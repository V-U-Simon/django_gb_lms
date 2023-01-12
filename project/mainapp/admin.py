from django.contrib import admin

from .models import Courses, CourseTeachers, Lesson, News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    pass


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass


@admin.register(CourseTeachers)
class CourseTeachersAdmin(admin.ModelAdmin):
    pass
