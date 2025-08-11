# Product Labeler Application

## 1. Overview

The Product Labeler Application is a Python-based GUI tool designed for labeling ground truth on product images. It enables users to accurately annotate key product information such as product name, manufacturer details, importer details, manufacturing date, expiry date, and product type. These ground truth labels provide high-quality, reliable data essential for training and validating AI models.
The application supports:

- Loading and displaying images (PNG, JPG, JPEG, HEIC).
- AI-powered label suggestions using Google Gemini.
- Input validation (phone numbers, dates, character limits, etc.).
- Saving images and metadata into a MySQL database.
- Viewing products by category, viewing details, and deleting entries.
- Exporting data to timestamped JSON files.
- Friendly error handling.

## 2. Main Technologies

- Python 3.12+
- GUI: Tkinter
- Database: MySQL
- AI Suggestion: Google Gemini API
- Image Handling: Pillow (PIL)
- Supporting Libraries: mysql-connector-python, base64, re, json, python-dotenv, etc.

## 3. Key Features

- **Image Loading:** Supports common image formats.
- **AI Suggestions:** Auto-fill fields using Google Gemini AI.
- **Validation:** Checks phone number formats, date formats, expiry date ≥ manufacturing date, etc.
- **Data Storage:** Saves images as base64 along with metadata in MySQL, prevents duplicates.
- **Data Management:** Displays products by category, detailed view, and delete option.
- **JSON Export:** Exports all data to a JSON file with a timestamp.
- **Error Handling:** Clear messages for input errors, database connection issues, etc.

## 4. Installation Requirements and Configuration

### Configuration file `config.env`
To securely store sensitive information like database credentials and API keys, create a file named `config.env` in the root folder of your project with the following sample content:

```env
# Database configuration
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_mysql_password
MYSQL_DATABASE=product_db
MYSQL_PORT=3306

# Google Gemini API Key
GEMINI_API_KEY=your_google_gemini_api_key
```
- Python 3.12 or higher
- Install required libraries:
```bash
pip install tkinter mysql-connector-python pillow python-dotenv google-generativeai
