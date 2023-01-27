from django.urls import path
from . import views

urlpatterns=[
    path("",views.OrderListView.as_view()),
    path("/<int:pk>",views.OrderDetailView.as_view()),
    path("/<int:pk>/comment",views.CommentListView.as_view()),
    path("/comment",views.CommentCreateView.as_view()),
    path("/comment/<int:pk>",views.CommentDetailView.as_view()),
    path("/comment/like",views.LikeCreateView.as_view()),
]
