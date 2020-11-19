import uuid
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse
from django.db import models
from django.core.mail import send_mail
from core import managers as core_managers


class User(AbstractUser):

    """ Custom User Model """

    avatar = models.ImageField(
        blank=True,
        upload_to="avatars",
        null=True,
    )
    bio = models.CharField(max_length=40, default="", blank=True)

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
    email_secret = models.CharField(max_length=20, default="", blank=True)

    # objects = core_managers.CustomModelManager()

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})

    def verify_email(self):

        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            send_mail(
                "Verify CodeCulum Account",
                f'To verify your account, click <a href="http://127.0.0.1:8000/users/verify/{secret}">here</a>',
                settings.EMAIL_FROM,
                [self.email],
                fail_silently=False,
            )
        return

    # def __str__(self):
    #     return self.username

    # def get_absolute_url(self):
    #     return reverse("curriculums:detail", kwargs={"pk": self.pk})
