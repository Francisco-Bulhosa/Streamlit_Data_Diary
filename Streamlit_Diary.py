import streamlit as st
import os

# Function to display the topic page
def display_topic_page():
    st.title(f"{st.session_state.selected_topic} Pages")
    
    # List of pages inside the selected topic
    path = "summaries"
    page_files = [file for file in os.listdir(path) if file.startswith(st.session_state.selected_topic) and file.endswith(".txt")]

    
    # Debug: Print the list of page files
   ### st.write("Debug - Page Files:", page_files)
    
    for page_name in page_files:
        if st.button(page_name[:-4]):  # Remove the file extension
            st.session_state.page = "summary_page"
            st.session_state.selected_page = page_name  # Store the full filename, including the topic

# Function to display the summary page
def display_summary_page():
    st.title(f"Summary of {st.session_state.selected_page[:-4]}")  # Remove the file extension
    
    # Reading the summary
    file_path = f"summaries/{st.session_state.selected_page}"
    
    with open(file_path, "r") as file:
        summary = file.read()

    st.markdown(summary)

    # Edit button
    if st.button("Edit Summary"):
        st.session_state.page = "edit_summary"


# Function to display the add summary page
def display_add_summary_page():
    st.title("Add Web Summary")
    
    # Topics
    topics = ["Data Analysis", "Deep Learning", "Generative AI", "Tutorials", "Interactive Sites"]
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


def display_edit_summary_page():
    st.title(f"Edit Summary: {st.session_state.selected_page}")
    
    # Reading the existing summary
    file_path = f"summaries/{st.session_state.selected_topic}/{st.session_state.selected_page}.txt"
    with open(file_path, "r") as file:
        lines = file.readlines()
        url = lines[0].strip().split(": ")[1]
        existing_summary = lines[1].strip().split(": ")[1]
    
    # Input fields pre-filled with existing values
    url = st.text_input("Enter the URL:", value=url)
    summary = st.text_area("Enter the summary:", value=existing_summary)
    
    # Button to save the changes
    if st.button("Save Changes"):
        # Writing the updated summary to the file
        with open(file_path, "w") as file:
            file.write(f"URL: {url}\nSummary: {summary}\n")
        
        st.success("Summary updated successfully!")
        st.session_state.page = "summary_page"  # Redirect back to the summary page


# Home Page
st.title("My Data Science Diary!")
st.markdown("by Francisco Bulhosa Ferreira")
st.markdown("---") 
st.markdown("Add New Summaries or search through the Topics!")
if st.button("Add New Summary"):
    st.session_state.page = "add_summary"

# List of Topics
st.header("Topics")
topics = ["Data Analysis", "Deep Learning", "Generative AI", "Tutorials", "Interactive Sites"]
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
elif st.session_state.page == "edit_summary":  
    display_edit_summary_page()

# Note
st.markdown("---") 
st.markdown("Note: All summaries are AI Generated.")