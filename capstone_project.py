import streamlit as st
import os 
import json
import requests
from google import genai
from dotenv import load_dotenv
load_dotenv()
from gtts import gTTS

@st.cache_resource
def get_client():
    try:
        client=genai.Client(api_key=os.getenv("gemini_apikey"))
        return client
    except Exception as e:
        st.error(f"Error creating Gemini client: {e}")

st.title("AI Visual novel 📖")
st.divider()

if "scenes" not in st.session_state:
    st.session_state.scenes=[]

if "chat" not in st.session_state:
    st.session_state.chat=None
    
if "scene" not in st.session_state:
    st.session_state.scene=None
    
if "audio" not in st.session_state:
    st.session_state.audio=None
    
st.sidebar.title("Story Settings ⚙️")

story_genre=st.sidebar.selectbox("Story genre",[
        "Horror",
        "Adventure",
        "Fiction",
        "Fantasy",
        "Mystery"
    ])

art_style=st.sidebar.selectbox("Art style 🎨",[
        "Oil Painting",
        "3D Render",
        "Surrealism",
        "Art Deco",
        "Pop Art"
    ])

client=get_client()

first_prompt = f"""
        Start a new Choose Your Own Adventure visual novel.
        Story Genre: {story_genre}
        Art Style: {art_style}
        Generate an engaging opening scene.
        Make sure the story follows the selected genre
        and the image prompt follows the selected art style.
        Give the player 2 to 3 choices for what to do next.
        """
        
system_prompt="""
You are an AI Story Director for an interactive
"Choose Your Own Adventure" visual novel.
Your job is to generate immersive story scenes and continue
the story based on the player's choices.
For every response, return ONLY a valid JSON object
with exactly these three keys:
{
    "story_text": "The narrative paragraph for the current scene.",
    "image_prompt": "A detailed prompt for generating an image of the scene.",
    "options": [
        "First possible action",
        "Second possible action",
        "Third possible action"
    ]
}
Rules:
1. Follow the Story Genre provided by the user.
2. Follow the Art Style provided by the user when creating
   the image_prompt.
3. Maintain continuity with previous scenes and player choices.
4. Generate 2 to 3 distinct and actionable choices.
5. The image_prompt must describe the characters, environment,
   lighting, mood, atmosphere, camera perspective, and visual style.
6. Return ONLY valid JSON.
7. Use exactly these keys:
   "story_text", "image_prompt", and "options".
8. Do not use Markdown.
9. Do not wrap the response in ```json.
10. Do not include any text before or after the JSON.
The response must be directly parseable using Python json.loads()
"""

if st.sidebar.button("Start Novel 🌀"):
    
    try:
        st.session_state.chat=client.chats.create(model="gemini-3.1-flash-lite")
        
        response=st.session_state.chat.send_message(f"{system_prompt} for {first_prompt}")
        
        text=response.text

        reply=json.loads(text)
        
        st.session_state.scene=reply

        st.rerun()
        
    except json.JSONDecodeError as e:
        st.error(f"Error reading AI response: {e}")
        
    except Exception as e:
        st.error(f"Error generating story: {e}")
    
if st.session_state.scene is not None:
    
    with st.spinner("generating scene..."):
        
        try:
            image_prompt=st.session_state.scene["image_prompt"]
            
            url=f"https://image.pollinations.ai/prompt/{image_prompt}?height=500&width=500"
                
            image_response=requests.get(url)
            
            scene={
                "story":st.session_state.scene["story_text"],
                "image":image_response._content,
                "options":st.session_state.scene["options"]
            }
            
            st.session_state.scenes.append(scene)
            
            st.session_state.scene=None
            
        except requests.RequestException as e:
            st.error(f"Error generating scene image: {e}")
            
        except Exception as e:
            st.error(f"Error processing scene: {e}")
    
if st.session_state.scenes:
    
    for index,one_scene in enumerate(st.session_state.scenes):
        
        st.subheader("Scene")
        
        try:
            st.image(one_scene["image"])
        except Exception as e:
            st.error(f"Error displaying image: {e}")
        
        text=one_scene["story"]
        
        try:
            tts=gTTS(text=text,lang="en")
            tts.save("sound.mp3")
            st.audio("sound.mp3")
            
        except Exception as e:
            st.error(f"Error generating audio: {e}")
            
        st.write(one_scene["story"])
        st.divider()
        
        if index==len(st.session_state.scenes)-1:
        
            for option_index,option in enumerate(one_scene["options"]):
                
                if st.button(option,key=f"{index},{option_index}"):
                    
                    try:
                        new_response=st.session_state.chat.send_message(option)
                        
                        new_reply=json.loads(new_response.text)
                        
                        st.session_state.scene=new_reply
                        
                        st.rerun()
                        
                    except json.JSONDecodeError as e:
                        st.error(f"Error reading AI response: {e}")
                        
                    except Exception as e:
                        st.error(f"Error generating next scene: {e}")