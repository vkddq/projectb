from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import login_view, logout_view, dashboard

from branches.views import home_view, BranchViewSet
from academics.views import students_view, SubjectViewSet, StudentViewSet, GroupViewSet
from scheduling.views import schedule_view

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = DefaultRouter()
router.register(r'branches', BranchViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'students', StudentViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('academics/', students_view, name='academics'),
    path('schedule/', schedule_view, name='schedule'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]