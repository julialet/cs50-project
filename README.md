# Birthday Reminder 🎂🎈

**Video Demo**: [TODO: Add Video URL Here]

## Description

Birthday Reminder is a Python project designed to help users keep track of upcoming birthdays. The core idea of the project is to read an Excel file containing a list of names and birthdates, process the data, and send email reminders whenever a birthday occurs on the current date.

The main purpose of the project is to automate the process of sending birthday reminders via email so that the user doesn’t need to remember these important dates. To achieve this, the project uses the `pandas` library for data manipulation and `smtplib` to send emails through Outlook. Additionally, using Excel files makes the project easy to use and accessible to users who already maintain their birthday information in spreadsheets.

The project is broken down into several functions, each responsible for a specific task: data conversion, filtering, and sending emails. These functions are well-defined, making the code easier to maintain and allowing for future expansions, such as adding support for other email providers or creating a graphical user interface (GUI) for user interaction.


## Features

- **Automated Birthday Checking**: Reads and filters birthday data from an Excel sheet.
- **Email Notifications**: Sends automated email reminders via Outlook.
- **Data Conversion**: Converts birthdates to datetime format to ensure accurate filtering and date comparison.

## Project Structure

- **project.py**: This is the main script that orchestrates reading, filtering, and sending birthday reminders.
- **test_project.py**: The test file containing pytest test cases to ensure the correctness of the code.
- **requirements.txt**: A list of required dependencies to run the project.
- **README.md**: Project documentation.

## Implementation Details

- **convert_bd(data)**: Converts the 'Birthday' column from string format to datetime format for accurate filtering.
- **filter_bd(data, current_date)**: Filters the dataset to retrieve birthdays that match the given date.
- **send_email(data)**: Sends an email notification for each person whose birthday is today.
- **main()**: The entry point that ties everything together.

## Design Decisions

- **Why use Pandas?**  
  Pandas simplifies data manipulation and filtering operations, making it easy to process and manage large datasets like Excel files.

- **Why use Outlook for email?**  
  Many corporate environments rely on Outlook, making this integration particularly useful for workplace reminders.

- **Why include tests?**  
  Including tests ensures the reliability of each function and helps maintain correctness as the project evolves.

## Installation & Usage

### Prerequisites

- Python 3.x
- Microsoft Outlook (for email functionality)

### Required dependencies

Install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```
### Running the Program

To run the program, execute the following command in your terminal:

```bash
python project.py
```
Running Tests
To run the tests, use pytest:

```bash
pytest test_project.py
```
## Future Improvements

- **Add Support for Multiple Email Providers**: Allow the program to send emails via different providers, like Gmail, Yahoo, etc. 
- **Enable Scheduling**: Implement scheduling functionality to run the program automatically at a fixed time every day.

This project was created as the culmination of the CS50 final project, showcasing the skills and knowledge gained throughout the course. 🚀

