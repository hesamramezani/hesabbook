from django.contrib import admin
from .models import Expend , Income

# admin.site.register(Expend)
# admin.site.register(Income)


@admin.register(Expend)
class ExpendAdmin(admin.ModelAdmin):
    search_fields = ("text",)
    list_filter = ("user",)


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    search_fields = ("text",)
    list_filter = ("user",)

