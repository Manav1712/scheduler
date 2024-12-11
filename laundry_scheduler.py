import pandas as pd
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
        self.load_users()
        self.load_schedules()

    def load_users(self):
        try:
            self.users_df = pd.read_csv('users.csv')
            for _, row in self.users_df.iterrows():
                self.users[row['user_id']] = row['name']
        except FileNotFoundError:
            self.users_df = pd.DataFrame(columns=['user_id', 'name'])

    def load_schedules(self):
        try:
            self.schedules_df = pd.read_csv('schedules.csv')
            for _, row in self.schedules_df.iterrows():
                scheduled_time = datetime.strptime(row['scheduled_time'], "%H:%M").time()
                if scheduled_time in self.slots:
                    self.slots[scheduled_time]["capacity"] -= 1
        except FileNotFoundError:
            self.schedules_df = pd.DataFrame(columns=['user_id', 'scheduled_time'])

    def save_users(self):
        self.users_df = pd.DataFrame(list(self.users.items()), columns=['user_id', 'name'])
        self.users_df.to_csv('users.csv', index=False)

    def save_schedules(self, user_id, scheduled_time):
        new_entry = pd.DataFrame([[user_id, scheduled_time]], columns=['user_id', 'scheduled_time'])
        self.schedules_df = pd.concat([self.schedules_df, new_entry], ignore_index=True)
        self.schedules_df.to_csv('schedules.csv', index=False)

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
                # Schedule the user
                self.slots[slot_time]["capacity"] -= 1
                if user_id not in self.users:
                    name = input("Enter your name: ")
                    self.users[user_id] = name
                    self.save_users()
                # Save the schedule
                scheduled_slot_str = slot_time.strftime("%H:%M")
                self.save_schedules(user_id, scheduled_slot_str)
                return scheduled_slot_str
        return None

    def display_schedule(self):
        print("\nCurrent Schedule:")
        for slot_time, slot_info in sorted(self.slots.items()):
            print(f"Time: {slot_time.strftime('%H:%M')}, Available: {slot_info['capacity']}/{self.max_slots}")

    def display_user_schedules(self):
        print("\nUser Schedules:")
        for user_id, slot in sorted(self.users.items()):
            print(f"User {user_id} ({slot}): Scheduled")

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

