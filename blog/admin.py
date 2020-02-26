from django.contrib import admin
from .models import Table
from .models import Table_cells

# TODO: удалить админки, которые не используются

admin.site.register(Table)
admin.site.register(Table_cells)
