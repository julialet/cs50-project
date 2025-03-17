import pandas as pd
from datetime import datetime
import pytest
from project import convert_bd, filter_bd, send_email, main

# Test if the convert_bd function correctly converts the 'Birthday' column to datetime format.
def test_convert_bd():
    mock_data = pd.DataFrame({
        'Name': ['John', 'Jane'],
        'Birthday': ['10/03/1990', '10/03/1985']
    })
    
    convert_bd(mock_data)
    
    assert pd.api.types.is_datetime64_any_dtype(mock_data['Birthday']), "Birthday column was not converted to datetime."

# Test if the filter_bd function correctly filters birthdays matching the current date.
def test_filter_bd():
    mock_data = pd.DataFrame({
        'Name': ['John', 'Jane'],
        'Birthday': [datetime(1990, 3, 10), datetime(1995, 3, 10)]
    })

    current_date = datetime(2025, 3, 10)

    filtered_data = filter_bd(mock_data, current_date)
    assert len(filtered_data) == 2, "The filter function didn't return the correct number of birthdays."

# Test if send_email correctly interacts with Outlook to send an email.
def test_send_email(mocker):
    mock_data = pd.DataFrame({
        'Name': ['John'],
        'Birthday': [datetime(1990, 3, 10)]
    })
    
    mock_dispatch = mocker.patch('win32com.client.Dispatch')
    mock_mail = mock_dispatch.return_value.CreateItem.return_value

    send_email(mock_data)

    mock_mail.Send.assert_called_once()

# Test if the main function correctly loads data, filters birthdays, and sends an email.
def test_main(mocker):
    mock_read_excel = mocker.patch('pandas.read_excel')
    mock_dispatch = mocker.patch('win32com.client.Dispatch')
    mock_datetime = mocker.patch('project.datetime')

    mock_data = pd.DataFrame({
        'Name': ['John', 'Jane'],
        'Birthday': ['10/03/1990', '10/03/1985']
    })
    mock_read_excel.return_value = mock_data

    mock_datetime.now.return_value = datetime(2025, 3, 13)

    main()
