import streamlit as st
import requests

def main():
    st.header("Audio Processing App")

    # Display HTML content
    st.components.v1.html(
        """
        <p>Upload an audio file for processing:</p>
        """
    )

    # Upload file widget
    uploaded_file = st.file_uploader("Choose an audio file", type="audio/*")

    if uploaded_file is not None:
        # Prepare data for API request
        data = {"audio_file": uploaded_file}

        # Send POST request to FastAPI endpoint
        response = requests.post("http://localhost:8000/process_audio", files=data)

        if response.status_code == 200:
            # Display processing result
            processed_data = response.json()["processed_data"]
            st.success(f"Processing result: {processed_data}")
        else:
            # Handle errors
            error_message = response.json().get("error", "Unknown error")
            st.error(f"Error: {error_message}")

if __name__ == "__main__":
    main()