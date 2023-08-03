# Streamlit_Data_Diary

A Streamlit Diary where I regularly add new information on topics that interest me in the broad field of Data Science!

## Description

The Data Diary is a Streamlit-based web application that allows users to create, search, and organize summaries of web content into topics and pages. It also provides a gallery feature to upload and manage images. It's designed to replace web browser tabs by providing a convenient way to save and categorize web page summaries and images.

## Features

- **Home Page**: Browse through different topics, search for content, upload images, and navigate to summaries or add new ones.
- **Topic Pages**: View the list of pages within a selected topic and choose a specific page to view its summary.
- **Summary Pages**: Read and edit the detailed summary of the selected page. Delete options are also available.
- **Add Summary**: Easily add new summaries, including URL, page name, and summary text, and categorize them by topic.
- **Search**: Use the search bar to find content across summaries and images, based on text and metadata.


## Structure

- **Home Page**: Contains the search bar, image uploader, and buttons to navigate to the input fields (for adding new summaries) and a list of topics.
- **Topic Page**: Displays a list of page names inside the selected topic and allows users to select a page to view the summary.
- **Summary Page**: Displays the summary of the selected page with options to edit or delete.
- **Add Summary Page**: Allows users to add new summaries.
- **Search Results Page**: Displays the results of the search query.


## How to Run

1. Clone the repository:
   git clone https://github.com/your-username/Streamlit_Data_Diary.git

2. Navigate to the project directory:
   cd Streamlit_Data_Diary

3. Install the required dependencies:
   pip install streamlit

4. Run the Streamlit app:
   streamlit run Streamlit_Diary.py (in command prompt, etc)

5. The app will open on your browser at http://localhost:8501.

## Note

Please make sure to create the following directories within the project directory:
- **summaries**: to store the summary files

You may also adjust the code to your preferred directory structure.

## Contributing

Feel free to use this project as you see fit!
