# handles incoming location updates at 1 Hz
from fastapi import APIRouter
from app.services import event_dispatcher
from app.storage import trip_store

router = APIRouter()

@router.post("/location")
def update_location(user_id: str, lat: float, lng: float):
    trip = trip_store.get_trip_by_user(user_id)
    trip_store.update_location(user_id, lat, lng)
    event_dispatcher.handle_location_update(user_id, lat, lng, trip)
    return {"status": "ok"}