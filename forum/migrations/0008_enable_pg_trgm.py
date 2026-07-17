from django.contrib.postgres.operations import TrigramExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("forum", "0007_remove_reply_upvotes_remove_thread_upvotes_and_more"),
    ]

    operations = [
        TrigramExtension(),
    ]
