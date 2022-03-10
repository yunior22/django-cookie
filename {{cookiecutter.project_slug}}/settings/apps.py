#   REGISTER VENDOR AND LOCAL APPS
# ------------------------------------------------------------------------------
VENDOR_APPS = [
    'djangomix',
    # Third party apps go here.
]
LOCAL_APPS = [
    {%- if cookiecutter.use_vuejs == "y" %}
    'apps.client',
    {%- endif %}
    'apps.core',
    # 'apps.users',
    # Your apps: custom apps go here.
]

VENDOR_LOCAL_APPS = VENDOR_APPS + LOCAL_APPS
