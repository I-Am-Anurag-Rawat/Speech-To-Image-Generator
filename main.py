import os
from speech_processor import SpeechProcessor
from image_generator import ImageGenerator

def main():
    print("Welcome to Speech-to-Image Generator!")
    print("Please speak a description of the image you want to generate...")
    
    # Initialize components
    speech_proc = SpeechProcessor()
    image_gen = ImageGenerator()
    
    # Record and process speech
    try:
        text = speech_proc.process_speech()
        if not text:
            print("Could not understand audio. Please try again.")
            return
            
        print(f"Recognized text: {text}")
        
        # Generate image
        output_path = image_gen.generate_image(text)
        if output_path:
            print(f"Image generated successfully at: {output_path}")
        else:
            print("Failed to generate image.")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()