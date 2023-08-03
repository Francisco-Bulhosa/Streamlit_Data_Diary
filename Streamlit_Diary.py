import streamlit as st
import os
import shutil
import json

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

    # Delete button
    if st.button("Delete Summary"):
        os.remove(file_path)  # Delete the file
        st.success("Summary deleted successfully!")
        st.session_state.page = "topic_page"  # Redirect back to the topic page


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
    st.title(f"Edit Summary: {st.session_state.selected_page[:-4]}")
    
    # Reading the existing summary
    file_path = f"summaries/{st.session_state.selected_page}"

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



# Function to display the graphic diary page
def display_graphic_diary_page():
    # Display Images
    st.title("Graphic Diary")

    # Display Images
    st.header("Gallery")
    image_directory = "graphic_diary"
    image_files = [file for file in os.listdir(image_directory) if file.endswith(('.png', '.jpg', '.jpeg'))]

    for image_file in image_files:
        image_path = f"{image_directory}/{image_file}"
        caption = metadata.get(image_file, {}).get("caption", "")
        category = metadata.get(image_file, {}).get("category", "")

        # Display the image with caption, category, and delete option
        st.image(image_path, caption=f"{caption} (Category: {category})", use_column_width=True)

        # Edit caption and category
        new_caption = st.text_input(f"Edit caption for {image_file}:", value=caption)
        new_category = st.text_input(f"Edit category for {image_file}:", value=category)
        if st.button(f"Save Changes for {image_file}"):
            metadata[image_file] = {"caption": new_caption, "category": new_category}
            with open(metadata_file, "w") as file:
                json.dump(metadata, file)
            st.success(f"Changes for {image_file} saved successfully!")

        # Delete button
        if st.button(f"Delete {image_file}"):
            os.remove(image_path)
            metadata.pop(image_file, None)  # Remove metadata entry
            with open(metadata_file, "w") as file:
                json.dump(metadata, file)
            st.success(f"Image {image_file} deleted successfully!")


# Function to display the search results page
def display_search_results_page():
    st.title(f"Search Results for: {st.session_state.search_query}")

    # Search through topics and pages
    st.header("Topic and Page Search Results:")
    path_to_summaries = "summaries"
    for topic in os.listdir(path_to_summaries):
        topic_path = os.path.join(path_to_summaries, topic)
        if os.path.isdir(topic_path):
            for page_file in os.listdir(topic_path):
                if page_file.endswith(".txt"):
                    page_path = os.path.join(topic_path, page_file)
                    with open(page_path, 'r') as file:
                        content = file.read()
                        if st.session_state.search_query.lower() in content.lower():
                            page_name = page_file[:-4] # Remove .txt extension
                            st.write(f"Found in topic: {topic}, page: {page_name}")

    # Search through images (implement based on your graphic diary page structure)



    # Upload Image
def upload_image():
    uploaded_image = st.file_uploader("Upload an image:", type=["jpg", "png", "jpeg"])
    if uploaded_image:
        # Save the uploaded image to a directory
        image_path = f"graphic_diary/{uploaded_image.name}"
        with open(image_path, "wb") as file:
            file.write(uploaded_image.read())
        st.success(f"Image {uploaded_image.name} uploaded successfully!")

    # Load metadata (captions and categories)
    metadata_file = "graphic_diary/metadata.json"
    if os.path.exists(metadata_file):
        with open(metadata_file, "r") as file:
            metadata = json.load(file)
    else:
        metadata = {}


# Home Page

search_query = st.text_input("Search:")


# Create a left column for navigation
left_column = st.sidebar
left_column.title("My Data Science Diary!")
left_column.markdown("by Francisco Bulhosa Ferreira")
left_column.markdown("---")
if search_query:
    st.session_state.page = "search_results"
    st.session_state.search_query = search_query

# Home Page Icon/Button
if left_column.button("Home"):
    st.session_state.page = "home_page"

left_column.header("Navigation")
if left_column.button("Add New Summary"):
    st.session_state.page = "add_summary"
if left_column.button("Upload Image"):
    st.session_state.page = "upload_image"
    st.header("Upload an Image to Graphic Diary")
    upload_image()  # Call the upload_image function

# List of Topics in left column
left_column.header("Topics")
topics = ["Data Analysis", "Deep Learning", "Generative AI", "Tutorials", "Interactive Sites", "Gallery"]
for topic in topics:
    if left_column.button(topic):
        st.session_state.page = "topic_page"
        st.session_state.selected_topic = topic

# Note at the bottom of the left side content
left_column.markdown("---")
left_column.markdown("Note: All summaries are AI Generated.")


# Navigation between pages (right side content)
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
elif st.session_state.page == "graphic_diary":
    display_graphic_diary_page()
elif st.session_state.page == "search_results":
    display_search_results_page()

