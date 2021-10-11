from httpx import AsyncClient

from .base import OAuthBase
from .enums import SocialTypes
from .schemas import OAuthUserDataResponseSchema, OAuthCodeResponseSchema, OAuthRedirectLink, OAuthTokenResponseSchema
from .settings import oauth_config


class FacebookOAuth(OAuthBase):
    """
    Config Facebook

    https://developers.facebook.com/docs/facebook-login/manually-build-a-login-flow?locale=ru_RU#exchangecode
    """

    scope = ["email", "public_profile"]

    user_fields = ["id", "first_name", "last_name", "email"]

    def prepare_user_data(self, external_id: str, user_data: dict) -> OAuthUserDataResponseSchema:
        """Converting interface socials for the general data format of the system"""

        return OAuthUserDataResponseSchema(
            external_id=external_id,
            email=user_data['email'],
            social_type=SocialTypes.facebook,
            firstname=user_data['first_name'],
            lastname=user_data['last_name']
        )

    def generate_link_for_code(self) -> OAuthRedirectLink:
        """
        Generating a link to a redirect to the service to receive a confirmation code.

        It is necessary for the user to further enter the service and receive a confirmation code from the service on Webhook.
        """

        url = f"https://www.facebook.com/v12.0/dialog/oauth?" \
              f"client_id={self.client_id}&" \
              f"redirect_uri={self.webhook_redirect_uri}&" \
              f"scope={self.scope_to_str(',')}&" \
              f"response_type={self.response_type}"

        return OAuthRedirectLink(url=url)

    async def get_token(self, code: OAuthCodeResponseSchema) -> OAuthTokenResponseSchema:
        """Exchange of a confirmation code for a user token."""

        async with self.session.get(
            'https://graph.facebook.com/v12.0/oauth/access_token',
            params=dict(
                code=code.code,
                client_id=self.client_id,
                client_secret=self.secret_key,
                redirect_uri=self.webhook_redirect_uri,
            )
        ) as response:
            token_data = await response.json()

        return OAuthTokenResponseSchema(token=token_data['access_token'])

    async def get_user_data(self, token: OAuthTokenResponseSchema) -> OAuthUserDataResponseSchema:
        """"Getting information about a user through an access token."""

        async with self.session.get(
            url="https://graph.facebook.com/me",
            params=dict(
                fields=",".join(self.user_fields),
                access_token=token.token
            )
        ) as response:
            user_data = await response.json()

        return self.prepare_user_data(user_data['id'], user_data)


facebook_oauth = FacebookOAuth(
    session=AsyncClient(),
    client_id=oauth_config.FACEBOOK_CLIENT_ID,
    secret_key=oauth_config.FACEBOOK_SECRET_KEY,
    webhook_redirect_uri=oauth_config.FACEBOOK_WEBHOOK_OAUTH_REDIRECT_URI
)
