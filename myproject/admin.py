from django.contrib import admin
# Nhập 7 lớp cần thiết (Course, Lesson, Question, Choice, Enrollment, Submission, và các lớp admin)
from .models import Course, Lesson, Question, Choice, Enrollment, Submission

# 1. Triển khai ChoiceInline để quản lý các lựa chọn ngay trong câu hỏi
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4  # Hiển thị sẵn 4 ô nhập lựa chọn

# 2. Triển khai QuestionInline để quản lý câu hỏi ngay trong bài học hoặc khóa học
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 5

# 3. Triển khai LessonInline (Tùy chọn thêm để quản lý bài học trong khóa học)
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

# 4. Triển khai QuestionAdmin để hiển thị ChoiceInline
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text', 'course']
    list_filter = ['course']

# 5. Triển khai LessonAdmin
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'course']

# 6. Triển khai CourseAdmin để hiển thị LessonInline và QuestionInline
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date')
    search_fields = ['name']

# Đăng ký các lớp với trang Admin
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Enrollment)
admin.site.register(Submission)
