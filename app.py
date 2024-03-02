import os
import time
import datetime

import whisper
import streamlit as st


model = whisper.load_model("small")

def feedTheModel(fileName, buffer):
    with open(fileName, 'wb') as f:
        f.write(buffer)

    result = model.transcribe(fileName)
    os.remove(fileName)
    return result

def format_timestamp(seconds):
    """Converts seconds to SRT timestamp format (HH:MM:SS,mmm)"""
    millis = int(round(seconds * 1000))
    return str(datetime.timedelta(milliseconds=millis))

def createSrt(segments):
    srt_file = ""
    for i, segment in enumerate(segments, start=1):
        srt_file += (str(i) + '\n')
        srt_file += (format_timestamp(segment['start']) + ' --> ' + format_timestamp(segment['end']) + '\n')
        srt_file += (segment['text'] + '\n\n')  # Two newlines for separation

    return srt_file

def main():
    st.header("Audio transcribing App with Whisper!")

    # Display HTML content
    st.components.v1.html(
        """
        <p>Upload an audio file for processing:</p>
        """
    )

    uploaded_file = st.file_uploader("Choose an audio file", type=["mp3", 'mp4', "mpeg", "mpga", "m4a", "wav", "webm"])

    if uploaded_file is not None:
        data = {"file": uploaded_file}

        extension = uploaded_file.name.split('.')[-1]
        timeStamp = int(time.time() * 100)
        fileName = f'temp-{timeStamp}.{extension}'

        result = feedTheModel(fileName, uploaded_file.getbuffer())

        st.subheader('here is the detected text!')
        st.success(result['text'])
        data = createSrt(result['segments'])

        st.subheader('and here is your proccessed srt file!🎉')
        st.download_button('Download!📥', data=data, file_name=f"{uploaded_file.name.split('.')[0]}.srt", on_click=None)
        # st.success(f"Processing result: {result['segments']}")
        
        return

        # else:
        #     # Handle errors
        #     # error_message = response.json().get("error", "Unknown error")
        #     st.error(f"Error: {response = }")

def callback():
    st.link_button('this code is in github!', "https://github.com/mahan-gh/pechpech")

if __name__ == "__main__":
    main()