## OtakuOracle
This project is a comprehensive platform for anime enthusiasts, providing features such as anime recommendations, chatting with anime characters, and anime character detection from images.


## Features
- **Anime Recommender:** Get recommendations for anime titles based on your input.
- **Chat with Anime Characters:** Interact with AI-generated responses in the style of your favorite anime characters.
- **Anime Character Detection:** Upload an image and receive details about the anime characters detected in the image.


## Demo Video
[Watch Demo Video](link_to_demo_video)


## Folder Structure

OtakuOracle/
│
├── README.md
├── requirements.txt
├── app.py
├── assets/
│ ├── images/
│ └── video/
│ └── demo_video.mp4
├── LICENSE


## Setup Instructions
Follow these steps to set up the AnimeVerse project on your local machine:

1. Clone the repository:
    ```bash
    git clone https://github.com/your_username/AnimeVerse.git
    ```

2. Navigate to the project directory:
    ```bash
    cd AnimeVerse
    ```

3. Create a virtual environment (optional but recommended):
    ```bash
    conda create -p venv python=3.11 -y
    ```

4. Activate the virtual environment:
    - On Windows:
        ```bash
        conda activate venv/
        ```
    - On macOS and Linux:
        ```bash
        source env/bin/activate
        ```

5. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

6. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

7. Access the app in your web browser at [http://localhost:8501](http://localhost:8501).