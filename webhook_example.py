from fastapi import APIRouter, status
from fastapi.responses import RedirectResponse

from oauth.facebook import facebook_oauth
from oauth.google import google_oauth

router = APIRouter(prefix='/webhooks', tags=['Webhooks'])


@router.get(
    "/google/oauth",
    status_code=status.HTTP_307_TEMPORARY_REDIRECT,
)
async def google_oauth_webhook(code: str) -> RedirectResponse:
    token = await google_oauth.get_token(code)
    user_data = await google_oauth.get_user_data(token)

    # Business logic ....

    return RedirectResponse(url='/')


@router.get(
    "/facebook/oauth",
    status_code=status.HTTP_307_TEMPORARY_REDIRECT,
)
async def facebook_oauth_webhook(code: str) -> RedirectResponse:
    token = await facebook_oauth.get_token(code)
    user_data = await facebook_oauth.get_user_data(token)

    # Business logic ....

    return RedirectResponse(url='/')
