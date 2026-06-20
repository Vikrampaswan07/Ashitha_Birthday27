import streamlit as st
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Happy Birthday Ashitha!",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM AESTHETIC STYLING (CSS) ---
# Custom CSS to inject a soft pink/purple gradient, custom fonts, and glowing card effects
st.markdown("""
    <style>
    /* Background Gradient */
    .stApp {
        background: linear-gradient(135deg, #fedfe1 0%, #ecc7fc 50%, #b3e5fc 100%);
    }
    
    /* Main Title Styling */
    .birthday-title {
        font-family: 'Lilita One', 'Fredoka One', 'Comic Sans MS', sans-serif;
        color: #ff4081;
        text-align: center;
        font-size: 3.5rem;
        font-weight: bold;
        text-shadow: 3px 3px 0px #fff, 6px 6px 0px rgba(255, 64, 129, 0.2);
        margin-bottom: 10px;
        animation: pulse 2s infinite alternate;
    }
    
    /* Subtitles & Cards */
    .card {
        background: rgba(255, 255, 255, 0.75);
        backdrop-filter: blur(10px);
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 8px 32px 0 rgba(255, 105, 180, 0.2);
        border: 2px solid rgba(255, 255, 255, 0.5);
        text-align: center;
        margin-bottom: 20px;
    }
    
    .card h3 {
        color: #7b1fa2;
        font-family: 'Poppins', sans-serif;
    }
    
    /* Custom CSS Animations */
    @keyframes pulse {
        0% { transform: scale(1); }
        100% { transform: scale(1.03); }
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown('<h1 class="birthday-title">✨ Happy Birthday, Ashitha! ✨</h1>', unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; font-size: 1.2rem; color: #6a1b9a; font-weight: 500;'>"
    "Wishing you a day as bright, beautiful, and fabulous as you are! 💖</p>", 
    unsafe_allow_html=True
)

# --- INTERACTIVE CELEBRATION BUTTON ---
st.write("")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # A glowing trigger button to release the magic
    celebrate = st.button("🎉 Click to Celebrate Ashitha! 🎉", use_container_width=True)

if celebrate:
    # 1. Trigger full-screen balloon animation
    st.balloons()
    
    # 2. Add an extra pop of snow/glitter particles
    st.snow()
    
    # 3. Dynamic typing countdown/reveal
    with st.spinner("✨ Loading your birthday magic..."):
        time.sleep(1)
    st.toast("Make a wish, Ashitha! 🎂", icon="✨")

# --- MULTI-TAB INTERACTIVE DISPLAY ---
st.write("")
tab1, tab2, tab3 = st.tabs(["💝 The Birthday Card", "🔮 Future Predictor", "📸 Photo Memory"])

with tab1:
    st.markdown("""
        <div class="card">
            <h3>To an Absolute Queen 👑</h3>
            <p style="font-size: 1.1rem; color: #4a4a4a; line-height: 1.6;">
                May your year ahead be filled with endless aesthetic coffees, perfect outfits, 
                unforgettable late-night laughs, and massive success. Never stop shining! ✨🌈
            </p>
            <span style="font-size: 2rem;">🎂 🍰 🧁 🦄 💫</span>
        </div>
        """, unsafe_allow_html=True)

# with tab2:
#     st.markdown('<div class="card"><h3>✨ Your Vibe for the Upcoming Year ✨</h3></div>', unsafe_allow_html=True)
#     # A fun interactive element to keep users engaged
#     if st.button("🔮 Reveal Your Fortune", use_container_width=True):
#         predictions = [
#             "📈 Ultimate Main Character Energy & Success!",
#             "✈️ Spontaneous, aesthetic trips with your besties!",
#             "☕ Clearing every goal while maintaining perfect skin & zero stress.",
#             "🌟 A massive breakthrough in your passions and career!"
#         ]
#         import random
#         chosen = random.choice(predictions)
#         st.success(f"**The Universe says:** {chosen}")

with tab2:
    st.markdown('<div class="card"><h3>✨ Your Vibe for the Upcoming Year ✨</h3></div>', unsafe_allow_html=True)
    
    # A fun interactive element to keep users engaged
    if st.button("🔮 Reveal Your Fortune", use_container_width=True):
        predictions = [
            "📈 Ultimate Main Character Energy & Success!",
            "✈️ Spontaneous, aesthetic trips with your besties!",
            "☕ Clearing every goal while maintaining perfect skin & zero stress.",
            "🌟 A massive breakthrough in your passions and career!"
        ]
        import random
        chosen = random.choice(predictions)
        
        # --- NEW CUSTOM BROWN BOX ---
        # Using custom HTML instead of st.success to control the exact color
        st.markdown(f"""
            <div style="background-color: #FDF5E6; padding: 15px; border-radius: 8px; color: #8B4513; font-size: 1.1rem; border: 1px solid #8B4513; text-align: left;">
                <strong>The Universe says:</strong> {chosen}
            </div>
        """, unsafe_allow_html=True)




# with tab3:
#     st.markdown('<div class="card"><h3>📸 Captured Moments</h3></div>', unsafe_allow_html=True)
#     # Placeholder for birthday image/aesthetic graphics
#     st.info("💡 Tip: Replace the URL below with a real link to Ashitha's best photo!")
#     st.image(
#         "https://images.unsplash.com/photo-1513151233558-d860c5398176?auto=format&fit=crop&w=800&q=80",
#         caption="Cheers to brilliant new beginnings! 🥂",
#         use_container_width=True
#     )

with tab3:
    st.markdown('<div class="card"><h3>📸 Imagination Photos and Memories</h3></div>', unsafe_allow_html=True)
    
    # Create 3 columns for a photo grid
    colA, colB, colC = st.columns(3)
    
    with colA:
        st.image("pic1.png", caption="Created by Gemini! ☕", use_container_width=True)
    
    with colB:
        st.image("pic2.png", caption="Created by ChatGPT! 🤖", use_container_width=True)
        
    with colC:
        st.image("pic3.png", caption="Created by Gemini! ✨", use_container_width=True)

    with colC:
        st.image("pic4.jpeg", caption="Created by Gemini! ✨", use_container_width=True)

    with colC:
        st.image("pic5.jpeg", caption="Created by Gemini! ✨", use_container_width=True)

    with colC:
        st.image("pic6.jpeg", caption="Created by Gemini! ✨", use_container_width=True)
        


# # --- MUSIC PLAYER ---
# # A subtle placeholder to play background vibes
# st.write("---")
# st.markdown("<p style='text-align: center; color: #7b1fa2;'>🎵 Play your favorite birthday track:</p>", unsafe_allow_html=True)
# # You can embed a royalty-free track or audio stream link here
# st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

# --- MUSIC PLAYER ---
st.write("---")
st.markdown("<p style='text-align: center; color: #7b1fa2;'>🎵 Play Ashitha's birthday anthem:</p>", unsafe_allow_html=True)

# Replace 'birthday_song.mp3' with the exact name of your saved music file
st.audio("music.mp3", format="audio/mpeg", autoplay=True)




# --- FOOTER ---
st.markdown(
    "<br><hr><p style='text-align: center; font-size: 0.8rem; color: #888;'>"
    "Made with 💖 using Python & Streamlit</p>", 
    unsafe_allow_html=True
)