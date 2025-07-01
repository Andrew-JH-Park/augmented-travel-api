from pydantic import BaseModel
from typing import List

class Trip(BaseModel):
    trip_id: str
    user_id: str
    state: str
    pickup: tuple
    dropoff: tuple
    passenger_count: int
    expected_duration: float
    expected_arrival: str
    current_location: tuple
    trip_sequence: List[str]
