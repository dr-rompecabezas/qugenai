from django.urls import path

from .views import generate_exam_questions

app_name = "ai"
urlpatterns = [
    path(
        "q-gen/",
        view=generate_exam_questions,
        name="generate_exam_questions",
    ),
]
