from django.contrib import admin
from .models import Challenge, ChallengeAttempts, ScoringRules


admin.site.register(Challenge)
admin.site.register(ChallengeAttempts)
admin.site.register(ScoringRules)
