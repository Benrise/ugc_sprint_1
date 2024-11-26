from fastapi import HTTPException
from http import HTTPStatus
from functools import wraps

from schemas.user import UserInDBRole, UserRoles


def roles_required(roles_list: list[UserRoles]):
    def decorator(fuction):
        @wraps(fuction)
        async def wrapper(*args, **kwargs):
            user: UserInDBRole = kwargs.get('request').custom_user
            if not user or user.role_id not in roles_list:
                raise HTTPException(
                    status_code=HTTPStatus.FORBIDDEN,
                    detail='Forbidden. Only authorized user have access'
                )
            return await fuction(*args, **kwargs)
        return wrapper
    return decorator
