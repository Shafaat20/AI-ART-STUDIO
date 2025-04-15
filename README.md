
# AI Art Studio

A professional AI-powered web application that generates images from text prompts using the OpenAI API.

## Features

- User authentication (signup, login, profile management)
- AI image generation using OpenAI's DALL-E model
- Image download and storage
- Dark mode with VS Code jellyfish color theme
- Responsive design

## Setup Instructions

1. Clone this repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up your OpenAI API key as an environment variable:
   - Go to Replit Secrets panel
   - Add a new secret with key `OPENAI_API_KEY` and your OpenAI API key as the value

4. Run the application:
   ```
   python main.py
   ```

## Technology Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Python Flask
- Database: SQLite
- AI: OpenAI DALL-E API

## Project Structure

- `/static` - CSS, JavaScript, and other static files
- `/templates` - HTML templates
- `/instance` - SQLite database
- `main.py` - Main application file

## Notes

- The application uses a SQLite database to store user information and generated images
- Images are stored as base64-encoded strings in the database
- The OpenAI API key must be set as an environment variable for image generation to work
