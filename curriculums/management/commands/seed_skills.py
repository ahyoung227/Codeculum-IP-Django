from django.core.management.base import BaseCommand
from curriculums.models import Skill


class Command(BaseCommand):

    help = "This command sets skillsets"

    def add_arguments(self, parser):
        parser.add_argument(
            "--times", help="How many times do you want to create skills"
        )

    def handle(self, *args, **options):
        skills = [
            "Web Development",
            "JavaScript",
            "React",
            "Angular",
            "CSS",
            "PHP",
            "Node.Js",
            "Python",
            "Vue JS",
            "WordPress",
            "Django",
            "MERN Stack",
            "Redux Framework",
            "HTML5",
            "Typescript",
            "ASP.NET Core",
            "Laravel",
            "Microservices",
        ]
        for s in skills:
            Skill.objects.create(title=s)
        self.stdout.write(self.style.SUCCESS("Skills are created!"))
