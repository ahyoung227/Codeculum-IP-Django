import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from curriculums import models as curriculum_models
from users import models as user_models


class Command(BaseCommand):

    help = "This command creates users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many curriculums do you want to create",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()

        seeder.add_entity(
            curriculum_models.Curriculum,
            number,
            {
                "title": lambda x: seeder.faker.job(),
                "owner": lambda x: random.choice(all_users),
                "budget": lambda x: random.randint(0, 100),
                "period": lambda x: random.randint(0, 100),
            },
        )
        created_photo = seeder.execute()
        created_clean = flatten(list(created_photo.values()))
        skills = curriculum_models.Skill.objects.all()
        for pk in created_clean:
            curriculum = curriculum_models.Curriculum.objects.get(pk=pk)
            curriculum_models.Photo.objects.create(
                caption=seeder.faker.sentence(),
                file=f"curriculum_photos/{random.randint(0, 27)}.jpeg",
                curriculum=curriculum,
            )
            for s in skills:
                magic_number = random.randint(0, 14)
                if magic_number % 2 == 0:
                    curriculum.related_skill.add(s)

        # created_lists = seeder.execute()
        # created_clean = flatten(list(created_lists.values()))
        # skills = curriculum_models.Skill.objects.all()
        # for c in created_clean:
        # slist = curriculum_models.Curriculum.objects.get(pk=c)
        # for s in skills:
        #     magic_number = random.randint(0, 15)
        #     if magic_number % 2 == 0:
        #         slist.related_skill.add(s)

        self.stdout.write(self.style.SUCCESS(f"{number} curriculums are created"))
