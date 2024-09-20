from get_response import *


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