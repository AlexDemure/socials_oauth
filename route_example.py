from fastapi import APIRouter, status

from oauth.facebook import facebook_oauth
from oauth.google import google_oauth
from oauth.schemas import OAuthRedirectLink

router = APIRouter(prefix='/oauth', tags=['OAuth'])


@router.get(
    "/google/login",
    status_code=status.HTTP_200_OK,
    response_model=OAuthRedirectLink
)
def google_oauth_login_request() -> OAuthRedirectLink:
    return google_oauth.generate_link_for_code()


@router.get(
    "/facebook/login",
    status_code=status.HTTP_200_OK,
    response_model=OAuthRedirectLink
)
def facebook_oauth_login_request() -> OAuthRedirectLink:
    return facebook_oauth.generate_link_for_code()
