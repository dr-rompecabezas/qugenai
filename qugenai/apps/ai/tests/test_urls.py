from django.urls import resolve
from django.urls import reverse

from qugenai.apps.ai.views import generate_exam_questions


def test_generate_exam_questions_url_resolves():
    url = reverse("ai:generate_exam_questions")
    assert resolve(url).func == generate_exam_questions
