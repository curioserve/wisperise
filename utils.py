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