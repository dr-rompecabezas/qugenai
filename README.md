# QuGenAI

QuGenAI is an AI-powered exam content generator designed to help educators, certification providers, and trainers create high-quality, data-driven assessments in minutes. Built for flexibility and scalability, QuGenAI streamlines exam development workflows, ensuring efficiency, accuracy, and reliability.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![codecov](https://codecov.io/gh/think-elearn/qugenai/graph/badge.svg?token=VoioOTaqbj)](https://codecov.io/gh/think-elearn/qugenai)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## Target Audience

- Certification Providers – Streamline exam development and updates.
- Educators – Build assessments aligned with learning objectives and curricula.
- Corporate Trainers – Develop competency-based training assessments.

## Key Features

1. AI-Generated Questions
    - Automatically generate exam questions from structured and unstructured content.
    - Customize outputs by topic, difficulty level, and question format.

2. Source Content Input
    - Upload source material in various formats, including PDFs, Word documents, text files, PowerPoint presentations, Excel spreadsheets, CSV files, and web links.

3. Fine-Tuning
    - Train the AI model using user-specific content to match organizational needs.
    - Leverage historical performance data to optimize outputs.

4. Multilingual Support
    - Provide seamless experiences in English, French, and Spanish.
    - Plan for scalability to additional languages.

5. Export Options
    - Export generated content to multiple formats (PDF, Word, and PowerPoint).

6. Robust API
    - Integrate with external tools and platforms for expanded workflows.

7. SaaS Model
    - Built as a Software-as-a-Service (SaaS) application with multitenancy support for scalability.

## AI Workflow

1. Input Source Content – Upload guidelines, topic details, and example materials.
2. Generate Questions – Use AI to create drafts with custom parameters.
3. Review and Refine – Adjust outputs through human review and expert input.
4. Export and Integrate – Finalize questions and export to multiple formats or integrate with external platforms.

## Technical Architecture Overview

QuGenAI is a Django-based SaaS application designed to streamline the creation of exam content using AI. It supports fine-tuning, retrieval-augmented generation (RAG) pipelines, and question validation workflows to assist exam creators and educators in generating high-quality, multilingual exam questions.

### Core Technologies

- **Backend Framework**:
  - **Django** – Handles user management, database interactions, admin interfaces, and multitenancy.

- **Database**:
  - **PostgreSQL** – Scalable relational database with JSONB support for flexible data storage.

- **AI Integration**:
  - **OpenAI API** or **Hugging Face Models** – Supports fine-tuning and retrieval-augmented generation (RAG).

- **Task Queue**:
  - **Celery with Redis** – Handles background tasks, such as AI processing and report generation.

- **File Storage**:
  - **Amazon S3** – Stores uploaded source content files (PDFs, Word, etc.).
  - **Django Storages** – Integrates S3 seamlessly with Django.

- **Email Services**:
  - **Mailgun** – Handles transactional emails with developer-friendly tools.

- **Multilingual Support (Planned)**:
  - **django-parler** or **modeltranslation** – For managing multilingual content.

### Architecture Diagram

```text
 User → Django Frontend (Admin + UI) → Django Backend (ORM + Views)
                                   ↓
                      Celery Task Queue (Background Tasks)
                                   ↓
                         AI Models (OpenAI, Hugging Face)
                                   ↓
                             File Storage (S3)
```

### Workflow Overview

1. **Source Content Upload**
   - Users upload PDFs, Word files, and CSVs via Django’s admin or web UI.

2. **AI Processing**
   - Content is processed using AI models (fine-tuning and RAG pipelines).
   - Tasks run asynchronously with Celery for scalability.

3. **Storage and Review**
   - AI-generated questions are stored in PostgreSQL and reviewed via Django’s UI.

4. **Export Options**
   - Users can export questions to multiple formats (Word, PDF, PPT).

### Security

- **Authentication**:
  - Django Allauth for secure user authentication with email confirmation.

- **Authorization**:
  - Role-based access control for Admins, Content Creators, and Reviewers.

- **Data Encryption**:
  - Encrypted file storage and SSL/TLS for secure communication.

## Technical Roadmap

### Deployment Strategy

#### Current Setup

- Django is deployed as a Heroku app for simplicity and cost efficiency.
- Celery handles background processing tasks for AI pipelines.
- This setup prioritizes rapid development and proof-of-concept validation.

#### Future Plans

- **Microservices Transition**:
  - Introduce an optional FastAPI service for AI workflows when scaling demands increase.
  - Use API gateways or reverse proxies for seamless routing between services.

- **Kubernetes Deployment**:
  - Deploy to AWS/GCP Kubernetes clusters for scalability and redundancy.

- **Internationalization**:
  - Add support for multilingual interfaces and localization.

#### Scaling Goals

- **Short-Term Goals**:
  - Optimize workflows within a unified app while maintaining low costs.

- **Long-Term Goals**:
  - Scale AI-specific processing independently.
  - Add API integrations for learning platforms.
  - Introduce multi-region deployments to support international users.

## Feature Development

1. **Multitenancy Design** – Build for scalability while keeping the initial implementation simple for a single developer.
2. **AI Fine-Tuning Models** – Incorporate techniques like retrieval-augmented generation (RAG) and prompt engineering.
3. **Performance Monitoring** – Enable feedback loops to refine question quality over time.
4. **Integrations** – Expand API capabilities for external platform connections.
5. **Multilingual Features** – Implement language localization with fallback options.

## Settings

This project remains largely structured and completely configured per the default Cookiecutter-Django's template [settings](https://cookiecutter-django.readthedocs.io/en/latest/1-getting-started/settings.html).

### Email Server

In development, it is often nice to see emails sent from your application. For that reason, the local SMTP server [Mailpit](https://github.com/axllent/mailpit) with a web interface is available as a Docker container.

The mailpit container will start automatically when you run all Docker containers. Please check the [cookiecutter-django Docker documentation](https://cookiecutter-django.readthedocs.io/en/latest/2-local-development/developing-locally-docker.html) for more details on how to start all containers.

With Mailpit running, to view messages that are sent by your application, open your browser and go to `http://127.0.0.1:8025`

### Sentry

Sentry is an error logging aggregator service. Sign up for a free account at <https://sentry.io/signup/?code=cookiecutter> or download and host it yourself.
The system is set up with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN URL in production.

## Deployment

The following details how to deploy this application.

### Heroku

See detailed [cookiecutter-django Heroku documentation](https://cookiecutter-django.readthedocs.io/en/latest/3-deployment/deployment-on-heroku.html).

### Docker

See detailed [cookiecutter-django Docker documentation](https://cookiecutter-django.readthedocs.io/en/latest/3-deployment/deployment-with-docker.html).

## Contributing

We’re in the early planning stages and welcome feedback and ideas to improve QuGenAI’s capabilities. As the technical architecture solidifies, contributions will be open.

## License

QuGenAI is released under the **Functional Source License (FSL)** for the first two years. After this period, it transitions to the **MIT License**.

For more details, see [LICENSE](LICENSE.md) or visit [fsl.software](https://fsl.software/) for an overview of the FSL terms.
