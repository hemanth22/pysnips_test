import psycopg2
from datetime import datetime
import os
import requests
import pytz

postgres_hostname = os.environ.get('postgres_hostname')
postgres_database = os.environ.get('postgres_database')
postgres_port = os.environ.get('postgres_port')
postgres_username = os.environ.get('postgres_username')
postgres_password = os.environ.get('postgres_password')
bot_token = os.environ.get('Priyoid_bot')

  
def telegram_send_message(message):
    url = "https://api.telegram.org/bot{}/sendMessage?chat_id=-1001943848370&text={}".format(bot_token, message)
    requests.get(url)

def fetch_message_for_date(date_str):
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(database=postgres_database, user=postgres_username, password=postgres_password, host=postgres_hostname, port=postgres_port)
        cursor = connection.cursor()

        # Define the query with parameterized inputs
        query = """
        SELECT message 
        FROM remainder_messages 
        WHERE message_date = %s;
        """
        # Execute the query
        cursor.execute(query, (date_str,))
        results = cursor.fetchall()

        # Return messages if they exist
        if results:
            messages = [row[0] for row in results]
            return messages
        else:
            return ["No messages found for this date."]

    except (Exception, psycopg2.Error) as error:
        return [f"Error while connecting to PostgreSQL: {error}"]

    finally:
        # Close the database connection
        if connection:
            cursor.close()
            connection.close()

# Usage example
if __name__ == "__main__":
    # Specify the date in YYYY-MM-DD format
    ist_timezone = pytz.timezone("Asia/Kolkata")
    # Create a datetime object
    current_date = datetime.now(ist_timezone)
    # Format it to YYYY-MM-DD
    formatted_date = current_date.strftime("%Y-%m-%d")
    print(f"Formatted Date: {formatted_date}")
    date_to_query = formatted_date
    message = fetch_message_for_date(date_to_query)
    #telegram_send_message(message)
    for new_sendMessage_tele in message:
        telegram_send_message(new_sendMessage_tele)
    print(f"Message for {date_to_query}: {message}")

