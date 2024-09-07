# Video to GIF Converter with Streamlit

This project is a simple **video to GIF converter** built using **Python** and **Streamlit**. It allows users to upload a video, adjust the frames per second (FPS), and convert the video into a GIF. The resulting GIF can then be downloaded.

## Features

- Upload video files in `.mp4`, `.avi`, or `.mov` formats.
- Adjust the **FPS (frames per second)** for the GIF.
- Preview the uploaded video.
- Convert the video to GIF.
- Download the generated GIF.

## Technologies Used

- **Python**: The main programming language used.
- **MoviePy**: Used for processing and converting the video to GIF.
- **Streamlit**: Used to create the interactive web application.
- **Tempfile**: Used for handling temporary files during the conversion process.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/video-to-gif-converter.git
   cd video-to-gif-converter
  
2. Create a virtual environment (optional but recommended):
   ```bash
	python3 -m venv env
	source env/bin/activate  # On Windows use `env\Scripts\activate`

3. Install the required dependencies:
   ```bash
	pip install -r requirements.txt

## Usage

1. Run the Streamlit app
   ```bash
	streamlit run app.py
 2. Open your browser and go to `http://localhost:8501`.
    
2. Upload a video file, adjust the FPS using the slider, and click **Convert to GIF**.
    
3. Once the conversion is complete, you can download the generated GIF.

## Example
After uploading a video and adjusting the FPS, the app will display the video and provide a button to convert it to a GIF. Once the GIF is generated, you can download it directly from the interface.

## Requirements
Make sure you have the following dependencies installed:

- Python 3.7+
- Streamlit
- MoviePy
- imageio

These can be installed via the `requirements.txt` file.
