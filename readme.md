# DareUpdater

## Overview
dareUpdater can update your system and install all of your needed packages on new machines in seconds, dareUpdater can also install openVPN & whitelist your ip to port 22.

## Prerequisites
- Python 3.6 or higher
- `virtualenv` package

## Setup

### 1. Create a Virtual Environment
First, navigate to the root directory of the project:
```bash
cd /dareUpdater
```

Create a virtual environment:
```bash
python3 -m venv env
```

Activate the virtual environment:
- On macOS and Linux:
    ```bash
    source env/bin/activate
    ```

### 2. Install Dependencies
With the virtual environment activated, install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application
To run the application, ensure you are in the root directory and the virtual environment is activated:
```bash
python main.py
```

## Contributing
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
