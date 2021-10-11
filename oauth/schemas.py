from typing import Optional

from pydantic import AnyHttpUrl, BaseModel, EmailStr

from .enums import SocialTypes


class OAuthRedirectLink(BaseModel):

    url: AnyHttpUrl


class OAuthCodeResponseSchema(BaseModel):
    code: str


class OAuthTokenResponseSchema(BaseModel):
    token: str


class OAuthUserDataResponseSchema(BaseModel):
    """Common interface for integration with external services via OAuth."""

    external_id: str
    email: EmailStr
    social_type: SocialTypes
    img: Optional[AnyHttpUrl]
    firstname: Optional[str]
    lastname: Optional[str]
