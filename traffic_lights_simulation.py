import time
from datetime import datetime

# Default durations in seconds
DAY_GREEN_DURATION = 10
DAY_YELLOW_DURATION = 3
DAY_RED_DURATION = 10

NIGHT_GREEN_DURATION = 5
NIGHT_YELLOW_DURATION = 2
NIGHT_RED_DURATION = 5

# Helper to check if it is night
def is_night():
    current_hour = datetime.now().hour
    return current_hour >= 21 or current_hour < 5

# Simulate one cycle of traffic light
def simulate_light(emergency=False):
    if is_night():
        green_time = NIGHT_GREEN_DURATION
        yellow_time = NIGHT_YELLOW_DURATION
        red_time = NIGHT_RED_DURATION
    else:
        green_time = DAY_GREEN_DURATION
        yellow_time = DAY_YELLOW_DURATION
        red_time = DAY_RED_DURATION

    if emergency:
        print("🚨 Emergency Detected! Switching to GREEN for ambulance.")
        print("Green (Emergency Mode)")
        time.sleep(5)  # Give green for 5 seconds during emergency
        return

    # Regular cycle
    print("Red ")
    time.sleep(red_time)
    print("Green ")
    time.sleep(green_time)
    print("Yellow ")
    time.sleep(yellow_time)

# Simulate for N cycles or until stopped
def traffic_light_simulation():
    cycle = 0
    while True:
        print(f"\n--- Cycle {cycle + 1} ---")
        
        # Simulate emergency randomly (for demo, every 5th cycle)
        if cycle % 5 == 4:
            simulate_light(emergency=True)
        else:
            simulate_light(emergency=False)

        cycle += 1
        time.sleep(1)

# Run the simulation
try:
    traffic_light_simulation()
except KeyboardInterrupt:
    print("\nSimulation stopped.")
