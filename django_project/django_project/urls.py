"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.conf import settings

#위에서부터 처리 순서임
urlpatterns = [
    path('blog/', include('blog.urls')),
    path('memo/', include('memo.urls')),
    path('admin/', admin.site.urls),
    path('markdownx/', include('markdownx.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('single_pages.urls')),

]

#장고 프로젝트 밖의 폴더에 접근하기 위해서 정적인 방식을 사용할 것이당
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)