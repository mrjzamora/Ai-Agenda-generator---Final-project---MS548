import nltk  # NLTK is used for natural language processing tasks
from nltk.tokenize import sent_tokenize  # Sentence tokenization to break text into sentences
import tkinter as tk  # Tkinter for GUI creation
from tkinter import scrolledtext  # ScrolledText widget for text areas with a scrollbar
from tkinter import messagebox  # MessageBox for showing dialog boxes
import re  # Regular expressions for pattern matching in text

# Ensure necessary NLTK resources are downloaded
nltk.download('punkt')

# Define a comprehensive list of action verbs for agenda extraction
action_verbs = [
    'finalize', 'implement', 'execute', 'complete', 'prepare', 'develop', 'arrange', 'organize', 'submit', 'report',
    'decide', 'choose', 'select', 'determine', 'resolve', 'consider',
    'discuss', 'review', 'brainstorm', 'meet', 'confer', 'consult',
    'follow up', 'check', 'update', 'remind', 'schedule', 'plan', 'track', 'monitor',
    'require', 'need', 'demand', 'urge', 'ensure', 'insist', 'prioritize',
    'oversee', 'supervise', 'manage', 'lead', 'coordinate', 'delegate'
]

# Function to extract agenda points from text based on action verbs
def extract_agenda_points(text):
    """
    Extracts potential agenda points from the provided text based on the presence of predefined action verbs.
    Uses sentence tokenization to break down the text into individual sentences and regular expressions
    to identify sentences containing any of the specified action verbs.

    Args:
        text (str): The text from which to extract agenda points.

    Returns:
        list: A list of sentences that contain action verbs, which could serve as agenda points.
    """
    sentences = sent_tokenize(text)  # Break text into sentences
    agenda_points = []
    for sentence in sentences:
        # Check if any action verb is present in the sentence; use regex to ensure whole word matching
        if any(re.search(r'\b' + re.escape(verb) + r'\b', sentence, re.IGNORECASE) for verb in action_verbs):
            agenda_points.append(sentence)
    return agenda_points

# Function to generate the meeting agenda from user input
def generate_agenda():
    """
    Handles the button click event to generate the agenda.
    Retrieves the text from the input area, processes it to extract agenda points,
    and displays them in the output area.
    """
    input_text = text_input.get('1.0', tk.END)  # Get text from input widget
    if not input_text.strip():
        messagebox.showinfo("Input Error", "Please enter some text.")  # Show error if input is empty
        return
    agenda_items = extract_agenda_points(input_text)  # Extract agenda points from the text
    text_output.delete('1.0', tk.END)  # Clear the output area
    text_output.insert(tk.INSERT, "Proposed Meeting Agenda:\n")  # Insert the header for the agenda
    for item in agenda_items:
        text_output.insert(tk.INSERT, "- " + item + "\n")  # Insert each agenda item

# Set up the main GUI window
root = tk.Tk()
root.title("Meeting Agenda Generator")

# Label for input area
input_label = tk.Label(root, text="Enter Email Text:")
input_label.pack(pady=(10, 0))

# Text input area
text_input = scrolledtext.ScrolledText(root, width=70, height=10)
text_input.pack()

# Button to generate agenda
generate_button = tk.Button(root, text="Generate Agenda", command=generate_agenda)
generate_button.pack(pady=5)

# Label for output area
output_label = tk.Label(root, text="Generated Meeting Agenda:")
output_label.pack(pady=(10, 0))

# Text output area
text_output = scrolledtext.ScrolledText(root, width=70, height=10)
text_output.pack(pady=(0, 10))

# Start the GUI event loop
root.mainloop()
