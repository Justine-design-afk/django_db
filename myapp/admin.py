from django.contrib import admin

from myapp.models import Book

# Register your models here.
admin.site.site_title="Bookshop"
admin.site.site_header="Bookshop Admin"
admin.site.index_title="Books Management system"

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=("title","isbn","year","cost")
    search_fields = ("title","isbn","year","cost")
    list_filter=("year","category")
    ordering=("-year",)
