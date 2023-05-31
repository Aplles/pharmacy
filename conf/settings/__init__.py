from split_settings.tools import include

settings = [
    "django.py",  # standard django settings
    "database.py",  # postgres
]

# Include settings:
include(*settings)
