from django.urls import path
from .views import CallbackView

urlpatterns = [
    path('callback', CallbackView.as_view(), name='callback_view'),
]

# urlpatterns += static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)
