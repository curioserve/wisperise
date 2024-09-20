import torch
from TTS.api import TTS

def text_to_speech_with_cloning(text, speaker_wav, output_path="output.wav"):
    # Check if CUDA is available, use GPU if possible
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    # Initialize TTS model with voice cloning capabilities
    tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2").to(device)
    
    # Convert the input text to speech, using the provided speaker_wav and save the output
    tts.tts_to_file(text=text, speaker_wav=speaker_wav, language="en", file_path=output_path)
    
    print(f"Audio saved to {output_path}")
    return output_path

# Example usage
output_file = text_to_speech_with_cloning("Word: rack\nDefinition: a framework, typically with rails, bars, hooks, or pegs, on which items can be displayed, stored, or hung\nExample sentences:\n- I hung my coat on the rack by the door.\n- The store had a rack of gardening tools for sale.\n- She displayed her collection of hats on a rack in her bedroom.\n- The bike rack was full, so I had to find another place to park my bicycle.\n- The kitchen rack was overflowing with pots and pans.\n\nWord: nerve racking\nDefinition: causing a person to feel very tense, anxious, and stressed\nExample sentences:\n- The job interview was nerve-racking, but she managed to remain composed.\n- Waiting for the exam results is always nerve-racking.\n- His constant procrastination is nerve-racking for his colleagues.\n- The suspenseful movie was so nerve-racking that I couldn't sit still.\n- Driving in heavy traffic can be nerve-racking for some people.\n\nWord: exhilarating\nDefinition: causing strong feelings of excitement and happiness\nExample sentences:\n- The roller coaster ride was exhilarating, with loops and twists that sent a thrill through her.\n- Taking a refreshing swim in the cool ocean on a hot summer day can be quite exhilarating.\n- Winning the championship game was an exhilarating moment for the team and their fans.\n- Skydiving for the first time is an exhilarating experience that many people find both terrifying and exhilarating.\n- The breathtaking view from the mountain peak was truly exhilarating, making the long hike worth every step.\n\nWord: venturing\nDefinition: the act or an instance of stepping out or going beyond; foraging, exploration\nExample sentences:\n- They were venturing into uncharted territory in search of the lost city.\n- As a group, we enjoyed venturing through the dense forest to discover hidden waterfalls.\n- The young entrepreneur was excited about venturing into a new business opportunity.\n- Venturing outside of her comfort zone, she decided to try bungee jumping for the first time.\n- Despite the risks, the team was determined to continue venturing farther into the wilderness.\n\nWord: barely\nDefinition: only just; almost not\nExample sentences:\n- She barely passed the exam with a score of 60%.\n- The hikers barely made it to the summit before the storm hit.\n- I could barely hear what he was saying over the loud music.\n- After running a marathon, she could barely walk due to exhaustion.\n- The old car barely made it up the steep hill.\n\nWord: etched in my mind\nDefinition: Remembered clearly and vividly; deeply ingrained in one's memory.\nExample sentences:\n- The image of her smiling face was etched in my mind long after she had left.\n- The ominous warning about the dangerous trails was etched in my mind as I hiked through the forest.\n- The haunting melody of the song stayed etched in my mind, playing on repeat throughout the day.\n- The taste of that delicious meal was so good that it was etched in my mind for weeks.\n- The memory of their heartfelt goodbye was etched in my mind, making me miss them even more.\n\nWord: milestone\nDefinition: A milestone is a significant event or stage in the development or progress of something.\nExample sentences:\n- Graduating from college was a major milestone in Sarah's life.\n- The company celebrated reaching the milestone of one million customers.\n- Learning to ride a bike is a common milestone for young children.\n- Successfully completing the project ahead of schedule was a significant milestone for the team.\n- Buying their first home together marked a special milestone in their relationship.\n\nWord: overwhelmed\nDefinition: defeated completely; too much work or emotion to handle\nExample sentences:\n- She felt overwhelmed by all the responsibilities piling up at work.\n- After the unexpected news, he was overwhelmed with emotion.\n- The sheer number of people at the event overwhelmed her senses.\n- Facing multiple deadlines, she became overwhelmed with anxiety.\n- The scale of the disaster left the rescue team feeling overwhelmed.\n\nWord: put on\nDefinition: to dress oneself in specified clothing; to apply or make use of\nExample sentences:\n- I need to put on my coat before going outside.\n- She decided to put on some makeup for the party.\n- He always puts on his favorite music while he works.\n- They will put on a play at the school next week.\n- Don't forget to put on sunscreen before going to the beach.\n\nWord: psyched\nDefinition: excited, enthusiastic, or pumped up about something\nExample sentences:\n- I'm psyched about the concert this weekend!\n- She was psyched to start her new job.\n- Are you psyched for the big game tomorrow?\n- We're all psyched for the upcoming vacation.\n- He got psyched when he found out he won the contest.\n\n", "charlie_clone_voice-vocals.wav", "cloned_output_charlie.wav")


#The attention mask is not set and cannot be inferred from input because pad token is same as eos token. As a consequence, you may observe unexpected behavior. Please pass your input's `attention_mask` to obtain reliable results.