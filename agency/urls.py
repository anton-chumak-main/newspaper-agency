from django.urls import path

from agency.views import (
    index,
    about,
    TopicListView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView,
    NewspaperListView,
    NewspapersDetailView,
    NewspapersCreateView,
    NewspapersUpdateView,
    NewspapersDeleteView,
    RedactorListView,
    RedactorDetailView,
    RedactorCreateView,
    RedactorUpdateView,
    RedactorDeleteView,
)


urlpatterns = [
    path("", index, name="index"),
    path("about", about, name="about"),
    path(
        "topics/",
        TopicListView.as_view(),
        name="topic-list"
    ),
    path(
        "topics/create/",
        TopicCreateView.as_view(),
        name="topic-create"
    ),
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
    path(
        "newspapers/",
        NewspaperListView.as_view(),
        name="newspaper-list"
    ),
    path(
        "newspapers/<int:pk>",
        NewspapersDetailView.as_view(),
        name="newspaper-detail"
    ),
    path(
        "newspapers/create",
        NewspapersCreateView.as_view(),
        name="newspaper-create"
    ),
    path(
        "newspapers/<int:pk>/update",
        NewspapersUpdateView.as_view(),
        name="newspaper-update"
    ),
    path(
        "newspapers/<int:pk>/delete",
        NewspapersDeleteView.as_view(),
        name="newspaper-delete"
    ),

    path(
        "redactors/",
        RedactorListView.as_view(),
        name="redactor-list"
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
    path(
        "redactors/<int:pk>/update",
        RedactorUpdateView.as_view(),
        name="redactor-update"
    ),
    path(
        "redactors/<int:pk>/delete",
        RedactorDeleteView.as_view(),
        name="redactor-delete"
    ),

]

app_name = "agency"
