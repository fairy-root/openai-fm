# OpenAI FM API

A Python implementation for interacting with the unofficial OpenAI FM text-to-speech service. This project provides a command-line interface to generate audio from text using a variety of voices and emotional vibes.

## Features

- **Voice Selection**: Choose from a list of available voices dynamically loaded from `voices.json`.
- **Vibe Customization**: Select from a wide range of vibes or emotional styles, loaded from `vibes.json`, to customize the voice output.
- **WAV Audio File Generation**: Saves the generated audio directly to a WAV file in the local directory.
- **Dynamic Prompt Formatting**: Utilizes vibe descriptions to format the prompt sent to the API, influencing the tone and style of the voice.
- **Easy-to-Use Interface**: Simple command-line prompts for text input, voice, and vibe selection.

## File Structure

- `main.py`: The main Python script containing the core implementation for interacting with the OpenAI FM API, including functions for sending requests, handling responses, and managing user input.
- `voices.json`: A JSON file listing the available voice options that can be used with the API.
- `vibes.json`: A JSON file containing configurations for various voice vibes or personalities, used to customize the audio output.

## Implementation Details

- **Request Format**:
  - The script sends POST requests to the `https://www.openai.fm/api/generate` endpoint.
  - It uses `multipart/form-data` to send text input, voice, and prompt information to the API.

- **Headers**:
  - The following headers are included in the requests:
    ```
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarya027BOtfh6crFn7A",
    "Accept": "*/*",
    "Origin": "https://www.openai.fm",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.openai.fm/worker-444eae9e2e1bdd6edd8969f319655e70.js",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=1, i"
    ```

- **Response Handling**:
  - The script checks the `Content-Type` in the response headers for `audio/wav` to ensure that a WAV audio file is returned.
  - If the response is a WAV file, it saves the content to a file.
  - Errors during the API request are caught and printed to the console.

- **File Saving Functionality**:
  - Audio files are saved with a timestamped filename (e.g., `output_YYYYMMDD_HHMMSS.wav`) in the same directory as the script.
  - The filename is generated using the `datetime` module to ensure uniqueness.

## Usage Examples

1. **Basic Usage**:
   Run `python main.py` from your terminal. The script will guide you through voice and vibe selection, and prompt you to enter text for speech generation.

2. **Voice Selection**:
   The script displays a numbered list of voices from `voices.json`. Enter the number corresponding to your desired voice when prompted.

3. **Vibe Customization**:
   Similarly, the script lists available vibes from `vibes.json`. Choose a vibe by entering its corresponding number to apply a specific emotional tone to the voice.

4. **Output Handling**:
   After successful audio generation, the script saves the audio as a `.wav` file and prints a confirmation message to the console, indicating the filename and successful save.

## Technical Details

- **API Endpoint**: `https://www.openai.fm/api/generate`
- **Request/Response Format**: `multipart/form-data` for requests, `audio/wav` for successful responses.
- **Headers Required**: Specific headers are needed to mimic browser requests to the OpenAI FM API (see 'Headers' section above).
- **File Handling**: Utilizes Python's `requests` library for API calls and standard file operations for saving audio files.

## Documentation

- **`display_choices(choices, choice_type)`**: 
  - Displays a numbered list of choices (voices or vibes) to the user.
  - Parameters: 
    - `choices`: A list of strings representing the choices.
    - `choice_type`: A string describing the type of choice (e.g., "voice", "vibe").

- **`get_user_choice(choices, choice_type)`**:
  - Prompts the user to enter a number to select from the displayed choices.
  - Validates user input and returns the selected choice.
  - Parameters:
    - `choices`: A list of available choices.
    - `choice_type`: Type of choice being made.

- **`format_vibe_prompt(vibe_name, vibes_data)`**:
  - Formats the vibe description from `vibes.json` into a prompt string suitable for the API.
  - Parameters:
    - `vibe_name`: The name of the selected vibe.
    - `vibes_data`: A dictionary containing vibe configurations.

- **`generate_filename()`**:
  - Generates a unique filename for the audio output file based on the current timestamp.
  - Returns: A string representing the filename.

- **`send_request(text, voice, vibe_prompt)`**:
  - Sends the text, voice, and vibe prompt to the OpenAI FM API.
  - Handles the API request and response, and saves the audio file if successful.
  - Parameters:
    - `text`: The text to be converted to speech.
    - `voice`: The selected voice.
    - `vibe_prompt`: The formatted prompt based on the selected vibe.

- **`load_voices()`**:
  - Loads voice options from `voices.json`.
  - Returns: A list of available voices.

- **`load_vibes()`**:
  - Loads vibe configurations from `vibes.json`.
  - Returns: A dictionary of vibe configurations.

- **`main()`**:
  - Main function to run the script, handling voice and vibe selection, user text input, and audio generation.

## Dependencies

- **Python**: 3.6 or higher.
- **requests**: Install using `pip install requests`.

## Legal Disclaimer

This project is intended for educational and personal use only. It is not affiliated with, endorsed by, or officially supported by OpenAI. Use of the OpenAI FM API is subject to their terms of service. Reverse engineering was employed to understand the API for the purpose of creating this tool. Please ensure your usage complies with all applicable terms and legal standards.

---

## Donation

Your support is appreciated:

- **USDt (TRC20)**: `TGCVbSSJbwL5nyXqMuKY839LJ5q5ygn2uS`
- **BTC**: `13GS1ixn2uQAmFQkte6qA5p1MQtMXre6MT`
- **ETH (ERC20)**: `0xdbc7a7dafbb333773a5866ccf7a74da15ee654cc`
- **LTC**: `Ldb6SDxUMEdYQQfRhSA3zi4dCUtfUdsPou`

## Author and Contact

- **GitHub**: [FairyRoot](https://github.com/fairy-root)
- **Telegram**: [@FairyRoot](https://t.me/FairyRoot)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.

