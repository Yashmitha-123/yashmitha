import streamlit as st
from transformers import pipeline
from PIL import Image
import torch
import tempfile
import librosa
import soundfile as sf

st.title("AI Playground with Transformers")
task = st.sidebar.selectbox(
    "Choose a task:",
    ["Sentiment Analysis", "Text Generation", "Image Classification", "Automatic Speech Recognition"]
)

@st.cache_resource
def load_sentiment():
    return pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english",
        device=0 if torch.cuda.is_available() else -1
    )

@st.cache_resource
def load_generator():
    return pipeline(
        "text-generation",
        model="gpt2",
        device=0 if torch.cuda.is_available() else -1
    )

@st.cache_resource
def load_image_classifier():
    return pipeline(
        "image-classification",
        model="google/vit-base-patch16-224",
        device=0 if torch.cuda.is_available() else -1
    )

@st.cache_resource
def load_asr():
    return pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-tiny",  
        device=0 if torch.cuda.is_available() else -1
    )


if task == "Sentiment Analysis":
    text = st.text_area("Enter text:", "I love using transformers for AI projects")

    if st.button("Analyze"):
        with st.spinner("Loading model..."):
            sentiment_model = load_sentiment()

        result = sentiment_model(text)[0]
        st.success(f"Sentiment: {result['label']}")
        st.write(f"Score: {result['score']:.4f}")

elif task == "Text Generation":
    prompt = st.text_area("Enter prompt:", "Once upon a time")

    if st.button("Generate"):
        with st.spinner("Loading model..."):
            generator = load_generator()

        result = generator(
            prompt,
            max_length=50,
            num_return_sequences=1
        )[0]

        st.success("Generated Text:")
        st.write(result["generated_text"])


elif task == "Image Classification":
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Classify"):
            with st.spinner("Loading model..."):
                image_model = load_image_classifier()

            result = image_model(image)
            st.success(f"Prediction: {result[0]['label']}")



elif task == "Automatic Speech Recognition":
    uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])

    if uploaded_file is not None:
        st.audio(uploaded_file)

        if st.button("Recognize"):
            with st.spinner("Loading model..."):
                asr_model = load_asr() 

            
            audio, sr = librosa.load(uploaded_file, sr=16000)

           
            result = asr_model(audio)  

            st.success("Recognized Text:")
            st.write(result["text"])