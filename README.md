# Customer workflow system

This project is a web-based workflow system to capture customer information and their financial data from an uploaded Excel file and display them in a graph.

## Requirements
- Python 3.x
- Flask
- Pandas
- Matplotlib
- Openpyxl (for reading .xlsx files)

## Installation

1. Clone the repository:
    ```
    git clone <repository_url>
    ```
2. Navigate to the project directory:
    ```
    cd <project_directory>
    ```
3. Install the required packages:
    ```
    pip install pandas
    pip install matplotlib
    pip install openpyxl --upgrade
    pip install plotly
    pip install cufflinks
    ```

## Running the Application

1. Run the Flask application:
    ```
    python app.py

    or

    python3 app.py

    ```
2. Open your web browser and go to `http://127.0.0.1:5000/`.

## Usage

1. Fill in the customer information form.
2. Upload an Excel file containing financial data with contains: `Month`, `Income`, and `Expenses`.
3. Submit the form to generate and view the temporal graph.

## Assumptions

- The Excel file should contain the columns: `Month`, `Income`, and `Expenses`.
- The application handles only one user at a time.
- The UI is simple and styled using basic HTML and CSS and flask framework.


