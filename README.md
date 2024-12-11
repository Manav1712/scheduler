# Laundry Scheduler Algorithm for Palwash

A Python-based scheduling algorithm designed to streamline laundry pickup and delivery services for college students. This project includes a command-line interface for demonstrating the app's functionality, with options to create user accounts, schedule laundry pickups, and manage service requests.

## Features

- **User Registration/Login**: Allows students to register and authenticate their accounts.
- **Scheduling**: Enables users to book laundry pickups and deliveries based on predefined time slots.
- **Conflict Management**: Automatically detects and resolves scheduling conflicts.
- **Admin Controls**: Allows admins to manage time slots, view schedules, and adjust operations as needed.
- **CSV Storage**: Stores user data and schedules locally for simplicity.

## Requirements

- Python 3.8+
- Required libraries: Install dependencies using the command below:

```bash
pip install pandas tabulate
```

## File Structure

```
.
|-- laundry_scheduler.py     # Main script containing the scheduling algorithm and CLI
|-- users.csv                # Stores user data
|-- schedules.csv            # Stores booking data
|-- README.md                # Project documentation
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/laundry-scheduler.git
cd laundry-scheduler
```

2. Run the script:

```bash
python laundry_scheduler.py
```

3. Follow the prompts to:
   - Register a new user.
   - Login to an existing account.
   - Schedule laundry pickups and deliveries.
   - View existing schedules (Admin feature).

## Demo

To demonstrate the functionality:

1. **Create Sample Users**: 
   - Edit `users.csv` to prepopulate data for presentation purposes.

2. **Schedule a Pickup**:
   - Run the app and simulate a user booking a laundry slot.

3. **Resolve Conflicts**:
   - Show how the algorithm manages scheduling conflicts and provides alternate options.

## Example Workflow

```bash
$ python laundry_scheduler.py
Welcome to the Laundry Scheduler App!
1. Register
2. Login
3. Exit
Choose an option: 1
Enter your name: John Doe
Enter your email (.edu required): john.doe@university.edu
Registration successful! You can now log in.
...
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add feature'`
4. Push the branch: `git push origin feature-name`
5. Submit a pull request.

## License

This project is licensed under the MIT License. See `LICENSE` for details.

## Contact

For questions or feedback, reach out to:

- **Name**: Manav Jairam
- **Email**: manav172022@gmail.com
- **GitHub**: [Manav1712](https://github.com/Manav1712)
