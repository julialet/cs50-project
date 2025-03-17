import pandas as pd
from datetime import datetime
import win32com.client as win32


def convert_bd(excel_data):
    try:
        excel_data["Birthday"] = pd.to_datetime(excel_data["Birthday"], format="%d/%m/%Y")
        print("The 'Birthday' column was successfully converted.")
    except Exception as e:
        print(f"Error converting the 'Birthday' column: {e}")


def filter_bd(excel_data, current_date):
    try:
        filtered_data = excel_data[(excel_data["Birthday"].dt.month == current_date.month) & 
                                    (excel_data["Birthday"].dt.day == current_date.day)]
        return filtered_data
    except Exception as e:
        print(f"Error filtering birthdays: {e}")
        return pd.DataFrame()


def send_email(bd_list):
    try:
        olApp = win32.Dispatch('Outlook.Application')
        mailItem = olApp.CreateItem(0)
        
        mailItem.Subject = "🎉 Today's Birthdays 🎉"
        mailItem.BodyFormat = 1

        email_body = "Here are today's birthdays:\n\n"
        for _, row in bd_list.iterrows():
            email_body += f"- {row['Name']} ({row['Birthday'].strftime('%d/%m/%Y')})\n"

        email_body += "\nWishing them all a fantastic day ahead! 🎂🎉" 

        mailItem.Body = email_body
        mailItem.To = "juliahille111@gmail.com" 

        mailItem.Send()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")


def main():
    try:
        excel_data = pd.read_excel("excel-bd.xlsx")
        if excel_data.empty:
            print("The spreadsheet is empty or wasn't loaded correctly.")
            return
    except Exception as e:
        print(f"Error loading the spreadsheet: {e}")
        return
    
    convert_bd(excel_data)
    
    current_date = datetime.now()
    current_bd = filter_bd(excel_data, current_date)
    
    if not current_bd.empty:
        print("Today's birthdays:\n", current_bd)
        send_email(current_bd)
    else:
        print("No birthdays today!")

if __name__ == "__main__":
    main()
