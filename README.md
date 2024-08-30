# Celebrity Search Application

This project is a Streamlit-based web application that leverages OpenAI's GPT model to provide information about celebrities. The application allows users to search for a celebrity and retrieve information about them, along with their notable achievements.

## Features

- **Celebrity Information Retrieval:** Enter a celebrity's name to receive a detailed description.
- **Achievements Listing:** Automatically generates a list of five major achievements for the selected celebrity.
- **Memory-Enhanced Interaction:** The application remembers previous inputs and interactions during a session, allowing for a more personalized user experience.

## Tech Stack

- Python
- Streamlit: For building the web interface.
- LangChain: For managing prompt templates and chaining LLM interactions.
- OpenAI API: Powered by GPT-3.5 for natural language processing.

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- OpenAI API Key

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/shiivam-saini/celebrity-search.git
   cd celebrity-search

2.**Install required packages**
 pip install -r requirements.txt

3.**Set Up Environment Variables:**

Replace openai_key with your actual OpenAI API key in the constants.py file or directly in your environment variables.

openai_key = "your_openai_api_key"
