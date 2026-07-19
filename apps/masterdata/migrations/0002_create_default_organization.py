from uuid import uuid4

from django.db import migrations


def create_default_organization(apps, schema_editor):
    Organization = apps.get_model("masterdata", "Organization")

    if not Organization.objects.exists():
        Organization.objects.create(
            public_id=uuid4(),
            name="New Organization",
        )


class Migration(migrations.Migration):

    dependencies = [
        ("masterdata", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(
            create_default_organization,
            # The Organization is part of the installation's
            # structural state and is therefore not removed on rollback.
            migrations.RunPython.noop,
        ),
    ]