from django.urls import path

from agency.views import (
    index,
    TopicListView,
    NewspaperListView,
    RedactorListView,
    NewspapersDetailView,

)


urlpatterns = [
    path("", index, name="index"),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("newspapers/", NewspaperListView.as_view(), name="newspaper-list"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path(
        "newspapers/<int:pk>",
        NewspapersDetailView.as_view(),
        name="newspaper-detail"
    ),

]

app_name = "agency"
