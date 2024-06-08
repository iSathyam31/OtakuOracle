## OtakuOracle
This project is a comprehensive platform for anime enthusiasts, providing features such as anime recommendations, chatting with anime characters, and anime character detection from images.


## Features
- **Anime Recommender:** Get recommendations for anime titles based on your input.
- **Chat with Anime Characters:** Interact with AI-generated responses in the style of your favorite anime characters.
- **Anime Character Detection:** Upload an image and receive details about the anime characters detected in the image.


## Demo Video
![Demo Video](Demo.mp4)


## Folder Structure
```
OtakuOracle/
│
├── README.md
├── requirements.txt
├── app.py
├── assets/
│ ├── images/
│ └── video/
│ └── Demo.mp4
├── LICENSE
```

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


## Usage

- **Anime Recommender:** Enter the title of an anime and click "Get Recommendations" to receive similar anime recommendations.
- **Chat with Anime Characters:** Enter the name of an anime character and your question to receive a response in the style of that character.
- **Anime Character Detection:** Upload an image containing anime characters and click "Tell me the Character" to detect and get details about the characters in the image.


## License

This project is licensed under the terms of the [MIT License](LICENSE).


## Acknowledgments

- The project utilizes the Google Generative AI models for anime character chat and image recognition.
- Special thanks to the contributors of Streamlit for providing an excellent framework for building interactive web applications.