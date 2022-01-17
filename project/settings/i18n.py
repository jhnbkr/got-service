from project.settings.environment import ENV

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = ENV.str("LANGUAGE_CODE", default="en")
TIME_ZONE = ENV.str("TIME_ZONE", default="UTC")
USE_I18N = True
USE_L10N = True
USE_TZ = True
