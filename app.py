import streamlit as st
import pandas as pd

# Load the user list from the Excel file
def load_user_list(file_path):
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
    # Simple authentication
    st.sidebar.title("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    
    # Replace with your actual username and password
    correct_username = "user"
    correct_password = "password"
    
    if st.sidebar.button("Login"):
        if username == correct_username and password == correct_password:
            st.success("Logged in successfully!")
            
            # Load the user data
            user_data = load_user_list('user.xlsx')

            # Check if the user data contains a 'video_id' or 'video_url' column
            if 'video_url' in user_data.columns:
                video_urls = user_data['video_url'].tolist()

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
                st.error("The Excel file must contain a 'video_url' column.")
        else:
            st.error("Incorrect username or password.")
    else:
        st.info("Please enter your username and password to continue.")

if __name__ == "__main__":
    main()
