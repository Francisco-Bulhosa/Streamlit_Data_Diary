import streamlit as st
import os

# Function to display the topic page
def display_topic_page():
    st.title(f"{st.session_state.selected_topic} Pages")
    
    # List of pages inside the selected topic
    path = "summaries"
    page_files = [file[:-4] for file in os.listdir(path) if file.startswith(st.session_state.selected_topic) and file.endswith(".txt")]
    
    for page_name in page_files:
        if st.button(page_name):
            st.session_state.page = "summary_page"
            st.session_state.selected_page = page_name

# Function to display the summary page
def display_summary_page():
    st.title(f"Summary of {st.session_state.selected_page}")
    
    # Reading the summary
    file_path = f"summaries/{st.session_state.selected_topic}/{st.session_state.selected_page}.txt"
    with open(file_path, "r") as file:
        summary = file.read()
    
    st.markdown(summary)

# Function to display the add summary page
def display_add_summary_page():
    st.title("Add Web Summary")
    
    # Topics
    topics = ["Data Analysis", "Deep Learning", "Generative AI"]
    selected_topic = st.selectbox("Select Topic:", topics)
    page_name = st.text_input("Enter Page Name:")
    url = st.text_input("Enter the URL:")
    summary = st.text_area("Enter the summary:")
    
    # Button to add the summary
    if st.button("Add Summary"):
        # File path
        file_path = f"summaries/{selected_topic}_{page_name}.txt"
        
        # Creating directory if not exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Writing to the file
        with open(file_path, "w") as file:
            file.write(f"URL: {url}\nSummary: {summary}\n")
        
        st.success("Summary added successfully!")

# Home Page
st.title("Web Summary Diary")
if st.button("Add New Summary"):
    st.session_state.page = "add_summary"

# List of Topics
st.header("Topics")
topics = ["Data Analysis", "Deep Learning", "Generative AI"]
for topic in topics:
    if st.button(topic):
        st.session_state.page = "topic_page"
        st.session_state.selected_topic = topic


# Navigation between pages
if "page" not in st.session_state:
    st.session_state.page = "home_page"

if st.session_state.page == "topic_page":
    display_topic_page()
elif st.session_state.page == "summary_page":
    display_summary_page()
elif st.session_state.page == "add_summary":
    display_add_summary_page()

# Note
st.markdown("---")  # Optional horizontal line
st.markdown("Note: All summaries are AI Generated.")