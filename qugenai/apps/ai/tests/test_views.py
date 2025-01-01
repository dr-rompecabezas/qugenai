import json
import re
from unittest.mock import MagicMock
from unittest.mock import patch

import pytest
from django.urls import reverse

from qugenai.apps.ai.forms import QGenForm

pytestmark = pytest.mark.django_db

HTTP_STATUS_OK = 200
HTTP_STATUS_BAD_REQUEST = 400
HTTP_STATUS_FOUND = 302


class TestGenerateExamQuestionsView:
    def test_generate_exam_questions_get(self, client, user):
        client.force_login(user)
        response = client.get(reverse("ai:generate_exam_questions"))
        assert response.status_code == HTTP_STATUS_OK
        context = response.context
        assert "form" in context
        assert isinstance(context["form"], QGenForm)
        assert context["exam_questions"] is None

    @patch("qugenai.apps.ai.views.client.chat.completions.create")
    def test_generate_exam_questions_post_valid_form(self, mock_create, client, user):
        client.force_login(user)
        mock_response = MagicMock()
        mock_response.choices = [
            MagicMock(message=MagicMock(content="Question 1\nQuestion 2\nQuestion 3")),
        ]
        mock_create.return_value = mock_response
        data = {"subject": "AI"}
        response = client.post(reverse("ai:generate_exam_questions"), data)
        assert response.status_code == HTTP_STATUS_OK
        context = response.context
        assert "form" in context
        assert isinstance(context["form"], QGenForm)
        assert context["exam_questions"] == ["Question 1", "Question 2", "Question 3"]

    def test_generate_exam_questions_post_invalid_form(self, client, user):
        client.force_login(user)
        data = {"subject": ""}
        response = client.post(reverse("ai:generate_exam_questions"), data)
        assert response.status_code == HTTP_STATUS_BAD_REQUEST
        assert json.loads(response.content) == {"error": "Invalid form data"}

    def test_generate_exam_questions_post_not_logged_in(self, client):
        response = client.post(reverse("ai:generate_exam_questions"))
        assert response.status_code == HTTP_STATUS_FOUND
        assert re.match(r"^/accounts/login/\?next=", response.url)
