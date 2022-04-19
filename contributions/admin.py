from django.contrib import admin
from contributions.models import Contribution

@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):
    list_display= ["id","contributor","room","body"]
    list_filter= ["contributor","room"]