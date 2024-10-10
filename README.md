---
title: lablabAI-O1A1-Learning-Assistant
emoji: 👁
colorFrom: purple
colorTo: blue
sdk: streamlit
sdk_version: 1.39.0
app_file: app.py
pinned: false
---

Here’s the updated `README.md` file based on the provided details:

---

# lablabAI-O1A1-Learning-Assistant

## Welcome to Team O1A1 Learning Assistant!  

This AI-powered educational tool is designed to help users with their learning-related questions, tailored to their learning level. Whether you're a child, a teenager, or an adult with minimal knowledge, the assistant provides step-by-step guidance to help you grasp concepts in an easy-to-understand manner.

The app was developed as part of the [lablab.ai Reasoning with o1 Hackathon](https://lablab.ai/) by team O1A1 and is hosted on Hugging Face. You can access the application [here](https://huggingface.co/spaces/Sumayyea/CodeMasterAI).

## How It Works

1. **Select your learning level.**
   - Options include: 
     - 5-12 years old
     - Teenager
     - Adult with minimal knowledge
     
2. **Enter a question about a concept or topic you need help with.**  
   - Below are some examples for guidance:

   - **Example 1**  
     - **Select:** 5-12 year old learning level.  
     - **Provide question 1:** Help me with Parts of Speech for Grade VI. Think step-by-step.  
     - **Provide question 2:** How many Rs are in the word 'strawberry'? Think step-by-step.

   - **Example 2**  
     - **Select:** Teenager learning level.  
     - **Provide question 1:** Explain how to solve a simple linear equation, like 2x + 3 = 7. Think step-by-step.  
     - **Provide question 2:** How do you calculate compound interest for a principal of $1000 at a 5% annual interest rate over 2 years? Explain step-by-step.

   - **Example 3**  
     - **Select:** Adult with minimal knowledge learning level.  
     - **Provide question 1:** What is the difference between RAM and ROM? Explain step-by-step.  
     - **Provide question 2:** How does the internet work? Explain it in simple terms step-by-step.

3. **Press the 'Get Help' button** to receive a response.  
   - The assistant will provide a step-by-step explanation based on your question and learning level.

4. **Save your response.**  
   - You can save the initial response as a PDF for later use.
   
5. **Request more help if needed.**  
   - If the initial explanation is not enough, press the 'I need more help' button for a more detailed response.

6. **Save the detailed response.**  
   - You can also save the detailed response as a PDF for future reference.

## Features

- Step-by-step learning assistance based on user-specified learning levels
- Personalized responses for different age groups
- Ability to save responses as PDFs
- Simple, user-friendly interface

## Tech Stack

- **Streamlit**: For building the user interface
- **OpenAI API**: For generating the AI-powered responses
- **FPDF**: For creating downloadable PDFs

## Getting Started

### Prerequisites

To run this app locally, you will need:

- Python 3.x
- pip (Python package installer)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/lablabAI-O1A1-Learning-Assistant.git
   ```

2. Navigate to the project directory:
   ```bash
   cd lablabAI-O1A1-Learning-Assistant
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the application:
   ```bash
   streamlit run app.py
   ```

2. Open your browser and go to `http://localhost:8501` to access the application.

## Files

- **app.py**: The main application code.
- **requirements.txt**: List of required Python dependencies.

## Requirements

- **Streamlit**: For building and running the app.
- **OpenAI**: API integration for generating AI-based responses.
- **FPDF**: To generate downloadable PDFs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to open an issue or submit a pull request if you'd like to contribute!

---

This updated README incorporates all the instructions and features of your app. You can customize further based on additional details.
