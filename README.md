# 📖 AI Visual Novel

AI Visual Novel is an interactive **Choose Your Own Adventure** application built with **Python** and **Streamlit**. The application uses **Google Gemini AI** to dynamically generate story scenes and player choices, **Pollinations AI** to generate scene images, and **Google Text-to-Speech (gTTS)** to create audio narration.

Each decision made by the player changes how the story progresses, creating a dynamic and personalized visual novel experience.

---

## ✨ Features

- 🤖 **AI-Generated Stories** — Uses Google Gemini to dynamically generate story scenes.
- 🌀 **Interactive Storytelling** — Players choose from multiple actions to determine how the story continues.
- 🎭 **Multiple Story Genres** — Choose from:
  - Horror
  - Adventure
  - Fiction
  - Fantasy
  - Mystery
- 🎨 **Multiple Art Styles** — Generate scenes in styles such as:
  - Oil Painting
  - 3D Render
  - Surrealism
  - Art Deco
  - Pop Art
- 🖼️ **AI-Generated Scene Images** — Uses Pollinations AI to generate images based on each scene.
- 🔊 **Audio Narration** — Uses gTTS to convert story text into speech.
- 📚 **Story History** — Previous scenes remain visible as the player progresses.
- 🔄 **Dynamic Story Continuation** — Gemini maintains the conversation context and continues the story based on the player's choices.
- ⚡ **Streamlit Interface** — Provides a simple and interactive web interface.

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini API
- Google Gen AI Python SDK
- Pollinations AI
- gTTS (Google Text-to-Speech)
- Requests
- python-dotenv

---

## 🧠 How It Works

The application follows this workflow:

1. The player selects a **story genre** and **art style** from the sidebar.
2. The player clicks **Start Novel 🌀**.
3. A Gemini chat session is created.
4. Gemini generates a JSON response containing:
   - Story text
   - Image generation prompt
   - 2–3 player choices
5. The image prompt is sent to Pollinations AI.
6. Pollinations AI generates an image representing the current scene.
7. gTTS converts the story text into audio narration.
8. The story, image, audio, and available choices are displayed.
9. The player selects one of the available choices.
10. The selected choice is sent back to the existing Gemini chat session.
11. Gemini generates the next scene while maintaining story continuity.
12. The process continues, creating an interactive AI-powered visual novel.

---

## 📂 Project Structure

```text
AI-Visual-Novel/
│
├── app.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

### File Description

**`app.py`**

Contains the main Streamlit application, including story generation, image generation, audio narration, session state management, and user interaction.

**`.env`**

Stores the Gemini API key securely.

**`.gitignore`**

Prevents sensitive and unnecessary files such as `.env` from being uploaded to GitHub.

**`requirements.txt`**

Contains all Python dependencies required to run the application.

**`README.md`**

Contains documentation and setup instructions for the project.

---

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd AI-Visual-Novel
```

Replace `<your-repository-url>` with the URL of your GitHub repository.

---

### 2. Create a Virtual Environment

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Alternatively, install the required packages manually:

```bash
pip install streamlit google-genai python-dotenv requests gTTS
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory of the project.

```text
gemini_apikey=YOUR_GEMINI_API_KEY
```

Replace `YOUR_GEMINI_API_KEY` with your actual Gemini API key.

> ⚠️ Never upload your `.env` file or API key to GitHub.

Add the following to your `.gitignore` file:

```text
.env
venv/
__pycache__/
sound.mp3
```

---

## 📦 requirements.txt

Create a `requirements.txt` file containing:

```text
streamlit
google-genai
python-dotenv
requests
gTTS
```

You can also generate it automatically using:

```bash
pip freeze > requirements.txt
```

---

## ▶️ Running the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

Streamlit will start a local development server and open the application in your browser.

---

## 🎮 How to Use

1. Open the application.
2. Select your preferred **Story Genre** from the sidebar.
3. Select your preferred **Art Style**.
4. Click **Start Novel 🌀**.
5. Wait for the AI to generate the opening scene.
6. View the AI-generated scene image.
7. Listen to the audio narration.
8. Read the generated story.
9. Select one of the available choices.
10. Continue making decisions and watch the story evolve.

Every choice influences what happens next.

---

## 🧩 AI Response Format

The Gemini model is instructed to return a structured JSON response:

```json
{
  "story_text": "The narrative paragraph for the current scene.",
  "image_prompt": "A detailed prompt describing the visual scene.",
  "options": [
    "First possible action",
    "Second possible action",
    "Third possible action"
  ]
}
```

This structure allows the application to separately process:

- `story_text` → Displayed as the story and converted to audio.
- `image_prompt` → Sent to the image generation service.
- `options` → Displayed as interactive Streamlit buttons.

---

## 💾 Session State Management

Streamlit reruns the entire Python script whenever the user interacts with a widget.

To preserve the story across reruns, the application uses `st.session_state`.

The main session state variables are:

```python
st.session_state.scenes
st.session_state.chat
st.session_state.scene
st.session_state.audio
```

### `scenes`

Stores all previously generated scenes so the complete story history can be displayed.

### `chat`

Stores the active Gemini chat session. This allows Gemini to remember previous interactions and maintain story continuity.

### `scene`

Temporarily stores the latest scene returned by Gemini before it is processed.

### `audio`

Reserved for storing audio-related data.

---

## 🖼️ Image Generation

Each Gemini response includes an `image_prompt` describing:

- Characters
- Environment
- Lighting
- Mood
- Atmosphere
- Camera perspective
- Selected visual style

The prompt is sent to Pollinations AI to generate a scene image.

Example:

```python
url = f"https://image.pollinations.ai/prompt/{image_prompt}?height=500&width=500"

image_response = requests.get(url)
```

The generated image is then displayed using Streamlit.

---

## 🔊 Audio Narration

The application uses gTTS to convert each story scene into speech.

```python
tts = gTTS(text=text, lang="en")
tts.save("sound.mp3")
st.audio("sound.mp3")
```

This adds audio narration to the visual novel experience.

---

## 🚀 Future Improvements

Possible features that can be added in the future:

- 👤 Character creation and customization
- 🧑‍🎨 Character consistency across generated images
- 💾 Save and load story progress
- 📖 Export completed stories
- 🎵 Background music and sound effects
- ❤️ Character health and inventory systems
- 🏆 Multiple endings
- 🌍 More story genres
- 🎨 More art styles
- 🔊 Multiple narrator voices
- 🧠 Improved long-term story memory
- 📱 Improved mobile responsiveness
- ☁️ Cloud deployment
- 🔐 User authentication
- 📚 Saved story library

---

## ⚠️ Known Limitations

- AI responses may occasionally fail to produce valid JSON.
- Image generation speed depends on the external image generation service.
- Audio generation requires an internet connection.
- Story quality and consistency depend on the AI model.
- Using the same `sound.mp3` filename for every scene may cause audio files to be overwritten.
- External API availability can affect application functionality.

---

## 🤝 Contributing

Contributions are welcome!

If you would like to improve the project:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Push the branch to your fork.
6. Open a Pull Request.

---

## 📄 License

This project is intended for educational and learning purposes.

You may add an open-source license such as the MIT License if you plan to make the project publicly available for reuse.

---

## 👨‍💻 Author

**Harsha Paloju**

Built as an AI-powered interactive storytelling project combining **Generative AI, image generation, text-to-speech, and Streamlit**.

---

## ⭐ Support

If you find this project interesting or useful, consider giving the repository a ⭐ on GitHub!

Enjoy creating your own AI-powered adventures! 📖✨
