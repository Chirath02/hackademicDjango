from django.db import models
from django.contrib.auth.models import User
from classes.models import Class


class Challenge(models.Model):
    title = models.CharField(max_length=300)
    pkg_name = models.CharField(max_length=100)
    description = models.TextField()
    authors = models.ManyToManyField(User, related_name="authors")
    category = models.CharField(max_length=200)
    date_posted = models.DateTimeField(auto_now=False, auto_now_add=True)
    visibility = models.CharField(default='private', max_length=100)
    is_published = models.BooleanField(default=0)
    abstract = models.CharField(max_length=500, default="")
    ordering = models.IntegerField(default=1)
    level = models.CharField(max_length=300, default="")
    duration = models.TimeField(blank=True, null=True, )
    goal = models.CharField(max_length=300, default="")
    solution = models.CharField(max_length=300, default="")
    availability = models.CharField(max_length=100, default='private')
    default_points = models.IntegerField()
    default_duration = models.TimeField(blank=True, null=True)

    image = models.ImageField(blank=True, null=True, upload_to='challenges/')

    def __str__(self):
        return self.title


class ChallengeAttempts(models.Model):
    user = models.ForeignKey(User, related_name="user")
    challenge = models.ForeignKey(Challenge, related_name="challanges")
    class_name = models.ForeignKey(Class, related_name="class_name")
    time = models.TimeField()
    status = models.IntegerField()
    count = models.IntegerField(default=1)

    def __str__(self):
        return self.user

class ScoringRules(models.Model):
    challenge = models.IntegerField(default=0)
    class_id = models.IntegerField(default=0)
    attempt_cap = models.IntegerField(default=0)
    attempt_cap_penalty = models.IntegerField(default=0)
    time_between_first_and_last_attempt = models.IntegerField(default=0)
    time_penalty = models.IntegerField(default=0)
    time_reset_limit_seconds = models.IntegerField(default=0)
    request_frequency_per_minute = models.IntegerField(default=0)
    request_frequency_penalty = models.IntegerField(default=0)
    experimentation_bonus = models.IntegerField(default=0)
    multiple_solution_bonus = models.IntegerField(default=0)
    banned_user_agents = models.TextField(default='')
    banned_user_agents_penalty = models.IntegerField(default=0)
    base_score = models.IntegerField(default=0)
    first_try_solves = models.IntegerField(default=0)
    penalty_for_many_first_try_solves = models.IntegerField(default=0)

    def __str__(self):
        return "Scoring rules for " + self.challenge



