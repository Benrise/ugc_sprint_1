from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.auth_request import AuthRequest
from dependencies.jwt import JWTBearer


async def get_current_user_global(
        request: AuthRequest,
        user: AsyncSession = Depends(JWTBearer())):
    request.custom_user = user
