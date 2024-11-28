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
from dependencies.kafka import get_kafka_service
from brokers.kafka import KafkaAdapter


router = APIRouter()


@router.post("/send_to_broker/{event_type}")
async def send_to_broker(
    event_type: str,
    request: Request,
    event_data: Optional[dict] = None,
    user_service: UserService = Depends(get_user_service),
    kafka_service: KafkaAdapter = Depends(get_kafka_service)
):
    token = request.cookies.get("access_token_cookie")
    if not token:
        raise HTTPException(status_code=401, detail="Токен отсутствует")

    data = await request.json()
    if not data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Data is required")

    data["date_event"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    user_id = await user_service.get_user_id(token)

    topic = f"{event_type}-events"

    await kafka_service.produce(topic=topic, key=event_type, value=str(data))
    return {
        'detail': 'Event successfully sent to broker',
        'data': data,
        'user_id': user_id,
        'event_type': event_type,
        'topic': topic
    }