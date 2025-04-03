import streamlit as st
def main():
   
    st.title("🎶 Explore Music Activities and Learning 🎵")

   
    music_activities = [
        {
            'title': '🎤 Singing Nursery Rhymes 🎶',
            'description': "Singing nursery rhymes is a fun way for young children to learn language, rhythm, and memory skills. Songs like 'Twinkle, Twinkle, Little Star' and 'Old MacDonald Had a Farm' introduce kids to melodies and simple words.",
            'fun_fact': 'Nursery rhymes like "Ring Around the Rosie" have origins dating back centuries, often tied to historical events!',
            'explore_online': 'https://www.youtube.com/kids',
        },
        {
            'title': '🎹 Playing Virtual Instruments 🥁',
            'description': "Virtual instruments provide an accessible way for kids to experiment with music. Online keyboards, drums, and xylophones help children understand sound, rhythm, and melody.",
            'fun_fact': 'The piano has been a foundational instrument in music education for centuries and helps build fine motor skills and hand-eye coordination.',
            'explore_online': 'https://www.examplelink.com',
        },
        {
            'title': '💃 Dance and Movement Songs 🕺',
            'description': "Songs with dance moves, like 'The Hokey Pokey' and 'Head, Shoulders, Knees, and Toes,' encourage physical movement, rhythm, and coordination. Dancing to music also improves body awareness and is a great way to express emotions.",
            'fun_fact': 'Moving to music has been shown to improve mood and cognitive function in children.',
            'explore_online': 'https://www.gonoodle.com',
        },
        {
            'title': '🥁 Learning Simple Beats on Drums 🎶',
            'description': "Drumming introduces kids to rhythm and timing. Simple patterns like 'boom-tap' can be played on toy drums or makeshift items like pots and pans.",
            'fun_fact': 'Drumming can help relieve stress, increase focus, and even improve coordination!',
            'explore_online': 'https://www.examplelink.com',
        }
    ]

    instruments = [
        {
            'title': '🎸 Guitar Basics 🎶',
            'description': "The guitar is a versatile instrument for all ages. Kids can start learning basic chords and rhythms, progressing to simple songs. Playing guitar improves hand-eye coordination and fine motor skills.",
            'fun_fact': 'The guitar has a history dating back over 4,000 years, evolving from ancient stringed instruments.',
            'explore_online': 'https://www.examplelink.com',
        },
        {
            'title': '🎹 Keyboard and Piano Exploration 🎶',
            'description': "The piano is a foundational instrument for music theory, making it perfect for beginners. Kids learn scales, notes, and chords, which are building blocks for other musical pursuits.",
            'fun_fact': 'The modern piano has 88 keys, and learning it can stimulate multiple areas of the brain!',
            'explore_online': 'https://www.examplelink.com',
        },
        {
            'title': '🎶 Ukulele for Beginners 🎸',
            'description': "The ukulele is a small, four-stringed instrument that’s easy for kids to pick up. It’s often tuned similarly to the top four strings of a guitar and has a fun, bright sound.",
            'fun_fact': 'The ukulele originated in Hawaii in the late 19th century, inspired by Portuguese instruments.',
            'explore_online': 'https://www.examplelink.com',
        },
        {
            'title': '🎻 Violin for Beginners 🎶',
            'description': "The violin is a string instrument played with a bow. Learning the violin helps develop pitch recognition, coordination, and musical sensitivity. Its sound ranges from soft and sweet to bold and intense.",
            'fun_fact': 'The violin’s structure has hardly changed since the 16th century, and it remains one of the most popular instruments in classical music.',
            'explore_online': 'https://www.examplelink.com',
        }
    ]

    music_styles = [
        {
            'title': '🎶 Classical Music 🎻',
            'description': "Classical music has been evolving for centuries and includes compositions by famous composers like Mozart, Beethoven, and Bach. Listening to classical music can improve concentration and expose kids to a wide range of musical dynamics.",
            'fun_fact': 'Studies have shown that listening to classical music can reduce stress and enhance cognitive function, known as the "Mozart Effect."',
            'explore_online': 'https://www.classicsforkids.com',
        },
        {
            'title': '🎷 Jazz Music 🎼',
            'description': "Jazz is an expressive, improvisational genre that originated in the African-American communities of New Orleans. It’s known for its lively rhythms and unique melodies and has influenced many other genres.",
            'fun_fact': 'Jazz incorporates "scat singing," where singers use nonsensical syllables to mimic the sounds of instruments.',
            'explore_online': 'https://www.spotify.com',
        },
        {
            'title': '🎶 Pop Music 🎤',
            'description': "Pop music is upbeat and catchy, designed to appeal to a broad audience. It often features repetitive lyrics and strong rhythms, making it a favorite among young listeners.",
            'fun_fact': 'Pop music started gaining popularity in the 1950s, with stars like Elvis Presley and The Beatles leading the way.',
            'explore_online': 'https://www.spotify.com',
        },
        {
            'title': '🌍 World Music 🌎',
            'description': "World music encompasses traditional and contemporary sounds from around the globe, introducing kids to various instruments, rhythms, and cultures.",
            'fun_fact': 'Instruments like the djembe drum (West Africa) and sitar (India) are often used in world music, providing a unique listening experience.',
            'explore_online': 'https://www.folkways.si.edu',
        }
    ]

   
    st.header("🎤 Music Activities 🕺")
    for activity in music_activities:
        st.subheader(activity['title'])
        st.write(activity['description'])
        st.write(f"✨ Fun Fact: {activity['fun_fact']} ✨")
        st.markdown(f"[Explore Online]({activity['explore_online']})", unsafe_allow_html=True)
        st.markdown("---")

   
    st.header("🎸 Learning About Instruments 🎶")
    for instrument in instruments:
        st.subheader(instrument['title'])
        st.write(instrument['description'])
        st.write(f"✨ Fun Fact: {instrument['fun_fact']} ✨")
        st.markdown(f"[Explore Online]({instrument['explore_online']})", unsafe_allow_html=True)
        st.markdown("---")

    
    st.header("🎼 Exploring Different Types of Music 🎧")
    for style in music_styles:
        st.subheader(style['title'])
        st.write(style['description'])
        st.write(f"✨ Fun Fact: {style['fun_fact']} ✨")
        st.markdown(f"[Explore Online]({style['explore_online']})", unsafe_allow_html=True)
        st.markdown("---")

    st.markdown(
        "<p style='text-align: center; font-size: 12px;'>By Team STAR</p>", 
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()