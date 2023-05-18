import streamlit as st
import cv2
from FinalVD_function import detect_objects
import tempfile

# Set the title and background color of the web app
st.set_page_config(page_title="Object Detection Web App", page_icon=":eyes:", layout="wide", initial_sidebar_state="expanded")
st.markdown(
    f"""
    <style>
        .reportview-container {{
            background: #F5F5F5
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Define the main function that runs the app
def main():

    st.title("Object Detection Web App")

    # Add a file uploader widget to the sidebar
    # st.sidebar.title("Upload video")
    # uploaded_file = st.sidebar.file_uploader("Upload a video file:", type=["mp4", "avi", "mov"])
    uploaded_file = st.file_uploader("Upload file")


    # Check if a file has been uploaded
    if uploaded_file is not None:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_file.read())
        # vf = cv2.VideoCapture(tfile.name)
        # print(vf)
        # Run the object detection function and display the output
        detection_results = detect_objects(tfile.name,st.empty())
        st.video(uploaded_file)
        st.write(detection_results)

# Run the main function
if __name__ == "__main__":
    main()
