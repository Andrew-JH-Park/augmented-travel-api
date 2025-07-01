# Trip state lifecycle
import app.storage.trip_store as trip_store

def update_trip_state(trip, lat, lng):
    if trip.state == "ENROUTE_TO_PICKUP" and is_near(trip.pickup, lat, lng):
        trip.state = "PICKED_UP"
    elif trip.state == "ENROUTE_TO_DROPOFF" and is_near(trip.dropoff, lat, lng):
        trip.state = "COMPLETED"
    # Save update
    trip_store.save_trip(trip)