from django.contrib import admin

# Register your models here.
# sticky_memo/memo/admin.py

from memo.models import Memo

@admin.register(Memo)
class MemoAdmin(admin.ModelAdmin):
    list_display = ['title']