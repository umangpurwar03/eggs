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
    uploaded_file = st.sidebar.file_uploader("Upload a video file:", type=["mp4", "avi", "mov"])

    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Save the uploaded file to a temporary location
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_file.read())

        # Run the object detection function and display the output
        detection_results = detect_objects(tfile.name, st.empty())
        st.video(uploaded_file)
        st.write(detection_results)

    # Add a button to toggle the webcam
    use_webcam = st.sidebar.checkbox("Use Webcam")

    # Check if the webcam option is selected
    if use_webcam:
        # Get the index of the webcam device
        webcam_index = 0

        # Run the object detection function and display the output
        detection_results = detect_objects(webcam_index, st.empty())
        st.write(detection_results)

# Run the main function
if __name__ == "__main__":
    main()




