from pydantic import BaseSettings


class FacebookConfig(BaseSettings):

    FACEBOOK_CLIENT_ID: str
    FACEBOOK_SECRET_KEY: str
    FACEBOOK_WEBHOOK_OAUTH_REDIRECT_URI: str


class GoogleConfig(BaseSettings):

    GOOGLE_CLIENT_ID: str
    GOOGLE_SECRET_KEY: str
    GOOGLE_WEBHOOK_OAUTH_REDIRECT_URI: str


class OAuthConfig(FacebookConfig, GoogleConfig):

    class Config:
        env_file = ".env"


oauth_config = OAuthConfig()
