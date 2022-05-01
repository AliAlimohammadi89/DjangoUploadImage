from django.urls import path
from .views import image_upload_view
from django.conf import settings
from django.conf.urls.static import static
static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)


urlpatterns = [
    # path('', picView,name= 'picView'),
    # path('picupload', picUploadView,name= 'picUploadView'),
    path('', image_upload_view),
    # path('', image_upload_view)

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)