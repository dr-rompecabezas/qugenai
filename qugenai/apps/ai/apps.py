import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AIConfig(AppConfig):
    name = "qugenai.apps.ai"
    verbose_name = _("AI")

    def ready(self):
        with contextlib.suppress(ImportError):
            import qugenai.apps.ai.signals  # noqa: F401
