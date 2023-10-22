# Flask Text-to-Video Application

This Flask application provides a simple interface for users to input text and generate a corresponding video. It utilizes `pyttsx3` to convert the text into audio and `moviepy` to create a video by combining the audio with an image.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Usage](#usage)
- [Image Placeholder](#image-placeholder)
- [Contributions](#contributions)
- [License](#license)
- [Contact Information](#contact-information)

## Features
- Convert user-input text (up to 1000 characters) into audio.
- Generate a video combining the text's audio with a default image.
- User-friendly interface with immediate video playback.

## Prerequisites
- Python 3.6 or later.
- `pip` (Python package installer).

## Getting Started

### Installation
1. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    ```

2. **Navigate to the Project Directory**:
    ```bash
    cd path-to-cloned-directory
    ```

3. **Create a Virtual Environment**:
    ```bash
    python3 -m venv venv
    ```

4. **Activate the Virtual Environment**:
    ```bash
    # On macOS and Linux:
    source venv/bin/activate
   
    # On Windows:
    .\venv\Scripts\activate    
    ```

5. **Install Required Packages**:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application
    ```bash
    python app.py
    ```
Navigate to `http://127.0.0.1:5000/` in your preferred web browser.

## Usage
1. Input text into the provided text area.
2. Click on "Generate Video".
3. Wait for the video to be processed, and it will be displayed on the page.

## Image Placeholder
Before each execution, make sure to replace the `placeholder.jpg` image in the `static` directory with your desired image. This image will serve as the visual background for the generated video.

## Contributions
Contributions, issues, and feature requests are welcome. Please open an issue first if you wish to make significant changes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
