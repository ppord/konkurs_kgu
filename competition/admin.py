from django.contrib import admin
from competition.models import TextIdea, Author

@admin.register(TextIdea)
class TextIdeaAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

# Register your models here.
