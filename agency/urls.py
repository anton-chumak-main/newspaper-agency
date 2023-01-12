from django.urls import path

from agency.views import (
    index,
    TopicListView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView,
    NewspaperListView,
    NewspapersDetailView,
    RedactorListView,
    RedactorDetailView,
    RedactorCreateView,

)


urlpatterns = [
    path("", index, name="index"),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("topics/create/", TopicCreateView.as_view(), name="topic-create"),
    path(
        "topics/<int:pk>/update",
        TopicUpdateView.as_view(),
        name="topic-update"
    ),
    path(
        "topics/<int:pk>/delete",
        TopicDeleteView.as_view(),
        name="topic-delete"
    ),
    path("newspapers/", NewspaperListView.as_view(), name="newspaper-list"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path(
        "newspapers/<int:pk>",
        NewspapersDetailView.as_view(),
        name="newspaper-detail"
    ),
    path(
        "redactors/<int:pk>",
        RedactorDetailView.as_view(),
        name="redactor-detail"
    ),
    path(
        "redactors/create/",
        RedactorCreateView.as_view(),
        name="redactor-create"
    ),


]

app_name = "agency"
