from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand

BASE_DIR = settings.BASE_DIR
FIXTURES_DIR = BASE_DIR / "fixtures"


class Command(BaseCommand):
    help = "Creates fixtures for articles and users."

    def handle(self, *args, **options):
        if not FIXTURES_DIR.exists():
            FIXTURES_DIR.mkdir(parents=True)
        apps = ["auth", "articles"]
        for app in apps:
            output_path = FIXTURES_DIR / f"{app}.json"
            relative_path = output_path.relative_to(BASE_DIR)
            with open(output_path, "w") as f:
                self.stdout.write(self.style.WARNING(f"Backing up app: {app}..."))
                management.call_command(
                    "dumpdata",
                    "auth.User",
                    "articles",
                    stdout=f,
                    verbosity=1,
                )
            if output_path.exists():
                self.stdout.write(self.style.SUCCESS(f"{relative_path} is updated.\n"))
