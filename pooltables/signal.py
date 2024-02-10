from django.db.models.signals import post_save #Import a post_save signal when a user is created
from pooltables.models.customer import CustomUser
from django.dispatch import receiver # Import the receiver
from django.contrib.auth import get_user_model
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.signals import social_account_added


@receiver(social_account_added)
def handle_social_account_added(sender, request, sociallogin, **kwargs):
    user = sociallogin.user
    # Add any additional logic to link the social account to your custom user model
    # For example, you might want to update custom fields based on the social account
    user.custom_field = sociallogin.account.extra_data.get('custom_field')
    user.save()
