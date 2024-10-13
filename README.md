# Selenium Python Sample Project

## Project Overview
This project is a sample Selenium automation framework implemented in Python, demonstrating the use of the Page Object Model (POM) for organizing code in a maintainable and scalable way.

## Project Structure
```
seleniumPythonSampleProject/
├── .venv                    # Virtual environment directory
├── pages                    # Page Object Model classes
│   ├── base_page.py         # Base page class with common methods
│   └── login_page.py        # Login page class with specific methods
├── reports                  # Directory for logs and reports
│   └── logs.txt             # Log file for test results
├── tests                    # Test cases
│   └── test_login.py        # Test case for login functionality
├── utils                    # Utility modules
│   └── config.py            # Configuration settings
├── conftest.py              # pytest configuration and fixtures
├── .gitignore               # Git ignore file
├── README.md                # Project documentation
└── requirements.txt         # Python dependencies
```

## Prerequisites
- Python 3.x
- pip (Python package installer)
- A web browser (e.g., Chrome or Firefox) and the corresponding WebDriver installed

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd seleniumPythonSampleProject
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Update `config.py`**:
   - Modify the `BASE_URL`, `USER_NAME`, and `PASSWORD` variables in `utils/config.py` with the appropriate values for your application.

2. **Run tests**:
   - Execute the test cases using pytest:
   ```bash
   pytest tests/test_login.py
   ```

3. **Check logs**:
   - Test results will be logged in `reports/logs.txt`.

## Project Details

### Pages
- **BasePage**: Contains common methods for interacting with web elements.
- **LoginPage**: Contains methods specific to the login functionality.

### Tests
- **test_login.py**: Contains test cases for verifying the login functionality.

### Utilities
- **config.py**: Holds configuration settings.
- **conftest.py**: Contains pytest fixtures for setup and teardown of the WebDriver.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or raise an issue.

## License
This project is licensed under the MIT License.
