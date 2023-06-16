# Generated by Django 2.2.24 on 2023-06-14 07:21

from django.db import migrations


def set_owners(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    Flat = apps.get_model('property', 'Flat')

    for flat in Flat.objects.all().iterator():
        Owner.objects.get_or_create(
            full_name=flat.owner,
            phone_number=flat.owners_phonenumber,
            defaults={'pure_phone': flat.owner_pure_phone}
            )


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_owner'),
    ]

    operations = [
    migrations.RunPython(set_owners),
    ]
