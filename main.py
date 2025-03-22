def display_choices(choices, choice_type):
    print(f"\nAvailable {choice_type}s:")
    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice}")

def get_user_choice(choices, choice_type):
    while True:
        try:
            choice_index = int(input(f"Enter the number for your desired {choice_type}: ")) - 1
            if 0 <= choice_index < len(choices):
                return choices[choice_index]
            else:
                print(f"Invalid {choice_type} number. Please choose from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def format_vibe_prompt(vibe_name, vibes_data):
    vibe_content = vibes_data.get(vibe_name)
    if vibe_content:
        return "\\n\\n".join(vibe_content) # join vibe lines with double newline
    return None

import datetime
import os

def generate_filename():
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"output_{timestamp}.wav"

from requests import Session
import json

session = Session()

def send_request(text: str, voice: str, vibe_prompt: str):
    url = "https://www.openai.fm/api/generate"
    boundary = "----WebKitFormBoundarya027BOtfh6crFn7A"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "Content-Type": f"multipart/form-data; boundary={boundary}",
        "Accept": "*/*",
        "Origin": "https://www.openai.fm",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.openai.fm/worker-444eae9e2e1bdd6edd8969f319655e70.js",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i"
    }

    data = []
    for name, value in [
        ("input", text),
        ("prompt", vibe_prompt),
        ("voice", voice.lower()),
        ("vibe", "null")
    ]:
        data.append(f"--{boundary}")
        data.append(f'Content-Disposition: form-data; name="{name}"\r\n') # Added \r\n here
        data.append(value)
    data.append(f"--{boundary}--")
    body = "\r\n".join(data).encode('utf-8') # Join with \r\n and encode to utf-8

    try:
        response = session.post(url, headers=headers, data=body)
        response.raise_for_status()
        if "audio/wav" in response.headers["Content-Type"]:
            audio_content = response.content
            filename = generate_filename()
            with open(filename, "wb") as f:
                f.write(audio_content)
            print(f"Audio saved to {filename}")
            return audio_content
        else:
            return None
    except Exception as e:
        print(e)

def load_voices():
    try:
        with open("voices.json") as f:
            return json.load(f)["voices"]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def load_vibes():
    try:
        with open("vibes.json") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def main():
    voices = load_voices()
    vibes_data = load_vibes()
    vibe_choices = list(vibes_data.keys())

    display_choices(voices, "voice")
    selected_voice = get_user_choice(voices, "voice")

    display_choices(vibe_choices, "vibe")
    selected_vibe_name = get_user_choice(vibe_choices, "vibe")

    vibe_prompt = format_vibe_prompt(selected_vibe_name, vibes_data)
    if vibe_prompt is None:
        print("Vibe prompt not found. Using default prompt.")
        vibe_prompt = "Voice Affect: Calm, composed, and reassuring; project quiet authority and confidence.\\n\\nTone: Sincere, empathetic, and gently authoritative—express genuine apology while conveying competence.\\n\\nPacing: Steady and moderate; unhurried enough to communicate care, yet efficient enough to demonstrate professionalism.\\n\\nEmotion: Genuine empathy and understanding; speak with warmth, especially during apologies (\\\"I'm very sorry for any disruption...\\\").\\n\\nPronunciation: Clear and precise, emphasizing key reassurances (\\\"smoothly,\\\" \\\"quickly,\\\" \\\"promptly\\\") to reinforce confidence.\\n\\nPauses: Brief pauses after offering assistance or requesting details, highlighting willingness to listen and support."


    text = input("Enter text: ")
    if text:
        send_request(text, selected_voice, vibe_prompt)
    else:
        print("No text entered. Exiting.")

if __name__ == "__main__":
    main()
