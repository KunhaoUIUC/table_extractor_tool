A web application that extracts tables from PDF files and allows users to export them as CSV files. The backend is built with Flask, and the frontend is built with React. 

# Prerequisites:
Python 3.8+
Node.js 14+

# Setup and Installation

## Backend:

### Navigate to the backend directory:
```
cd table_extractor_tool/backend
```

### Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
Note: Creating a virtual environment allows you to manage dependencies for your project in isolation from other projects, avoiding conflicts and ensuring reproducibility.

### Install the dependencies:
```
pip install -r requirements.txt
```

### Run the Flask application
```
flask run
```

## Frontend:
### Navigate to the frontend directory:
```
cd table_extractor_tool/frontend
```
### Install the dependencies:
```
npm install
```

### Run the React application:
```
npm start
```




