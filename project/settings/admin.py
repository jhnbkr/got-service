from project.settings.environment import ENV

# Admin
# https://docs.djangoproject.com/en/4.0/ref/contrib/admin/

ADMIN_ENABLED = ENV.bool("ADMIN_ENABLED", default=True)

# Ace
# https://ace.c9.io/
ADMIN_ACE_THEME = ENV.str("ADMIN_ACE_THEME", default="chrome")
