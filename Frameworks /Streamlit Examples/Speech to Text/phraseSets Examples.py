import streamlit as st
from google.cloud import speech_v2

#... (Authentication and setup)
def transcribe_streaming(stream, phrases):
    # ... (Your streaming configuration and recognizer)

    # Update config with the phrase set from the console or inline phrases
    config.update(
        {
            "speech_contexts": [
                {"phrases": phrases, "boost": 20}
            ]
        }
    )

    requests = (
        speech_v2.StreamingRecognizeRequest(audio_content=chunk) for chunk in stream
    )
    responses = client.streaming_recognize(config, requests)
    # ... (Process responses to get transcription)

st.title("Real-Time Transcription with Phrase Set Boosting")
phrases = st.text_input("Enter phrases to boost (comma-separated):")

if st.button("Start Recording"):
    with sr.Microphone() as source:
        audio_data = r.listen_in_background(source, callback)
        
        # Split phrases entered in the text box and pass to transcribe_streaming
        phrases_list = [phrase.strip() for phrase in phrases.split(",")] if phrases else []
        
        # Pass both the audio stream and the list of phrases to the transcription function
        result = transcribe_streaming(audio_data, phrases_list)
        
        st.write("Transcription:", result)

