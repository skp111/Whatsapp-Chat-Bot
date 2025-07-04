import pyautogui                         # For GUI automation like mouse and keyboard control
import time                              # For adding delays (sleep)
import pyperclip                         # For copying and pasting clipboard text
import google.generativeai as genai      # To use Google's Gemini AI model
from datetime import datetime            # To work with current date and time
import keyboard                          # use keyboard function

pyautogui.click(1293, 1049)              # Click on Chrome icon if prseent(or any window at that position

while True:                              # run continuously
    # print(pyautogui.position())        # Uncomment to print cursor corrdinated(X,Y)

    keyboard.wait('Ctrl')                 # Detect if Ctrl key is pressed then do the work            

    pyautogui.moveTo(701, 267)               # Move cursor to the start position of text
    pyautogui.mouseDown()                    # Press and hold the mouse button
    time.sleep(0.5)                          # Small pause to ensure stability
    pyautogui.moveTo(1885, 911, duration=1.0)# Drag the mouse to end position over 1 second
    pyautogui.mouseUp()                      # Release the mouse button to complete text selection
    time.sleep(0.5)                          # Let selection settle before copying

    pyautogui.hotkey('ctrl', 'c')            # Press Ctrl+C to copy selected text
    time.sleep(0.2)                          # Wait briefly for clipboard to update

    chat_history = pyperclip.paste()         # Get the copied text from clipboard

    pyautogui.click(953, 977)                # Click in the input box or desired area
    time.sleep(0.2)                          # Small pause before next action

    print(chat_history)                      # Print the copied chat history (for debugging)

    def is_last_message_from_another(last_message):
        if last_message:                                  # check if message is there or empty
            return not last_message.startswith('꧁☯︎Ⓢ︎Ⓐ︎Ⓜ︎Ⓔ︎Ⓔ︎Ⓡ︎☯︎꧂')  # Check if last message does not starts with ꧁☯︎Ⓢ︎Ⓐ︎Ⓜ︎Ⓔ︎Ⓔ︎Ⓡ︎☯︎꧂
        return False                                      # if message empty then return False

    def generate_chat(command):  # Function to process user queries using Gemini AI
        genai.configure(api_key='{Your API Key}')  # Set Gemini API key
        model = genai.GenerativeModel(model_name='gemini-2.0-flash')  # Load the Gemini model
        prompt = f"""
                    Act as Sameer, an Indian who speaks Hindi and English and like hindi jokes,
                    watching movies, listening songs and playing games.
                    You’re replying in a natural tone like a friend in a chat and give on to the point reply.

                    Here is the chat history received:
                    "{command}"

                    Now, reply as Sameer in — short, friendly, relevant, and casual by undertsanding from chat history.
                    Avoid unnecessary explanation. Be concise and text (message only) avoid this type of
                    starting of message '[5:30 PM, 6/16/2025]' it is an example """  # Prompt to guide AI reply tone
        response = model.generate_content(prompt)  # Generate response using Gemini
        return response.text  # Return the response text

    now = datetime.now()                     # Get current date and time
    year = now.year                          # Extract the year
    last_message=chat_history.strip().split(f"/{year}] ")[-1]  # Get the last message

    if is_last_message_from_another(last_message):     # If last message is from Another person

        ai_response = generate_chat(chat_history)      # Generate AI reply for the chat history
        pyperclip.copy(ai_response)                    # Copy AI response to clipboard

        pyautogui.click(953, 977)                      # Click back in the chat input box
        time.sleep(0.2)                                # Small pause

        pyautogui.hotkey('ctrl', 'v')                  # Paste the response
        time.sleep(0.2)                                # Small pause

        pyautogui.press('enter')                       # Press Enter to send the message