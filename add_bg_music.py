from pydub import AudioSegment
import simpleaudio as sa

def combine_audio(vocal_path, music_path, output_path):
    # Load the vocal track (wav) and the background music (mp3)
    vocal = AudioSegment.from_wav(vocal_path)
    music = AudioSegment.from_mp3(music_path)
    
    # Loop the background music if it's shorter than the vocal track
    while len(music) < len(vocal):
        music += music  # Repeat the background music
    
    # Trim the background music to the length of the vocal track
    music = music[:len(vocal)]
    
    # Combine the two audio tracks: overlay music over vocal
    combined = vocal.overlay(music)
    
    # Export the result as a new file
    combined.export(output_path, format="wav")
    
    # Play the new audio file
    wave_obj = sa.WaveObject.from_wave_file(output_path)
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Wait until the audio finishes playing

# Example usage
combine_audio("cloned_output_charlie.wav", "/Users/ali/Desktop/mesmerise/spotifydown.com - Gnossienne No. 3.mp3", "combined_output_charlie.wav")
