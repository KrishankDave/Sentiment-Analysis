from django.db import models
from django.contrib.auth.models import User


class UserActivity(models.Model):
    """
    Model to track user sentiment analysis activity.
    Stores each analysis request with user info, input text, result, and timestamp.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    text_input = models.TextField(help_text="The text submitted for sentiment analysis")
    sentiment_result = models.CharField(
        max_length=20,
        choices=[
            ('Positive', 'Positive'),
            ('Negative', 'Negative'),
            ('Neutral', 'Neutral'),
        ],
        help_text="The sentiment analysis result"
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "User Activity"
        verbose_name_plural = "User Activities"
        ordering = ['-timestamp']  # Most recent first

    def __str__(self):
        return f"{self.user.username} - {self.sentiment_result} - {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

    def get_short_text(self):
        """Return first 50 characters of text input"""
        return self.text_input[:50] + '...' if len(self.text_input) > 50 else self.text_input
