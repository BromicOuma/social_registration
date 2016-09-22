from django.conf import settings
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class MyAccountAdapter(DefaultSocialAccountAdapter):

    def save_user(self, request, sociallogin, form=None):
        """
        Saves a newly signed up social login. In case of auto-signup,
        the signup form is not available.
        """
        # u = sociallogin.user
        # u.set_unusable_password()
        # if form:
        #     get_account_adapter().save_user(request, u, form)
        # else:
        #     get_account_adapter().populate_username(request, u)
        # sociallogin.save(request)
        # return u

