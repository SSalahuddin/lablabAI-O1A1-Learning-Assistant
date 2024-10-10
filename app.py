import streamlit as st
from openai import OpenAI
import os
from fpdf import FPDF
import re

# AIML API settings
aiml_api_key = os.getenv("AIML_API_KEY")  # Fetch the API key from Hugging Face secrets
base_url = "https://api.aimlapi.com/"

# Initialize the AIML API client
client = OpenAI(api_key=aiml_api_key, base_url=base_url)

# Function to generate response using AIML API
def generate_response(user_input, user_category):
    # Create the prompt based on user input and category
    prompt = f"As a {user_category}, I need help with: {user_input}. Please provide a step-by-step explanation."
    
    # Send the prompt to the AIML API's "o1-mini" model
    try:
        chat_completion = client.chat.completions.create(
            model="o1-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000,
        )
        response = chat_completion.choices[0].message.content
        return response
    except Exception as e:
        st.error(f"Error occurred: {str(e)}")
        return None

# Function to clean up the text (remove or replace unsupported characters)
def clean_text_for_pdf(text):
    # Remove markdown symbols like ##, **, and ---
    text = re.sub(r'\*\*', '', text)  # Remove all occurrences of **
    text = re.sub(r'##', '', text)    # Remove all occurrences of ##
    text = re.sub(r'---', '', text)    # Remove all occurrences of ##

    # Replace unsupported characters like the arrow (→) with equivalent text symbols
    replacements = {
        "…": "...",  # Ellipsis
        "—": "-",    # Em dash
        "–": "-",    # En dash
        "‘": "'",    # Left single quotation
        "’": "'",    # Right single quotation
        "“": '"',    # Left double quotation
        "”": '"',    # Right double quotation
        "•": "-",    # Bullet point
        "→": "->",   # Arrow (replace with simple '->')
        # Add more replacements as needed
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    # Remove extra empty lines (reduce multiple newlines to a single newline)
    text = re.sub(r'\n\s*\n+', '\n\n', text)
    
    # Trim leading and trailing newlines
    text = text.strip()
    
    return text

# Custom class to handle PDF layout improvements
class CustomPDF(FPDF):
    def header(self):
        # Add a custom title in the header
        self.set_font("Arial", 'B', 12)
        self.cell(0, 10, 'Team O1A1 Learning AI Assistant - Response', align='C', ln=True)
        self.ln(5)

    def footer(self):
        # Add a page number in the footer
        self.set_y(-15)
        self.set_font("Arial", 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

# Function to create a PDF from the AI response
def create_pdf(content, file_name):
    pdf = CustomPDF()
    pdf.add_page()
    
    # Set font and spacing for the body content
    pdf.set_font("Arial", size=12)
    
    # Add margins for better layout
    pdf.set_left_margin(10)
    pdf.set_right_margin(10)
    
    # Clean content before adding to the PDF
    cleaned_content = clean_text_for_pdf(content)
    
    # Split content into paragraphs and add to PDF with proper wrapping
    pdf.multi_cell(0, 10, txt=cleaned_content)

    # Save the PDF to a file-like object (in memory)
    pdf_output = pdf.output(dest="S").encode("latin1")
    
    return pdf_output

# Streamlit app layout
st.set_page_config(page_title="Lablab.Ai O1 Hackathon Learning Assistant", page_icon="🤖")

# Introduction
st.title("Lablab.Ai O1 Hackathon Learning Assistant 🤖")
st.write("Welcome to Team O1A1 Learning Assistant! Get help with your learning-related questions, tailored to your learning level.")

# Adding spacing between sections
st.markdown("### How it works:")
st.write("1. Select your **learning level**.")
st.write("2. Enter a **question about a concept or topic** you need help with. Below are examples for guidance:")
# Use st.markdown for better formatting with Markdown
st.markdown("""#### Example 1: 
- **Select:** 5-12 year old learning level.  
- **Provide question 1:** Help me with Parts of Speech for Grade VI. Think step-by-step.
- **Provide question 2:** How many Rs are in the word 'strawberry'? Think step-by-step.
#### Example 2:
- **Select:** Teenager learning level.  
- **Provide question 1:** Explain how to solve a simple linear equation, like 2x + 3 = 7. Think step-by-step.
- **Provide question 2:** How do you calculate compound interest for a principal of $1000 at a 5% annual interest rate over 2 years? Explain step-by-step.
#### Example 3:
- **Select:** Adult with minimal knowledge learning level.  
- **Provide question 1:** What is the difference between RAM and ROM? Explain step-by-step.
- **Provide question 2:** How does the internet work? Explain it in simple terms step-by-step.
""")
st.write("3. Press the **Get Help** button to get a response.")
st.write("4. You can **save the initial response as pdf** for later use.")
st.write("5. You can ask for more detailed help using **I need more help**.")
st.write("6. You can **save the detailed response as pdf** for later use.")


# Input section with clear labels
st.markdown("---")

# Using a container for better organization
with st.container():
    st.subheader("Your Query")

    # Category selection with a more user-friendly label
    category = st.selectbox(
        "Select your learning level:",
        ("5-12 year old", "Teenager", "Adult with minimal knowledge")
    )

    # Input area with a more detailed placeholder
    query = st.text_area("What do you need help with?", placeholder="Type your question about a concept or topic here...")

    # Store the responses to show them sequentially
    response = None
    more_response = None

    # Button to trigger response generation with loading spinner
    if st.button("Get Help"):
        if query:
            with st.spinner("Generating response..."):
                response = generate_response(query, category)
            st.markdown("### AI's Response:")
            if response:
                st.write(response)
                
                # Convert response to PDF and add a download button
                pdf_response = create_pdf(response, "O1A1_Learning_Assistant_Response.pdf")
                st.download_button(
                    label="Download AI's Response as PDF",
                    data=pdf_response,
                    file_name="O1A1_Learning_Assistant_Response.pdf",
                    mime="application/pdf"
                )
        else:
            st.warning("Please enter your question before asking for help.")
    
    # Button for additional help
    if st.button("I need more help"):
        if query:
            with st.spinner("Generating more detailed response..."):
                more_response = generate_response(f"{query}. Please explain it in more detail.", category)
            st.markdown("### Detailed Response:")
            if more_response:
                st.write(more_response)
                
                # Convert detailed response to PDF and add a download button
                pdf_detailed_response = create_pdf(more_response, "O1A1_Learning_Assistant_Detailed_Response.pdf")
                st.download_button(
                    label="Download Detailed Response as PDF",
                    data=pdf_detailed_response,
                    file_name="O1A1_Learning_Assistant_Detailed_Response.pdf",
                    mime="application/pdf"
                )
        else:
            st.warning("Please enter your question before asking for more help.")

# Add a footer or help section with more detailed information
st.markdown("---")
st.markdown("""
### Need More Assistance? 
We're here to help! If you're facing any issues or need further support, feel free to:

- **Refine Your Query**: Try rephrasing your question to be more specific for better results.
- **Visit Our Support Page**: [Team O1A1 Support](https://lablab.ai/event/strawberry-reasoning-with-o1/o1ai)

#### Quick Links:
- [Contact Us](https://lablab.ai/event/strawberry-reasoning-with-o1/o1ai): Get in touch for personalized assistance.

Thank you for choosing the O1A1 Learning Assistant. *Happy Learning!* 🎓
""")
