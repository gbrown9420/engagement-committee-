import streamlit as st
import pandas as pd
import random
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="iRhythm Engagement Committee Portal",
    page_icon="🎉",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern styling
st.markdown("""
    <style>
    /* Main App Background & Fonts */
    .stApp {
        background-color: #f8f9fa;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #2F5496;
    }
    
    /* Custom Card Style */
    .custom-card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        border-left: 5px solid #2F5496;
    }
    
    .event-card {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-bottom: 15px;
        border-left: 5px solid #28a745;
    }

    .comment-card {
        background-color: #f1f3f5;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 10px;
        border-left: 4px solid #17a2b8;
    }
    
    /* Buttons */
    .stButton>button {
        background-color: #2F5496;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 8px 16px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #1e3966;
        color: #ffc107;
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
    </style>
""", unsafe_allow_html=True)

# Define session state variables to store interactive data
if "comments" not in st.session_state:
    st.session_state.comments = [
        {"name": "Sarah T.", "topic": "Snack Ideas", "text": "Can we get more healthy snack options in the breakroom? Maybe some fresh fruit?", "time": "2026-08-19 14:32"},
        {"name": "Anonymous", "topic": "Workplace Vibe", "text": "Loved the trivia night! Let's do a board game lunch next time.", "time": "2026-08-20 09:15"},
        {"name": "Michael K.", "topic": "Wellness", "text": "The steps challenge was amazing. Highly recommend doing it quarterly!", "time": "2026-08-20 11:45"}
    ]

if "volunteers" not in st.session_state:
    st.session_state.volunteers = [
        {"name": "Alex Mercer", "email": "amercer@irhythmtech.com", "event": "Virtual Trivia Night", "role": "Trivia Host / MC"},
        {"name": "Jessica Lee", "email": "jlee@irhythmtech.com", "event": "Summer Volunteer Day", "role": "Logistics Coordinator"},
        {"name": "David Smith", "email": "dsmith@irhythmtech.com", "event": "Wellness Week", "role": "Stretch Session Leader"}
    ]

if "polls" not in st.session_state:
    st.session_state.polls = {
        "Friday Bagel Breakfast": {"likes": 42, "dislikes": 3},
        "Monthly Virtual Bingo": {"likes": 28, "dislikes": 12},
        "Bring Your Pet to Zoom Day": {"likes": 67, "dislikes": 5},
        "Lunch & Learn: Coding Basics": {"likes": 19, "dislikes": 14}
    }

if "events" not in st.session_state:
    st.session_state.events = [
        {"title": "🎮 Virtual Trivia Night", "date": "Sept 10, 2026", "time": "5:00 PM EST", "desc": "Join us for a fun-filled night of general trivia, pop culture, and team bonding! Prizes for the top 3 teams."},
        {"title": "🌳 Summer Volunteer Day", "date": "Sept 25, 2026", "time": "9:00 AM Local", "desc": "Partnering with local food banks and environmental centers. Sign up to make an impact in your local community!"},
        {"title": "🧘 Wellness Week & Steps Challenge", "date": "Oct 12-16, 2026", "time": "All Day", "desc": "Daily mindfulness breaks, desk stretching sessions, and our annual steps competition. Prizes for highest steps!"}
    ]

# --- Sidebar Navigation ---
st.sidebar.image("https://img.icons8.com/clouds/200/groups.png", width=120)
st.sidebar.title("iRhythm Engagement")
st.sidebar.write("Bringing teams together, fostering fun, and building connection across the company!")

menu = st.sidebar.radio(
    "Go To:",
    ["🏠 Home", "📌 Bulletin Boards", "💌 Comment Cards", "📊 Interactive Polls", "🤝 Volunteer Sign-up"]
)

st.sidebar.markdown("---")
st.sidebar.write("💡 *Developed by the iRhythm Engagement Committee*")
st.sidebar.write("Have feedback? Use the **Comment Cards** tab!")

# --- Menu Views ---

if menu == "🏠":
    # Title Banner
    st.markdown("<h1 style='text-align: center; color: #2F5496;'>🎉 iRhythm Engagement Committee Portal 🎉</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2em; color: #555;'>Your interactive hub for community, connection, and workplace fun!</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
            <div class='custom-card'>
                <h3>👋 Welcome iRhythm Team!</h3>
                <p>Welcome to our brand-new <strong>Engagement Portal</strong>! This site was designed to give every team member an interactive way to shape our workplace culture, pitch exciting new event ideas, and connect with peers across offices and remote spaces.</p>
                <p>Use this portal to check out the bulletin boards, leave a comment, sign up to volunteer, and vote in our fun monthly polls!</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.subheader("🚀 Featured Upcoming Events")
        for event in st.session_state.events[:2]:
            st.markdown(f"""
                <div class='event-card'>
                    <h4 style='color: #28a745; margin: 0;'>{event['title']}</h4>
                    <p style='margin: 5px 0; font-weight: bold;'>📅 Date: {event['date']} | ⏰ Time: {event['time']}</p>
                    <p style='margin: 0;'>{event['desc']}</p>
                </div>
            """, unsafe_allow_html=True)
            
    with col2:
        st.subheader("💡 Energy Meter")
        st.write("How are we feeling today, team?")
        mood = st.select_slider(
            "Current Vibe Indicator",
            options=["🔋 Low Power", "☕ Getting There", "🚀 Ready to Roll", "🔥 On Fire!"]
        )
        if mood == "🔥 On Fire!":
            st.balloons()
            st.success("Let's keep this energy going all week!")
        elif mood == "🚀 Ready to Roll":
            st.info("You love to see it! Let's conquer the day.")
        else:
            st.warning("Let the Engagement Committee cook up something fun to boost your energy! 🍪")
            
        st.markdown("---")
        st.subheader("📊 Quick Stats")
        st.metric(label="Open Volunteer Spots", value="8 Slots")
        st.metric(label="Active Poll Votes", value=str(sum(p['likes'] + p['dislikes'] for p in st.session_state.polls.values())))

elif menu == "📌 Bulletin Boards":
    st.markdown("<h2>📌 Bulletin Boards & Topics</h2>", unsafe_allow_html=True)
    st.write("Select a bulletin board category below to browse upcoming initiatives, news, or team boards.")
    
    board_category = st.tabs(["🎪 Upcoming Events", "🎨 Fun & Hobbies", "📢 Kudos & Celebration"])
    
    with board_category[0]:
        st.subheader("Current Event Calendar")
        cols = st.columns(3)
        for idx, event in enumerate(st.session_state.events):
            with cols[idx % 3]:
                st.markdown(f"""
                    <div class='custom-card' style='height: 250px;'>
                        <h4 style='color: #2F5496;'>{event['title']}</h4>
                        <p style='font-size: 0.9em; font-weight: bold; margin: 0 0 10px 0;'>🕒 {event['date']} @ {event['time']}</p>
                        <p style='font-size: 0.95em;'>{event['desc']}</p>
                    </div>
                """, unsafe_allow_html=True)
                
    with board_category[1]:
        st.subheader("🎨 Team Hobbies & Social Circles")
        st.write("Find your people! Connect with co-workers over shared interests:")
        hobby_cols = st.columns(2)
        with hobby_cols[0]:
            st.markdown("""
                <div class='custom-card'>
                    <h4>🏃 iRhythm Runners & Walkers</h4>
                    <p>Whether you're training for a 5K or just enjoy a morning walk, join our community chat! Share your routes, track achievements, and prep for the next charity walk.</p>
                    <span style='background-color: #e2e3e5; padding: 4px 8px; border-radius: 4px; font-size: 0.85em;'>Active Members: 45</span>
                </div>
            """, unsafe_allow_html=True)
        with hobby_cols[1]:
            st.markdown("""
                <div class='custom-card'>
                    <h4>📚 Page Turners (Monthly Book Club)</h4>
                    <p>We read one book a month across genres (fiction, professional growth, sci-fi) and meet virtually over lunch to chat. All are welcome!</p>
                    <span style='background-color: #e2e3e5; padding: 4px 8px; border-radius: 4px; font-size: 0.85em;'>Active Members: 22</span>
                </div>
            """, unsafe_allow_html=True)

    with board_category[2]:
        st.subheader("📢 Kudos & Digital Shout-outs")
        st.write("Got a teammate who went above and beyond? Give them a digital shout-out!")
        
        kudos_cols = st.columns(2)
        with kudos_cols[0]:
            st.success("🌟 **Kudos to David S.!** - 'Thank you for stepping in to lead the stress-testing workflow check when we were short-staffed. You're a rockstar!' — *From Laura M.*")
        with kudos_cols[1]:
            st.success("🎉 **Shout-out to the Onboarding Team!** - 'The new welcome kits are beautiful and make starting out so special. Thanks for the thoughtfulness!' — *From Alex P.*")

elif menu == "💌 Comment Cards":
    st.markdown("<h2>💌 Digital Comment Box</h2>", unsafe_allow_html=True)
    st.write("Have a suggestion, feedback, or a cool idea for the team? Drop a card in our digital suggestion box! You can choose to post anonymously or include your name.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Leave a Comment Card")
        with st.form("comment_form", clear_on_submit=True):
            name = st.text_input("Your Name (or leave blank for Anonymous)", placeholder="Anonymous")
            topic = st.selectbox("Topic Category", ["Event Suggestion", "Breakroom/Office", "Wellness", "Company Culture", "Other"])
            comment_text = st.text_area("Your Suggestion / Feedback")
            submit_comment = st.form_submit_button("Post Comment Card 📮")
            
            if submit_comment:
                if comment_text.strip() == "":
                    st.error("Please enter some text before submitting!")
                else:
                    display_name = name.strip() if name.strip() != "" else "Anonymous"
                    new_comment = {
                        "name": display_name,
                        "topic": topic,
                        "text": comment_text,
                        "time": datetime.now().strftime("%Y-%m-%d %H:%M")
                    }
                    st.session_state.comments.insert(0, new_comment)
                    st.success("Comment card dropped successfully!")
                    
    with col2:
        st.subheader("💬 Live Suggestions Wall")
        for comment in st.session_state.comments:
            st.markdown(f"""
                <div class='comment-card'>
                    <div style='display: flex; justify-content: space-between; font-weight: bold; margin-bottom: 5px;'>
                        <span style='color: #2F5496;'>👤 {comment['name']}</span>
                        <span style='background-color: #e2e3e5; font-size: 0.8em; padding: 2px 6px; border-radius: 4px;'>{comment['topic']}</span>
                    </div>
                    <p style='margin: 5px 0;'>"{comment['text']}"</p>
                    <div style='text-align: right; font-size: 0.75em; color: #888;'>📅 {comment['time']}</div>
                </div>
            """, unsafe_allow_html=True)

elif menu == "📊 Interactive Polls":
    st.markdown("<h2>📊 Interactive Likes & Dislikes Polls</h2>", unsafe_allow_html=True)
    st.write("We want to make sure we invest time and resources in events you actually want! Vote below to let us know what's a 'Like' and what's a 'Dislike'.")
    
    for idea, votes in st.session_state.polls.items():
        st.markdown(f"""
            <div class='custom-card'>
                <h4 style='margin: 0 0 10px 0;'>💡 Proposed Initiative: <strong>{idea}</strong></h4>
            </div>
        """, unsafe_allow_html=True)
        
        # Display stats
        total_votes = votes["likes"] + votes["dislikes"]
        like_pct = int((votes["likes"] / total_votes) * 100) if total_votes > 0 else 0
        dislike_pct = 100 - like_pct if total_votes > 0 else 0
        
        col1, col2, col3 = st.columns([1, 1, 3])
        with col1:
            if st.button(f"👍 Like ({votes['likes']})", key=f"like_{idea}"):
                st.session_state.polls[idea]["likes"] += 1
                st.rerun()
        with col2:
            if st.button(f"👎 Dislike ({votes['dislikes']})", key=f"dislike_{idea}"):
                st.session_state.polls[idea]["dislikes"] += 1
                st.rerun()
                
        with col3:
            # Simple custom progress bar visual using streamlit
            st.write(f"Approval Rating: **{like_pct}%** ({total_votes} total votes)")
            st.progress(like_pct / 100.0)

elif menu == "🤝 Volunteer Sign-up":
    st.markdown("<h2>🤝 Volunteer Sign-Up Sheet</h2>", unsafe_allow_html=True)
    st.write("Our amazing events only happen because of our incredible team volunteers! Sign up for a role below and join the action.")
    
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        st.subheader("Join a Team & Volunteer")
        with st.form("volunteer_form", clear_on_submit=True):
            vol_name = st.text_input("Full Name")
            vol_email = st.text_input("iRhythm Email Address")
            vol_event = st.selectbox("Select Event", [e["title"] for e in st.session_state.events])
            vol_role = st.text_input("Preferred Role (e.g., Coordinator, DJ, Setup, Clean-up)")
            submit_vol = st.form_submit_button("Sign Me Up! 🚀")
            
            if submit_vol:
                if vol_name.strip() == "" or vol_email.strip() == "" or vol_role.strip() == "":
                    st.error("Please fill out all the fields in the form!")
                elif "@irhythmtech.com" not in vol_email.lower():
                    st.error("Please use a valid iRhythm email address!")
                else:
                    new_vol = {
                        "name": vol_name,
                        "email": vol_email,
                        "event": vol_event,
                        "role": vol_role
                    }
                    st.session_state.volunteers.append(new_vol)
                    st.success("Thank you for volunteering! You have been added to the roster.")
                    st.balloons()
                    
    with col2:
        st.subheader("📋 Active Volunteer Roster")
        df = pd.DataFrame(st.session_state.volunteers)
        # Display as a styled table
        st.dataframe(
            df,
            column_config={
                "name": "Volunteer",
                "email": "Email Contact",
                "event": "Assigned Event",
                "role": "Role"
            },
            hide_index=True,
            use_container_width=True
        )
