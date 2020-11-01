from django.urls import path, include

urlpatterns = [
    # path('callback/', include('app.urls')),
    path('callback', CallbackView.as_view(), name='callback_view'),
]

# urlpatterns += static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)
