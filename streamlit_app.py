import streamlit as st
import streamlit.components.v1 as components

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Presentonomica | School of Economics, XIM University",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS STYLING ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Injecting CSS for theming and custom components
# Note: Streamlit's structure is different from raw HTML, so direct CSS mapping isn't always 1:1.
# This CSS block mimics the original design's aesthetic.
st.markdown("""
<style>
    /* --- General & Background --- */
    .stApp {
        background-color: #0a0a0a;
        color: #f0f0f0;
    }
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* --- Custom Headers & Text --- */
    h1, h2, h3 {
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        tracking-tight;
    }
    .highlight-blue {
        color: #3b82f6; /* Tailwind blue-500 */
    }
    .hero-subtitle {
        color: #d1d5db; /* Tailwind gray-300 */
        font-size: 1.25rem;
        max-width: 48rem;
        margin: auto;
    }

    /* --- Custom Card Styles --- */
    .topic-card, .spec-card, .prize-card, .program-card {
        background-color: #111827; /* Tailwind gray-900 */
        border: 1px solid #374151; /* Tailwind gray-700 */
        padding: 1.5rem;
        border-radius: 0.75rem;
        margin-bottom: 1rem;
        transition: all 0.3s ease-in-out;
        height: 100%;
    }
    .topic-card:hover, .spec-card:hover, .prize-card:hover, .program-card:hover {
        border-color: #3b82f6;
        transform: translateY(-5px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    }
    
    .prize-card-highlight {
         border: 2px solid #3b82f6;
         transform: scale(1.05);
    }

    /* --- Section Styling --- */
    .section-header {
        text-align: center;
        margin-bottom: 3rem;
    }
    
    /* Remove Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)


# --- HERO SECTION ---
with st.container():
    st.markdown('<p style="text-align: center; color: #60a5fa; font-weight: 600;">SCHOOL OF ECONOMICS, XIM UNIVERSITY PRESENTS</p>', unsafe_allow_html=True)
    st.markdown('<h1 style="text-align: center; font-size: 5rem; font-weight: 900;">Presentonomica</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Showcase your analytical skills, engage with peers, and gain valuable exposure to real-world economic problem-solving. An event to make economics accessible, relevant, and impactful.</p>', unsafe_allow_html=True)
    st.markdown("---")


# --- ABOUT SECTION ---
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('## About <span class="highlight-blue">XIM University</span>', unsafe_allow_html=True)
        st.markdown("""
        <div style="color: #9ca3af; line-height: 1.75;">
        XIM University ignites the potential of tomorrow’s leaders by delivering top-tier education across a wide range of disciplines. We continually launch innovative programs aimed at shaping visionaries who are capable, committed, compassionate, and grounded in values. Students are equipped not only with knowledge and skills but with a long-view mindset: to innovate, serve society, and grow meaningfully.
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown('## About <span class="highlight-blue">Presentonomica</span>', unsafe_allow_html=True)
        st.markdown("""
        <div style="color: #9ca3af; line-height: 1.75;">
        This event offers a platform to showcase analytical prowess and engage in real-world economic problem-solving. It embodies the academic spirit of the School of Economics, making the discipline accessible and impactful. Participants will also experience an exuberant celebration of Odisha’s rich heritage and culture.
        </div>
        """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)


# --- EVENT SPECS SECTION ---
with st.container():
    st.markdown('<div class="section-header"><h2>Event Specifications</h2><p style="color: #9ca3af;">Key details for all participants.</p></div>', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div class="spec-card">
            <h3 class="highlight-blue">Open For</h3>
            <p>Postgraduate, Undergraduate, and Class XI–XII students.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="spec-card">
            <h3 class="highlight-blue">Prizes</h3>
            <p>Exciting cash prizes for winners and runners-up in each category.</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="spec-card">
            <h3 class="highlight-blue">Recognition</h3>
            <p>A Certificate of Participation for every single participant.</p>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class="spec-card">
            <h3 class="highlight-blue">Cultural Showcase</h3>
            <p>Experience a vibrant celebration of Odisha’s rich heritage.</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("---")

# --- TOPICS SECTION ---
with st.container():
    st.markdown('<div class="section-header"><h2>Presentation Topics</h2><p style="color: #9ca3af;">Choose a topic from your category and prepare to present your perspective.</p></div>', unsafe_allow_html=True)

    pg_topics, ug_topics, school_topics = st.tabs(["Postgraduate (PG)", "Undergraduate (UG)", "School (XI-XII)"])

    with pg_topics:
        topics = [
            "Does Dani Rodrik’s political trilemma prove that globalization cannot coexist with full democracy and sovereignty?",
            "Does infrastructure investment in emerging economies create fragility instead of growth?",
            "Is the push for de-risking global supply chains really economic strategy or disguised geopolitical warfare?",
            "Do stock market driven budgets undermine democratic accountability?",
            "Is inequality between countries a bigger threat than inequality within countries?",
            "Do humanitarian interventions like aid to Gaza undermine state sovereignty or reinforce global order?",
            "Does Gen Z represent a radical break in economic behavior or just a continuation of earlier youth waves?",
            "Should demographic change redefine global economic leadership?",
            "Are uprisings in places like Nepal or France symptoms of a global legitimacy crisis in governments?"
        ]
        for topic in topics:
            st.markdown(f'<div class="topic-card">{topic}</div>', unsafe_allow_html=True)

    with ug_topics:
        topics = [
            "Does raising the minimum wage in Europe do more harm than good?",
            "Should developing nations weaponize tariffs as a bargaining tool against the West?",
            "Should cryptocurrencies be banned by governments for economic stability?",
            "Is forgiving the debt of poorer nations justified and practical?",
            "Will artificial intelligence destroy more jobs than it creates for India’s youth?",
            "Does the India-Japan migration agreement signal a new era for Asia’s labor markets?",
            "Is the youth bulge in South Asia an economic dividend or a ticking time bomb?",
            "Is France’s political crisis proof that democracy is fragile in advanced economies?",
            "Should India support or stay away from uprisings in neighboring countries like Nepal?"
        ]
        for topic in topics:
            st.markdown(f'<div class="topic-card">{topic}</div>', unsafe_allow_html=True)

    with school_topics:
        topics = [
            "Should India implement Universal Basic Income to secure its future?",
            "Are higher taxes on the stock market the right way to fund welfare?",
            "Should India scrap food subsidies and switch fully to cash transfers?",
            "Should countries restrict outsourcing of tech jobs to protect their youth?",
            "Should rural India prioritize digital infrastructure over roads and bridges?",
            "Should humanitarian aid to Gaza be unconditional, even if it risks being misused?",
            "Should Gen Z be trusted to lead climate change solutions more than today’s politicians?",
            "Is population slowdown in India a threat to growth, or an opportunity?"
        ]
        for topic in topics:
            st.markdown(f'<div class="topic-card">{topic}</div>', unsafe_allow_html=True)
    st.markdown("---")


# --- PRIZES SECTION ---
with st.container():
    st.markdown('<div class="section-header"><h2>Prizes & Recognition</h2><p style="color: #9ca3af;">Rewarding excellence at every level of participation.</p></div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="prize-card">
            <h3>Postgraduate</h3>
            <p><span style="font-weight: bold; color: #60a5fa;">Winner:</span> ₹5,000</p>
            <p><span style="font-weight: bold; color: #9ca3af;">Runner-Up:</span> ₹4,000</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="prize-card prize-card-highlight">
            <h3>Undergraduate</h3>
            <p><span style="font-weight: bold; color: #60a5fa;">Winner:</span> ₹4,000</p>
            <p><span style="font-weight: bold; color: #9ca3af;">Runner-Up:</span> ₹3,000</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
         st.markdown("""
        <div class="prize-card">
            <h3>School (XI-XII)</h3>
            <p><span style="font-weight: bold; color: #60a5fa;">Winner:</span> ₹3,000</p>
            <p><span style="font-weight: bold; color: #9ca3af;">Runner-Up:</span> ₹2,000</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.25rem; margin-top: 2rem;">Every participant will be awarded a <span class="highlight-blue" style="font-weight:600;">Certificate of Participation</span>.</p>', unsafe_allow_html=True)
    st.markdown("---")

# --- ACADEMIC PROGRAMS ---
with st.container():
    st.markdown('<div class="section-header"><h2>Our Flagship Programs</h2><p style="color: #9ca3af;">Discover the programs that shape the future of economics.</p></div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="program-card">
            <h3 class="highlight-blue">M.Sc. in Economics</h3>
            <p style="color: #9ca3af;">Crafted to equip students with cutting-edge knowledge and advanced technical skills, preparing graduates to excel in corporate and academic arenas on par with the best institutions in India and abroad.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="program-card">
            <h3 class="highlight-blue">B.Sc. (Hons.) in Economics</h3>
            <p style="color: #9ca3af;">A full-time, four-year program offering a wide range of interdisciplinary courses. It sharpens critical thinking, strengthens logical analysis, and deepens understanding of pressing economic issues.</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("---")


# --- REGISTRATION SECTION ---
with st.container():
    st.markdown('<div class="section-header"><h2>Register for Presentonomica</h2><p style="color: #9ca3af;">Fill out the form below to secure your spot. Registrations are now live.</p></div>', unsafe_allow_html=True)
    
    components.iframe(
        "https://docs.google.com/forms/d/e/1FAIpQLScNfpn1Lua6uE8lMa_tReeWjhBkvqklIKyhrpasbM99PgykQw/viewform?embedded=true",
        height=1871,
        scrolling=True
    )

# --- FOOTER ---
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #6b7280;">
        <p>&copy; 2024 School of Economics, XIM University. All Rights Reserved.</p>
        <p style="font-size: 0.875rem;">Designed for Presentonomica.</p>
    </div>
    """,
    unsafe_allow_html=True
)
