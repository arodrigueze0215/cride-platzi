from django.contrib import admin

# Models
from cride.circles.models import Circle

@admin.register(Circle)
class CircleAdmin(admin.ModelAdmin):
    """ Admin Circle """
    list_display = ('slug_name', 'name', 'is_public', 'verified', 'is_limited', 'member_list')
