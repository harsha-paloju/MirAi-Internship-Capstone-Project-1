import streamlit as st
import requests
import random

st.title("AI image Studio")
st.divider()

prompt=st.chat_input("Enter your Prompt for the message:")

height=st.sidebar.slider("Height",min_value=256,max_value=1024,value=750)
width=st.sidebar.slider("Width",min_value=256,max_value=1024,value=750)

image_type=st.sidebar.selectbox("Select the image type:",["Realistic","Pecil Sketch","3D render","Illustration"])

l = [
    "A colossal transparent blue whale floating through a futuristic neon city at midnight, tiny flying cars swimming around it like fish, rain reflecting vibrant lights on the streets, cinematic wide-angle composition, breathtaking atmosphere, ultra photorealistic, masterpiece, 8K, highly detailed",
    "An astronaut in a white spacesuit riding a majestic black horse across the glowing rings of Saturn, enormous planet dominating the background, colorful cosmic nebulae and millions of stars, dramatic cinematic lighting, surreal realism, ultra detailed, masterpiece, 8K",
    "A hidden ancient civilization built inside the hollow trunk of a gigantic thousand-year-old tree, tiny golden temples and waterfalls flowing between branches, glowing magical creatures flying through the air, volumetric sunlight, epic fantasy atmosphere, incredibly detailed, cinematic masterpiece, 8K",
    "A futuristic cyberpunk samurai standing on the edge of a skyscraper overlooking Tokyo in the year 3000, enormous holographic dragons flying between neon towers, heavy rain, glowing katana, dramatic lightning in the sky, cinematic composition, ultra photorealistic, masterpiece, 8K",
    "A breathtaking floating island above the clouds containing an entire magical kingdom, enormous waterfalls pouring endlessly into the sky below, giant dragons circling a crystal castle, golden sunset illuminating the clouds, epic cinematic fantasy landscape, hyper detailed, masterpiece, 8K"
]

if st.button("Suprise Me"):
    prompt=random.choice(l)
    

if st.sidebar.checkbox("Enable magic enhance"):
    full_prompt=f"{prompt} in Image Style - {image_type} and masterpiece, 8k resolution, highly detailed, trending on artstation, unreal engine 5 render"
else:
    full_prompt=f"{prompt} in Image Style - {image_type}"

url=f"https://image.pollinations.ai/prompt/{full_prompt}?height={height}&width={width}"

if "images" not in st.session_state:
            st.session_state.images=[]

if prompt:
    
    with st.spinner("Generating image ...."):

        st.session_state.images.append({
            "role":"user",
            "contents":full_prompt
        })

        response=requests.get(url)

        st.session_state.images.append({
            "role":"assistant",
            "contents":response.content
        })

for chat in st.session_state.images:
    if chat["role"]=="user":
        with st.chat_message(chat["role"]):
            st.write(chat["contents"])
    else:
        with st.chat_message(chat["role"]):
            st.image(chat["contents"])
        
if st.session_state.images:
    st.download_button("Download Image",data=st.session_state.images[-1]["contents"],file_name=f"{image_type}_image.png",mime=f"{image_type}_image/png")
    
            
    
