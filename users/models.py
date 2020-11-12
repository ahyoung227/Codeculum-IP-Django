import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """ Custom User Model """

    avatar = models.ImageField(blank=True, upload_to="avatars", null=True)

    my_curriculums = models.ManyToManyField(
        "curriculums.Curriculum", related_name="myC", blank=True
    )
    subscribed_curriculum = models.ManyToManyField(
        "curriculums.Curriculum", related_name="subscribedC", blank=True
    )
    saved_curriculum_titles = models.ManyToManyField(
        "curriculums.Curriculum", related_name="savedC", blank=True
    )
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=120, default="", blank="")

    def verify_email(self):
        if self.email_email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            pass
        return

    # def __str__(self):
    #     return self.username

    # def get_absolute_url(self):
    #     return reverse("curriculums:detail", kwargs={"pk": self.pk})
