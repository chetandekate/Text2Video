# Flask Text-to-Video Converter: Transform Words into Visual Stories

Create immersive videos from text with our #Flask Text-to-Video Converter. Leveraging #pyttsx3 for audio synthesis and #moviepy for video creation, it's perfect for transforming narratives into visual content.

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
-Text-to-audio conversion with up to 1000 characters.
- Automatic video production combining audio and images.
- User-friendly interface for immediate playback.

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

#Python #WebDevelopment #OpenSource #TechInnovation
