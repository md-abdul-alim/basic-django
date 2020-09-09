from django.urls import path

from .views import (
    CourseView,
    CourseCreateView,
    CourseListView,
    CourseUpdateView,
    CourseDeleteView,
    # MyListView, #go to view and check note
)

app_name = 'mycourses'
urlpatterns = [
    path('create/', CourseCreateView.as_view(), name='mycourses-create'),
    # path('', MyListView.as_view(), name='courses-list'), ##go to view and check note
    path('', CourseListView.as_view(), name='courses-list'),
    path('<int:id>/', CourseView.as_view(), name='mycourses-detail'),
    path('update/<int:id>/', CourseUpdateView.as_view(), name='mycourses-update'),
    path('delete/<int:id>/', CourseDeleteView.as_view(), name='mycourses-delete'),
]
