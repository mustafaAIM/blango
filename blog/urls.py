# other imports
import blog.views
from django.urls import path
urlpatterns = [
    # other patterns
    path("", blog.views.index)
]