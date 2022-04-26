from django.contrib import admin
from django.apps import apps
from users.models import ExtendUser

admin.site.register(ExtendUser)


app = apps.get_app_config('graphql_auth')

for model_name, model in app.models.items():
    admin.site.register(model)
