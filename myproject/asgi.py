from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'onlinecourse'

urlpatterns = [
    # Các đường dẫn cơ bản đã có sẵn
    path(route='', view=views.CourseListView.as_view(), name='index'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course_details'),
    path('<int:course_id>/enroll/', views.enroll, name='enroll'),

    # --- NHIỆM VỤ 6: THÊM ĐƯỜNG DẪN CHO SUBMIT VÀ SHOW_EXAM_RESULT ---
    
    # 1. Đường dẫn để xử lý việc nộp bài thi (POST request từ form)
    path('<int:course_id>/submit/', views.submit, name='submit'),
    
    # 2. Đường dẫn để hiển thị kết quả sau khi nộp bài
    path('submission/<int:submission_id>/show_result/', views.show_exam_result, name='show_exam_result'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
