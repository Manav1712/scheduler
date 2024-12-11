import heapq
from datetime import datetime, timedelta
from collections import defaultdict

class LaundryScheduler:
    def __init__(self, start_time, end_time, slot_duration, max_slots):
        self.start_time = datetime.strptime(start_time, "%H:%M").time()
        self.end_time = datetime.strptime(end_time, "%H:%M").time()
        self.slot_duration = slot_duration
        self.max_slots = max_slots
        self.slots = defaultdict(lambda: {"capacity": max_slots})
        self.users = {}

    def generate_slots(self):
        current_time = datetime.combine(datetime.today(), self.start_time)
        end_time = datetime.combine(datetime.today(), self.end_time)

        while current_time < end_time:
            self.slots[current_time.time()] = {"capacity": self.max_slots}
            current_time += timedelta(minutes=self.slot_duration)

    def schedule_request(self, user_id, preferred_time):
        preferred_time = datetime.strptime(preferred_time, "%H:%M").time()
        
        for slot_time in sorted(self.slots.keys()):
            if slot_time >= preferred_time and self.slots[slot_time]["capacity"] > 0:
                self.slots[slot_time]["capacity"] -= 1
                self.users[user_id] = slot_time.strftime("%H:%M")
                return slot_time.strftime("%H:%M")

        return None

    def display_schedule(self):
        print("\nCurrent Schedule:")
        for slot_time, slot_info in sorted(self.slots.items()):
            print(f"Time: {slot_time.strftime('%H:%M')}, Available: {slot_info['capacity']}/{self.max_slots}")

    def display_user_schedules(self):
        print("\nUser Schedules:")
        for user_id, slot_time in self.users.items():
            print(f"User {user_id}: Scheduled at {slot_time}")

def main():
    scheduler = LaundryScheduler("08:00", "20:00", 30, 5)
    scheduler.generate_slots()

    print("Welcome to the Laundry Scheduler!")
    print("Available time slots are from 08:00 to 20:00, every 30 minutes.")

    while True:
        print("\nOptions:")
        print("1. Schedule a laundry slot")
        print("2. View current schedule")
        print("3. View user schedules")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            user_id = input("Enter user ID: ")
            preferred_time = input("Enter preferred time (HH:MM): ")
            result = scheduler.schedule_request(user_id, preferred_time)
            if result:
                print(f"Slot scheduled for User {user_id} at {result}")
            else:
                print("No available slots at or after the preferred time.")
        elif choice == '2':
            scheduler.display_schedule()
        elif choice == '3':
            scheduler.display_user_schedules()
        elif choice == '4':
            print("Thank you for using the Laundry Scheduler. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
