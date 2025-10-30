from django.contrib import admin
from .models import UserActivity


@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for UserActivity model.
    Displays user activities with filters and search capabilities.
    """
    # Display these fields in the admin list view
    list_display = ('user', 'get_short_text', 'sentiment_result', 'timestamp')

    # Add filters in the right sidebar
    list_filter = ('sentiment_result', 'user', 'timestamp')

    # Add search functionality
    search_fields = ('user__username', 'text_input', 'sentiment_result')

    # Make fields read-only (prevent editing)
    readonly_fields = ('user', 'text_input', 'sentiment_result', 'timestamp')

    # Order by most recent first
    ordering = ('-timestamp',)

    # Number of items per page
    list_per_page = 25

    # Date hierarchy for easy navigation
    date_hierarchy = 'timestamp'

    def get_short_text(self, obj):
        """Display first 50 characters of text input"""
        return obj.get_short_text()
    get_short_text.short_description = 'Text Input (Preview)'

    # Disable add permission (activities are created automatically)
    def has_add_permission(self, request):
        return False

    # Disable change permission (activities should not be edited)
    def has_change_permission(self, request, obj=None):
        return False
