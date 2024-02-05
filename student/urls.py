# from django.urls import path
# from . import views


# urlpatterns = [
#     path('std/', views.std, name="std"),
#     path('edit', views.edit, name="edit"),
#     path('view', views.view, name="view")

# ]

# from django.urls import path, include
# from . import views
# from .views import StudentViewSet
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'student', StudentViewSet, basename='student')

# urlpatterns = [
#     path('api/', include(router.urls)),
# ]

from django.urls import path
from .views import StudentListCreate, StudentRetrieveUpdateDelete

urlpatterns = [
    path('student', StudentListCreate.as_view(), name="Create-User-List"),
    path('student/<int:pk>/',
         StudentRetrieveUpdateDelete.as_view(), name='user-Details')
]
