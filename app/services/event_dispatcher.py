# Handles all event triggers

"""
List of events to be handled

New incoming request
Requested detour for tourism
Upcoming POI => generate voice
Trip State Updated => notify customer
Local information update
    => call weather service
    => congestion level en route
Approaching destination

"""

# from app.services.narration_service import maybe_trigger_narration
# from app.services.trip_state_machine import update_trip_state
# from app.services.poi_service import is_near_important_poi
#
# def handle_location_update(user_id, lat, lng, trip):
#     # Update state machine
#     update_trip_state(trip, lat, lng)
#
#     # Check for POI-based narration
#     if is_near_important_poi(lat, lng, trip):
#         maybe_trigger_narration(user_id, trip)
#
#     # Future triggers: ETA deviation, battery, weather
#     ...
