from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from openai import OpenAI

from .forms import QGenForm

client = OpenAI(api_key=settings.OPENAI_API_KEY)


@login_required
def generate_exam_questions(request):
    exam_questions = None
    if request.method == "POST":
        form = QGenForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            system_prompt = """You are an exam question generator.
            You are tasked with creating multiple choice questions for an exam.
            The questions should be challenging but fair.
            There should be four answer choices for each question.
            There must be only one correct answer.
            Do not use "all of the above" or "none of the above" as answer choices.
            Include the rationale for the correct answer and the distractors.
            The subject is: """
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "developer", "content": system_prompt},
                    {"role": "user", "content": subject},
                ],
                temperature=0.8,
                max_tokens=1000,
            )
            exam_questions = response.choices[0].message.content.strip().split("\n")
        else:
            return JsonResponse({"error": "Invalid form data"}, status=400)
    else:
        form = QGenForm()

    return render(
        request,
        "ai/qgenform.html",
        {"form": form, "exam_questions": exam_questions},
    )
