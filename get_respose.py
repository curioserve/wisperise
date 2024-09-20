import openai
import json
import pandas as pd
API_KEY = ""
# Initialize the client with your API key
client = openai.OpenAI(api_key=API_KEY)

def get_word_info(word):
    # Construct the prompt for ChatGPT
    prompt = f"Define the word '{word}' and provide five example sentences using the word.(give response as json)"

    # Use the client to create a chat completion
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Specify the model, adjust as necessary
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    # Extract and return the response text
    info_dict = response.to_dict()['choices'][0]['message']['content']
    return json.loads(info_dict)


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