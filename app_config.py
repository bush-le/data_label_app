import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import errorcode
import google.generativeai as genai 

# Load file config.env
load_dotenv("config.env")

# Database
def connect_db():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("MYSQLHOST"),
            user=os.getenv("MYSQLUSER"),
            password=os.getenv("MYSQLPASSWORD"),
            database=os.getenv("MYSQLDATABASE"),
            port=int(os.getenv("MYSQLPORT", '3306'))
        )
        print("MySQL: Connected successfully")
        return connection
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("MySQL: Invalid username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("MySQL: Database does not exist")
        else:
            print(f"MySQL: {err}")
        return None


# Gemini
def get_gemini_model():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Gemini: API key not found in .env file")
        return None

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("models/gemini-2.5-flash")

        # Gửi thử 1 request đơn giản để check key
        try:
            test_response = model.generate_content("Hi")
            if test_response and hasattr(test_response, "text"):
                print("Gemini: Connected successfully (API key valid)")
            else:
                print("Gemini: Connected but no valid response")
        except Exception as test_err:
            print(f"Gemini: API key may be invalid — {test_err}")
            return None

        return model

    except Exception as e:
        print(f"Gemini: Failed to connect — {e}")
        return None
