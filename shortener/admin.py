from django.contrib import admin
from .models import ClickAnalytics, ShortURL

@admin.register(ShortURL)
class ShortURLAdmin(admin.ModelAdmin):
    list_display = (
        "short_code",
        "original_url",
        "clicks_count",
        "is_active",
        "created_at",
    )
    list_filter = ("is_active", "created_at")
    search_fields = ("short_code", "original_url")
    readonly_fields = ("short_code", "created_at", "clicks_count")
    ordering = ("-created_at",)
    list_per_page = 25

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


@admin.register(ClickAnalytics)
class ClickAnalyticsAdmin(admin.ModelAdmin):
    list_display = (
        "short_url",
        "clicked_at",
        "ip_address",
        "referrer",
    )
    list_filter = ("clicked_at",)
    search_fields = (
        "short_url__short_code",
        "short_url__original_url",
        "ip_address",
        "user_agent",
        "referrer",
    )
    readonly_fields = (
        "short_url",
        "clicked_at",
        "ip_address",
        "user_agent",
        "referrer",
    )
    ordering = ("-clicked_at",)
    list_per_page = 50

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
