import debug_toolbar
from django.urls import include, path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path('comment/<int:pk>/', views.CreateComment.as_view(), name='create_comment'),
    path('<slug:slug>/<slug:post_slug>', views.PostDetailView.as_view(), name='post_single'),
    path('<slug:slug>/', views.PostListView.as_view(), name='post_list'),
    path('', views.HomeView.as_view(), name='home'),
    # path('', cache_page(60 * 15)(views.HomeView.as_view()), name='home'),
    path('__debug__/', include(debug_toolbar.urls)),
]
