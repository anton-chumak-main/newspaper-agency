from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from agency.models import Redactor, Newspaper, Topic


@login_required
def index(request):
    """View function for the home page of the site."""

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_publishers": Redactor.objects.count(),
        "num_newspapers": Newspaper.objects.count(),
        "num_topics": Topic.objects.count(),
        "num_visits": num_visits + 1,
        }

    return render(request, "agency/index.html", context=context)
