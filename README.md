## Morning Greetings

A Python package that automates the process of sending personalized "Good Morning" messages to a list of contacts. The package allows users to manage a contact list, generate custom messages, and simulate sending them via a console application. This project also supports loading contacts from a file, adding new contacts interactively, and logging the messages sent.

## Features

- Manage a list of contacts with names, email addresses, and preferred greeting times.
- Load contacts from a text file.
- Interactively add new contacts through a text editor.
- Generate personalized "Good Morning" messages for each contact.
- Simulate sending the messages and log the results.
- Modular code structure that makes it easy to extend.

## Installation

1. **Clone the Repository**

   Clone the repository from GitHub to your local machine:

   ```bash
   git clone https://github.com/your-username/morning_greetings.git
   cd morning_greetings
   ```

## Installation

To install the package locally using setup.py, run:

pip install .

This will install the morning_greetings package and make it available for use in your Python environment.

## addmore_contact_main.py is working only with python addmore_contact_main.py

After installing the package, you can run the main script to manage contacts and send greetings:

python addmore_contact_main.py

## Interacting with the Program

When the script runs, it will try to load existing contacts from new_contacts.txt.
If the file exists and is properly formatted, the contacts will be added to the list.
You will then be asked if you want to add more people.
If you choose "yes", a text editor will open where you can add more contacts.
The format for adding contacts is:

**Name, Email, Preferred Time (optional)**
Example:

Alice, alice@example.com, 08:00 AM
Bob, bob@example.com, 09:00 AM
Sending Greetings

The program will send personalized "Good Morning" messages to all contacts in the list. The messages will be displayed in the console, and a log of the sent messages will be saved to message_log.txt.

## Project Structure

morning_greetings/
│
├── morning_greetings/ # Package directory
│ ├── **init**.py # Package initialization file
│ ├── contacts_manager.py # Manages advanced contact operations
├── contacts.py # Handles basic contact data structure and operations
│ ├── message_generator.py # Generates personalized messages
│ ├── message_sender.py # Simulates sending messages
│ ├── logger.py # Logs sent messages
├── main.py  
│
├── addmore_contact_main.py # Main script to run the program(this one is not working for now . it contains main function and have dynamically adding contacts functionality, currently it is located in test_main folder)
├── setup.py # Setup script for installing the package
├── README.md # Project documentation
└── new_contacts.txt # File for adding new contacts (optional, created at runtime)

## Development

Editable Install
If you're developing the package and want changes to be reflected immediately, you can install the package in "editable" mode:

pip install -e .

## Contributing

Contributions are welcome! If you have ideas to improve the package, please fork the repository and submit a pull request.

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes and commit (git commit -m 'Add new feature').
4. Push to the branch (git push origin feature-branch).
5. Create a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.
