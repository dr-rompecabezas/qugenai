import json
from unittest.mock import MagicMock, patch

import pytest
from django.test import Client
from django.urls import resolve, reverse

from app import generate_exam_questions


def test_generate_exam_questions_url_resolves():
    url = reverse("generate_exam_questions")
    # Compare with the view function's qualified name
    assert resolve(url).func.__name__ == generate_exam_questions.__name__


@pytest.fixture(scope="module", autouse=True)
def client():
    return Client()


HTTP_STATUS_OK = 200
HTTP_STATUS_BAD_REQUEST = 400
HTTP_STATUS_INTERNAL_SERVER_ERROR = 500


class TestGenerateExamQuestionsView:
    def test_generate_exam_questions_get(self, client):
        response = client.get(reverse("generate_exam_questions"))
        assert response.status_code == HTTP_STATUS_OK
        content = response.content.decode("utf-8")
        assert "subject" in content  # Check for the subject field in QGenForm

    def test_generate_exam_questions_post_invalid_form(self, client):
        data = {"subject": ""}
        response = client.post(reverse("generate_exam_questions"), data)
        assert response.status_code == HTTP_STATUS_BAD_REQUEST
        assert json.loads(response.content) == {"error": "Invalid form data"}

    @patch("app.client.beta.chat.completions.parse")
    def test_generate_exam_questions_api_refusal(self, mock_parse, client):
        mock_response = MagicMock()
        mock_response.choices = [
            MagicMock(message=MagicMock(refusal="Content violation")),
        ]
        mock_parse.return_value = mock_response

        data = {"subject": "Math"}
        response = client.post(reverse("generate_exam_questions"), data)
        assert response.status_code == HTTP_STATUS_BAD_REQUEST
        assert json.loads(response.content) == {"error": "Content violation"}

    @patch("app.client.beta.chat.completions.parse")
    def test_generate_exam_questions_valid_response(self, mock_parse, client):
        # Mocking the OpenAI response object structure
        mock_choice = MagicMock()
        mock_choice.message.content = json.dumps(
            {
                "subject": "Math",
                "questions": [
                    {
                        "question": "What is 2+2?",
                        "options": {"A": "3", "B": "4", "C": "5", "D": "6"},
                        "correct_option": "B",
                        "rationale": "2+2 equals 4.",
                        "tags": ["math", "addition"],
                    },
                ],
            },
        )
        mock_choice.message.refusal = None  # Ensure this is JSON-serializable
        mock_parse.return_value = MagicMock(choices=[mock_choice])

        # Sending a POST request with valid data
        data = {"subject": "Math"}
        response = client.post(reverse("generate_exam_questions"), data)

        # Asserting the response
        assert response.status_code == HTTP_STATUS_OK
        content = response.content.decode("utf-8")

        # Check that the response contains expected elements
        # These are strings we expect to find in the rendered HTML
        assert "Math" in content
        assert "What is 2+2?" in content
        assert "2+2 equals 4." in content

    @patch("app.client.beta.chat.completions.parse")
    def test_generate_exam_questions_parsing_error(self, mock_parse, client):
        # Mocking a response with invalid JSON content
        mock_choice = MagicMock()
        mock_choice.message.content = "invalid JSON"
        mock_choice.message.refusal = None  # Ensure this is JSON-serializable
        mock_parse.return_value = MagicMock(choices=[mock_choice])

        # Sending a POST request with valid data
        data = {"subject": "Math"}
        response = client.post(reverse("generate_exam_questions"), data)

        # Asserting the response
        assert response.status_code == HTTP_STATUS_INTERNAL_SERVER_ERROR
        assert json.loads(response.content) == {"error": "Failed to parse response"}
