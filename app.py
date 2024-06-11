from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()

# Configure the generative AI models with API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get anime recommendations from Gemini
def get_anime_recommendations(anime_title):
    query = f"Give me 5 anime recommendations similar to {anime_title} with the following details: Anime, Genre, Main Protagonists, Summary."
    response = chat.send_message(query, stream=True)
    full_response = ""
    for chunk in response:
        full_response += chunk.text
    return full_response

# Function to format the anime recommendation response
def format_anime_recommendation(text):
    # Process the response to format each recommended anime
    recommendations = text.split('\n\n')
    formatted_recommendations = []
    for rec in recommendations:
        lines = rec.split('\n')
        if len(lines) >= 4:
            anime = lines[0].replace("Anime:", "").strip()
            genre = lines[1].replace("Genre:", "").strip()
            protagonists = lines[2].replace("Main Protagonists:", "").strip()
            summary = lines[3].replace("Summary:", "").strip()
            formatted_recommendations.append({
                "Anime": anime,
                "Genre": genre,
                "Main Protagonists": protagonists,
                "Summary": summary
            })
    return formatted_recommendations

# Function to get response from Gemini with specific anime character style
def get_anime_character_response(character, question):
    query = f"Respond to the following question in the style of the anime character {character}: {question}"
    response = chat.send_message(query, stream=True)
    full_response = ""
    for chunk in response:
        full_response += chunk.text
    return full_response

# Function to load Google Gemini Pro Vision API And get response
def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, image[0], prompt])
    return response.text

# Function to set up input image
def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        # Format of file given to Google Gemini Pro
        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Initialize the Gemini Pro model for anime character chat
chat = genai.GenerativeModel("gemini-pro") 
chat = chat.start_chat(history=[])

# Initialize Streamlit app
st.set_page_config(page_title="OtakuOracle 🌟", layout="wide")

# Sidebar navigation
page = st.sidebar.selectbox("Select Service", ["Anime Recommender 🌟", "Talk to Anime Character 🗣️", "Anime Face Detect 👀"])

# Page for Anime Recommender
if page == "Anime Recommender 🌟":
    st.header("Anime Recommender System 🎬")

    # Get user input
    input_anime = st.text_input("Input Anime Title: ", key="input_anime", help="Enter the title of an anime you like and get similar recommendations! 🍿")
    submit_anime = st.button("Get Recommendations 🚀")

    # Process the input and get recommendations
    if submit_anime and input_anime:
        st.info("Fetching recommendations... 🔍")
        response = get_anime_recommendations(input_anime)
        recommendations = format_anime_recommendation(response)
        
        # Display the recommendations
        st.subheader("Anime Recommendations 📜")
        for rec in recommendations:
            st.write(f"**Anime:** {rec['Anime']} 📺")
            st.write(f"**Genre:** {rec['Genre']} 🎭")
            st.write(f"**Main Protagonists:** {rec['Main Protagonists']} 🧑‍🤝‍🧑")
            st.write(f"**Summary:** {rec['Summary']} 📝")
            st.write("---")

# Page for Talking to Anime Character
elif page == "Talk to Anime Character 🗣️":
    st.header("Chat with an Anime Character 💬")

    # Get user input
    character = st.text_input("Anime Character Name: ", key="character", help="Enter the name of an anime character you want to talk to! 🧙‍♂️")
    question = st.text_input("Your Question: ", key="question", help="Ask your question here! ❓")
    submit_character = st.button("Ask the character 🙋")

    # Process the input and get a response
    if submit_character and character and question:
        st.info("Getting response from character... 💭")
        response = get_anime_character_response(character, question)
        
        # Display the response
        st.subheader(f"Response from {character} 🗨️")
        st.write(response)

# Page for Anime Face Detect
elif page == "Anime Face Detect 👀":
    st.header("Anime Character Detector 🕵️")

    input_prompt = """
    You are an expert in the world of Anime where you need to see characters from the image and provide the details of every character in this below format:

    1. Name of the Character(s):
    2. Anime:
    3. Role:
    4. Favourite Habit:

    If there are multiple characters then mention them separately in the above format

    Note: If you don't find the character related to any Anime then kindly tell the user to provide an Anime character picture in this below format:
    'Kindly provide a character from Anime'
    """

    input_text = st.text_input("Input Prompt: ", key="input_text", help="Enter your custom prompt here! 📜")
    uploaded_file = st.file_uploader("Choose an image... 📷", type=["jpg", "jpeg", "png"])
    image = ""
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image. 🖼️", use_column_width=True)

    submit_image = st.button("Tell me the Character 🎭")

    if submit_image:
        st.info("Analyzing the image... 🔍")
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_response(input_text, image_data, input_prompt)
        st.subheader("The Response is 📢")
        st.write(response)
