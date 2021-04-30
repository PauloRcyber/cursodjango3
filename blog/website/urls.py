from django.urls import path, include
from .views import hello_blog


# urlpatterns = [
#     path('', hello_blog),
# ]


urlpatterns = [
    path('', hello_blog),
]


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('hello/', hello_world),
#     path('blog/', include('website.urls')),
# ]