# Weather-Application

This is a Django-based weather application. The project provides a web interface to view weather information.


## Setup Instructions

1. **Clone the repository**

    ```bash
    git clone https://github.com/Priyanshu2sh/Weather-Application.git
    cd weather_project
    ```

2. **Create and activate a virtual environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up API keys**

    The project requires an API key to fetch weather data. The API key is set directly in the `weather_app/views.py` file. The default API key is provided. You can either use this key or replace it with your own.

    ```python
    # weather_app/views.py
    API_KEY = 'your_api_key_here'
    ```

5. **Apply migrations**

    ```bash
    python manage.py migrate
    ```

6. **Run the development server**

    ```bash
    python manage.py runserver
    ```

7. **Access the application**

    Open your web browser and go to `http://127.0.0.1:8000` to view the application.

## Additional Information

- The project uses SQLite as the database, which is included in the repository as `db.sqlite3`.
- The weather data is displayed on the main page located at `weather_app/templates/weather_app/index.html`.

## Troubleshooting

- If you encounter any issues, ensure all dependencies are installed correctly and the virtual environment is activated.
- Check if the API key in `weather_app/views.py` is correctly set up.
