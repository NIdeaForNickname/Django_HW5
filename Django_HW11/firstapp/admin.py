from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.utils.html import format_html
from django.apps import apps
from .models import Movie, Genre, Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "text_short", "date", "film")
    list_filter = ("date",)
    search_fields = ("name", "text", "film__title")

    def text_short(self, obj):
        return obj.text[:50] + "..." if len(obj.text) > 50 else obj.text
    text_short.short_description = "Review Text"

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return request.user.has_perm("firstapp.can_moderate_reviews")

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return request.user.has_perm("firstapp.can_moderate_reviews")

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return request.user.has_perm("firstapp.can_moderate_reviews")

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "country", "release", "rating", "review_count_display")
    search_fields = ("title", "description", "country")
    list_filter = ("release", "rating", "genre")
    ordering = ("title",)

    filter_horizontal = ("genre",)

    def review_count_display(self, obj):
        return obj.Review.count()
    review_count_display.short_description = "Review Count"

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_superuser

def create_moderators_group():
    Review = apps.get_model("firstapp", "Review")
    content_type = ContentType.objects.get_for_model(Review)

    group, created = Group.objects.get_or_create(name="Moderators")

    perm = Permission.objects.get(
        codename="can_moderate_reviews",
        content_type=content_type,
    )

    group.permissions.add(perm)

create_moderators_group()