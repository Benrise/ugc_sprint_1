from fastapi import Depends, Request
from fastapi.security import HTTPBearer

from async_fastapi_jwt_auth import AuthJWT
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.user import UserInDBRole
from db.postgres import get_session
from services.user import UserService, get_user_service


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(
            self,
            request: Request,
            user_service: UserService = Depends(get_user_service),
            db: AsyncSession = Depends(get_session)) -> UserInDBRole | None:
        authorize = AuthJWT(req=request)
        await authorize.jwt_optional()
        user_id = await authorize.get_jwt_subject()
        if not user_id:
            return None
        user = await user_service.get_user(db, authorize)
        return UserInDBRole.from_orm(user)
