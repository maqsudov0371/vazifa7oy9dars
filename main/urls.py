from django.urls import path
from .views import (HomePageView, RegisterView, LoginView, CourseDetailView,
                    AddCourseView, UpdateCourseView, ServiceView, ServiceDetailView)

app_name = 'main'

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('register', RegisterView.as_view(), name="register"),
    path('login', LoginView.as_view(), name="kirish"),
    path('course/<str:slug>', CourseDetailView.as_view(), name="detail"),
    path('add_course', AddCourseView.as_view(), name="add_course"),
    path('course/<int:pk>/edit', UpdateCourseView.as_view(), name="update_course"),
    path('service/', ServiceView.as_view(), name="services"),
    path('service_detail/<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),

]
