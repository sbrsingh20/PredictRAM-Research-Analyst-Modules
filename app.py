import streamlit as st
import pandas as pd

# Load user data from the Excel file
def load_user_data(file_path):
    df = pd.read_excel(file_path)
    return df

# Function to extract video ID from a YouTube link
def extract_video_id(youtube_url):
    if "watch?v=" in youtube_url:
        return youtube_url.split("watch?v=")[1].split("&")[0]
    return None

# Function to embed a YouTube video
def embed_youtube_video(video_id):
    return f'<iframe width="560" height="315" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allowfullscreen></iframe>'

# Main function to run the Streamlit app
def main():
    # Load user data
    user_data = load_user_data('user.xlsx')

    # Authentication input
    st.sidebar.title("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        # Check credentials
        if username in user_data['name'].values:
            user_row = user_data[user_data['name'] == username]
            if user_row['password'].values[0] == password:
                st.success("Logged in successfully!")

                # Hardcoded video URLs
                video_urls = [
                    "https://www.youtube.com/watch?v=80_EV6L8V9s",
                    "https://www.youtube.com/watch?v=T8msaNr2hrM",
                    # Add more video URLs as needed
                ]

                # Display the videos
                for video_url in video_urls:
                    video_id = extract_video_id(video_url)
                    if video_id:
                        st.subheader(f"Video URL: {video_url}")
                        video_embed = embed_youtube_video(video_id)
                        try:
                            st.markdown(video_embed, unsafe_allow_html=True)
                        except Exception as e:
                            st.error(f"An error occurred while loading the video: {e}")
                    else:
                        st.error("Invalid video URL format.")
            else:
                st.error("Incorrect password.")
        else:
            st.error("Username not found.")

    else:
        st.info("Please enter your username and password to continue.")

if __name__ == "__main__":
    main()
