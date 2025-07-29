# MVP Garmin Project

This README provides instructions to set up the project on your local machine, including creating a Python virtual environment and running the main script.

## Prerequisites

- Python 3.8 or higher installed
- Git installed

## Setup Instructions

1. **Clone the Repository**

    ```bash
    git clone <repository-url>
    cd mvp garmin
    ```

2. **Create a Virtual Environment**

    ```bash
    python3 -m venv venv
    ```

3. **Activate the Virtual Environment**

    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```

4. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

## Running the Main Script

example command line argument

```bash
python main.py --username john.pork@outlook.com --password abc123! --start_date 2025-05-01 --end_date 2025-05-30
```

## Additional Notes

- Deactivate the virtual environment with `deactivate` when done.
- Update `requirements.txt` as needed for new dependencies.
