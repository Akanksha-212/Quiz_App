from django.core.management.base import BaseCommand

from core.models import Category, Quiz, Question, Option

from core.random_ai import generate_questions

import random


class Command(BaseCommand):

    help = "Generate Quiz Questions"


    def add_arguments(self, parser):

        parser.add_argument("topic", type=str)


    def handle(self, *args, **kwargs):

        topic = kwargs["topic"]

        questions = generate_questions(topic)

        if not questions:

            self.stdout.write(
                self.style.ERROR("No questions found!")
            )
            return


        category, _ = Category.objects.get_or_create(
            name=topic
        )

        quiz, _ = Quiz.objects.get_or_create(
            title=f"{topic} Quiz",
            category=category
        )


        for q in questions:

            question = Question.objects.create(
                quiz=quiz,
                text=q["question"]
            )

            options = q["wrong"] + [q["correct"]]

            random.shuffle(options)

            for option in options:

                Option.objects.create(
                    question=question,
                    text=option,
                    is_correct=(option == q["correct"])
                )

        self.stdout.write(
            self.style.SUCCESS(
                f"{topic} Quiz Generated!"
            )
        )