from datetime import datetime
from typing import Optional

from fastapi import (
    APIRouter,
    Request,
    Depends,
    HTTPException,
    status,
)

from services.user import UserService
from dependencies.user import get_user_service
from utils.query_params import extract_query_params


router = APIRouter()


@router.get("/send_to_broker/{event_type}")
async def send_to_broker(
            event_type: str,
            request: Request,
            event_params: Optional[str] = None,
            user_service: UserService = Depends(get_user_service)
        ):
    token = request.cookies.get("access_token_cookie")
    if not token:
        raise HTTPException(status_code=401, detail="Токен отсутствует")

    data = extract_query_params(request, event_params)
    if not data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Data is required")

    data["date_event"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    user_id = await user_service.get_user_id(token)

    try:
        return {
            'detail': 'Event successfully sent to broker',
            'data': data,
            'user_id': user_id,
            'event_type': event_type
        }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
