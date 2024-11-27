from fastapi import APIRouter, Request, Depends, HTTPException
from services.user import UserService
from dependencies.user import get_user_service

router = APIRouter()


@router.get("/send_message")
async def send_message(request: Request, user_service: UserService = Depends(get_user_service)):
    token = request.cookies.get("access_token_cookie")

    if not token:
        raise HTTPException(status_code=401, detail="Токен отсутствует")

    user_id = await user_service.get_user_id(token)
    return {"message": f"Сообщение отправлено пользователю {user_id}"}