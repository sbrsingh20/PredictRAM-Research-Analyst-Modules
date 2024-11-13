import streamlit as st
import pandas as pd

# Load the user list from the Excel file
def load_user_list(file_path):
    df = pd.read_excel(file_path)
    return df

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

            # Check if the user data contains a 'video_id' column
            if 'video_id' in user_data.columns:
                video_ids = user_data['video_id'].tolist()

                # Display the videos
                for video_id in video_ids:
                    st.subheader(f"Video ID: {video_id}")
                    video_embed = embed_youtube_video(video_id)
                    st.markdown(video_embed, unsafe_allow_html=True)

            else:
                st.error("The Excel file must contain a 'video_id' column.")
        else:
            st.error("Incorrect username or password.")
    else:
        st.info("Please enter your username and password to continue.")

if __name__ == "__main__":
    main()
