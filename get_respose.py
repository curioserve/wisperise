import openai
import json
import pandas as pd
API_KEY = ""
# Initialize the client with your API key
client = openai.OpenAI(api_key=API_KEY)

import requests
import json

def get_word_info(api_key, word):
    # Construct the prompt for Gemini
    prompt = f"Define the word '{word}' and provide five example sentences using the word.(give response as json)"
    
    # Define the Gemini API URL
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent?key=" + api_key

    # Headers for the request
    headers = {
        "Content-Type": "application/json",
    }

    # Payload for the request
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    # Send the request to Gemini
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # Check the response status code
    if response.status_code == 200:
        # Parse and return the JSON response
        response_json = response.json()
        info_dict = response_json['results'][0]['parts'][0]['text']
        return json.loads(info_dict)
    else:
        # Handle failure response
        print(f"Failed to get response. Status code: {response.status_code}")
        print(f"Response: {response.text}")
        return None




def process_words_from_csv(csv_file_path):
    # Read the CSV file into a pandas DataFrame (with one word per line)
    words_df = pd.read_csv(csv_file_path)
    
    # Convert the 'Words' column into a list
    words = words_df['Words'].tolist()

    # Initialize a dictionary to hold word information
    word_info_dict = {}

    # Process each word in the list
    for word in words:
        word = word.strip()  # Remove any extra spaces
        if word:  # Only process non-empty words
            try:
                word_info = get_word_info(word)
                word_info_dict[word] = word_info
            except Exception as e:
                print(f"Error processing word '{word}': {e}")

    return word_info_dict

def dict_to_tts_string(word_info_dict):
    tts_text = ""

    # Loop through each word and its details in the dictionary
    for word, info in word_info_dict.items():
        definition = info.get('definition', 'No definition available.')
        example_sentences = info.get('example_sentences', [])

        # Construct the string for TTS
        tts_text += f"Word: {word}\n"
        tts_text += f"Definition: {definition}\n"
        tts_text += "Example sentences:\n"
        for sentence in example_sentences:
            tts_text += f"- {sentence}\n"
        tts_text += "\n"  # Add an extra newline between entries

    return tts_text

# Example usage
csv_file_path = "word_list.csv"  # Path to your CSV file with comma-separated words
word_info_dict = process_words_from_csv(csv_file_path)

# Save the result dictionary to a JSON file if needed
with open("word_info.json", "w") as json_file:
    json.dump(word_info_dict, json_file, indent=4)