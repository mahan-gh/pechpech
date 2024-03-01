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
    uploaded_file = st.file_uploader("Choose an audio file", type=["mp3"])

    if uploaded_file is not None:
        data = {"file": uploaded_file}

        response = requests.post("http://0.0.0.0:8000/process_audio", files=data)

        if response.status_code == 200:
            # Display processing result
            processed_data = response.json()["processed_data"]
            st.success(f"Processing result: {processed_data}")
        else:
            # Handle errors
            # error_message = response.json().get("error", "Unknown error")
            st.error(f"Error: {response = }")

if __name__ == "__main__":
    main()