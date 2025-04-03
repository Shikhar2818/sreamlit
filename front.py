import streamlit as st

# Function to handle the age category feedback
def age_category_feedback(age):
    if 0 <= age <= 5:
        st.markdown("""
        ### 👶 Parental Steps for Nurturing Development
        *Health & Safety*
        - Regular check-ups, immunizations, and maintaining a safe, child-friendly home environment.
        - Nutrition guidance for each stage, from breastfeeding and formula to introducing solids and toddler nutrition.
        - [Watch Video: Child Safety at Home | Babyproofing Tips](https://www.youtube.com/watch?v=WQuX_Yw3yIg)
        
        *Emotional Support & Bonding*
        - Importance of bonding through skin-to-skin contact, eye contact, and responsive caregiving.
        - Tips for building trust and security through a consistent routine.
        - [Watch Video: Importance of Bonding with Babies](https://www.youtube.com/watch?v=AHMsmn6EX84)
        
        *Language & Communication*
        - Talking, singing, and reading to your child daily, starting from birth.
        - Encouraging early language skills through interactive books and simple conversations.
        - [Watch Video: Early Language Skills](https://www.youtube.com/watch?v=4ROA7UK6c7U)
        
        *Physical Activity & Motor Skills*
        - Age-appropriate ways to encourage movement, from tummy time for infants to outdoor play for toddlers.
        - [Watch Video: Encouraging Motor Skills](https://www.youtube.com/watch?v=lRyElTQFhtY)
        
        ### 📚 Cognitive and Motor Skill Development
        - *0-12 Months:* Tummy Time, Sensory Play, and Reading Aloud.
        - *1-3 Years:* Fine Motor Skills, Basic Counting & Shapes, and Imaginative Play.
        - *3-5 Years:* Pre-writing Skills, Early Literacy & Numeracy, and Social Play.
        """)
        st.balloons()
    elif 6 <= age <= 10:
        st.markdown("""
        ### 🧒 5-10 Years Child Care & Development
        *Introduction:*
        This stage is crucial for building foundational skills in academics, emotional intelligence, and social relationships.
        
        *Parental Steps for Nurturing Development*
        - *Encouraging Learning & Curiosity:* Foster a love for learning through books, games, and educational outings.
        - *Developing Social Skills & Empathy:* Encourage respectful interactions and teamwork.
        - *Physical Health & Activity:* Ensure regular physical activity and emphasize the importance of a balanced diet.
        - *Responsibility & Independence:* Give children age-appropriate responsibilities to build confidence.
        
        ### 🎨 Activities for Learning, Social Skills, and Physical Growth
        - *5-7 Years:* Reading & Storytelling, Basic Math Games, Cooperative Games.
        - *7-8 Years:* Science & Exploration Activities, Art & Creativity, Introduction to Music or Dance.
        - *8-10 Years:* Problem-Solving Challenges, Goal-Oriented Activities, Team Sports or Group Activities.
        """)
        st.snow()
    elif 10 <= age <= 15:
        st.markdown("""
        ### 🧑‍🦰 Pre-Teen & Early Adolescent Development
        *Parental Steps for Supporting Growth and Independence*
        - *Encourage Open Communication & Emotional Health*: Teach emotional intelligence and guide stress management.
        - *Support Academic & Personal Interests*: Help kids explore extracurricular activities.
        - *Foster Responsibility & Independence*: Gradually increase responsibilities and decision-making opportunities.
        - *Guide Safe Social Media Use*: Discuss online safety and encourage healthy tech habits.
        
        ### 🏃 Activities for Skill Development, Social Growth, and Healthy Habits
        - *10-12 Years:* Exploratory Learning, Team Sports, Creative Expression.
        - *12-13 Years:* Goal-Oriented Projects, Physical Fitness & Health Awareness, Peer Interaction.
        - *13-15 Years:* Academic and Career Exploration, Volunteer Work, Independent Hobbies.
        """)
    elif 15 <= age <= 18:
        st.markdown("""
        ### 👩‍🎓 Teen Development (Ages 15-18)
        *Parental Steps for Guiding Independence and Responsibility*
        - *Encourage Open Communication & Emotional Support*: Foster open dialogue about stress, peer pressure, and relationships.
        - *Support Academic & Career Preparation*: Help teens explore college, career paths, and vocational options.
        - *Promote Financial Responsibility*: Teach budgeting, saving, and managing money.
        - *Guide Safe and Responsible Social Media Use*: Encourage a balanced relationship with technology.
        
        ### 🎯 Activities for Personal Development, Social Skills, and Future Planning
        - *15-16 Years:* Academic Enrichment, Volunteer Work, Social Skills Development.
        - *16-17 Years:* Part-Time Jobs, Life Skills Training, College & Career Exploration.
        - *17-18 Years:* Goal Setting & Future Planning, Independent Projects, Self-Care & Mental Health Practices.
        """)
        
    else:
        st.write("🚨 Invalid age category. Please try again.")

# Streamlit UI Elements
def main():
    st.title("👨‍👩‍👧‍👦 Child Care And Development")

    # Form for basic user info
    with st.form("user_info_form"):
        name = st.text_input("Enter your name:")
        age = st.number_input("Enter your age:", min_value=1, max_value=20)  # Limit the age range if necessary
        gender = st.text_input("Enter your gender:")
        submit_button = st.form_submit_button("Submit")

    # Store the page state in session state after the form submission
    if submit_button:
        st.session_state.name = name
        st.session_state.age = age
        st.session_state.gender = gender
        

        # If the user selects "Age Category"
        st.session_state.page_selected = "Age Category"
        age_category_feedback(age)
    st.markdown(
        "<p style='text-align: center; font-size: 12px;'>By Team STAR</p>", 
        unsafe_allow_html=True
    )

# Run the app
if __name__ == "__main__":
    main()