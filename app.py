import streamlit as st
import textwrap
from pathlib import Path

st.set_page_config(
    page_title="Jelaisa B. Daigdigan",
    page_icon="✦",
    layout="centered",
    initial_sidebar_state="collapsed",
)

if "page" not in st.session_state:
    st.session_state.page = "Home"

def go(page):
    st.session_state.page = page
    st.rerun()

# -------------------- PREMIUM MOBILE UI --------------------
st.markdown(textwrap.dedent("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

:root {
    --bg:#f7f5fb;
    --ink:#17131f;
    --muted:#77717f;
    --purple:#7c3aed;
    --purple2:#9b5cff;
    --line:#e9e3f2;
    --white:#ffffff;
    --dark:#17131f;
}

.stApp {
    background: var(--bg);
    font-family:'DM Sans',sans-serif;
}

.block-container {
    max-width: 480px !important;
    padding: 22px 17px 120px !important;
    margin:auto;
}

#MainMenu, footer, header {visibility:hidden;}
[data-testid="stSidebar"] {display:none;}

h1,h2,h3,p {font-family:'DM Sans',sans-serif;}

.topbar {
    display:flex;
    align-items:center;
    justify-content:space-between;
    margin-bottom:22px;
}

.brand {
    font-family:'Space Grotesk',sans-serif;
    font-weight:700;
    font-size:20px;
    color:var(--ink);
    letter-spacing:-.8px;
}

.brand-dot {color:var(--purple);}

.available {
    display:flex;
    align-items:center;
    gap:6px;
    color:#4c8b62;
    font-size:9px;
    font-weight:700;
    letter-spacing:1px;
}

.available i {
    width:6px;height:6px;border-radius:50%;
    background:#55b878;display:inline-block;
}

/* HERO */
.hero {
    position:relative;
    background:var(--dark);
    border-radius:31px;
    padding:29px 25px 25px;
    overflow:hidden;
    box-shadow:0 18px 40px rgba(32,20,50,.14);
}

.hero:after {
    content:"";
    position:absolute;
    width:220px;height:220px;
    border-radius:50%;
    right:-115px;top:-110px;
    background:var(--purple);
    opacity:.35;
}

.hero-kicker {
    position:relative;
    z-index:2;
    color:#b98cff;
    font-size:9px;
    font-weight:700;
    letter-spacing:2.2px;
}

.hero h1 {
    position:relative;
    z-index:2;
    color:#fff;
    font-family:'Space Grotesk',sans-serif;
    font-size:43px;
    line-height:.98;
    letter-spacing:-2.7px;
    margin:17px 0 15px;
}

.hero h1 span {color:#b979ff;}

.hero-copy {
    position:relative;
    z-index:2;
    color:#b7b1bf;
    font-size:12px;
    line-height:1.75;
    max-width:330px;
}

.hero-button {
    position:relative;
    z-index:2;
    margin-top:20px;
}

.chips {
    position:relative;
    z-index:2;
    margin-top:19px;
}

.chip {
    display:inline-block;
    padding:7px 10px;
    border:1px solid #39313f;
    border-radius:100px;
    color:#ddd5e5;
    font-size:9px;
    font-weight:600;
    margin-right:4px;
}

/* PROFILE */
.profile-card {
    background:#fff;
    border:1px solid var(--line);
    border-radius:27px;
    padding:14px;
    margin-top:14px;
}

.profile-photo {
    border-radius:20px;
    overflow:hidden;
    background:#eee8f7;
}

.profile-name {
    color:var(--ink);
    font-family:'Space Grotesk',sans-serif;
    font-size:19px;
    font-weight:700;
    margin:14px 4px 2px;
}

.profile-role {
    color:var(--muted);
    font-size:10px;
    margin:0 4px 3px;
}

/* SECTION HEAD */
.section-head {
    margin:31px 3px 14px;
}

.eyebrow {
    color:var(--purple);
    font-size:9px;
    font-weight:700;
    letter-spacing:1.8px;
}

.section-title {
    color:var(--ink);
    font-family:'Space Grotesk',sans-serif;
    font-size:26px;
    font-weight:700;
    letter-spacing:-1.2px;
    margin-top:4px;
}

.section-desc {
    color:var(--muted);
    font-size:11px;
    margin-top:3px;
}

/* STATS */
.stat-card {
    background:#fff;
    border:1px solid var(--line);
    border-radius:19px;
    padding:17px 15px;
    min-height:82px;
}

.stat-number {
    color:var(--purple);
    font-family:'Space Grotesk',sans-serif;
    font-size:25px;
    font-weight:700;
}

.stat-label {
    color:var(--muted);
    font-size:9px;
    margin-top:3px;
}

/* ABOUT CARDS */
.info-card {
    background:#fff;
    border:1px solid var(--line);
    border-radius:21px;
    padding:19px;
    margin-bottom:11px;
}

.info-icon {
    width:34px;height:34px;
    border-radius:11px;
    display:flex;
    align-items:center;
    justify-content:center;
    background:#f0e8ff;
    color:var(--purple);
    font-weight:700;
    margin-bottom:12px;
}

.info-title {
    color:var(--ink);
    font-family:'Space Grotesk',sans-serif;
    font-size:16px;
    font-weight:700;
}

.info-text {
    color:var(--muted);
    font-size:11px;
    line-height:1.8;
    margin-top:6px;
}

/* PROJECT */
.project-card {
    background:#fff;
    border:1px solid var(--line);
    border-radius:24px;
    padding:20px;
    margin-bottom:13px;
    position:relative;
    overflow:hidden;
    box-shadow:0 8px 25px rgba(32,20,50,.05);
}

.project-index {
    color:#a99fb1;
    font-size:9px;
    font-weight:700;
    letter-spacing:1.5px;
}

.project-title {
    color:var(--ink);
    font-family:'Space Grotesk',sans-serif;
    font-size:21px;
    font-weight:700;
    letter-spacing:-.7px;
    margin-top:8px;
}

.project-desc {
    color:var(--muted);
    font-size:11px;
    line-height:1.75;
    margin-top:6px;
}

.project-tag {
    display:inline-block;
    color:var(--purple);
    background:#f1e9ff;
    border-radius:7px;
    padding:5px 8px;
    font-size:8px;
    font-weight:700;
    margin:11px 3px 0 0;
}


/* PROJECT IMAGES */
.project-image {
    width:100%;
    height:190px;
    border-radius:17px;
    overflow:hidden;
    margin-bottom:17px;
    background:#eee8f7;
}

.project-image img {
    width:100%;
    height:100%;
    object-fit:cover;
    display:block;
    transition:transform .4s ease;
}

.project-card:hover .project-image img {
    transform:scale(1.05);
}

/* SKILLS */
.skill-card {
    background:#fff;
    border:1px solid var(--line);
    border-radius:18px;
    padding:15px 16px;
    margin-bottom:9px;
}

.skill-line {
    display:flex;
    justify-content:space-between;
    align-items:center;
}

.skill-name {
    color:var(--ink);
    font-size:12px;
    font-weight:700;
}

.skill-percent {
    color:var(--purple);
    font-size:10px;
    font-weight:700;
}

.skill-type {
    color:var(--muted);
    font-size:9px;
    margin-top:2px;
}

/* CONTACT */
.contact-card {
    background:var(--dark);
    border-radius:27px;
    padding:25px 22px;
    color:white;
}

.contact-card h2 {
    color:#fff;
    font-family:'Space Grotesk',sans-serif;
    font-size:29px;
    line-height:1;
    letter-spacing:-1.2px;
    margin:0;
}

.contact-card p {
    color:#aaa3b1;
    font-size:11px;
    line-height:1.8;
    margin:11px 0 18px;
}

.contact-row {
    border-top:1px solid #302a35;
    padding:11px 0 0;
    margin-top:8px;
    color:#eee;
    font-size:10px;
}

/* BUTTONS */
div.stButton > button, .stLinkButton > a, .stFormSubmitButton > button {
    border-radius:13px !important;
    min-height:42px !important;
    font-family:'DM Sans',sans-serif !important;
    font-size:10px !important;
    font-weight:700 !important;
    border:1px solid var(--line) !important;
    box-shadow:none !important;
}

div.stButton > button[kind="primary"],
.stFormSubmitButton > button {
    background:var(--purple) !important;
    color:#fff !important;
    border-color:var(--purple) !important;
}

div.stButton > button:hover {
    border-color:var(--purple) !important;
    color:var(--purple) !important;
}

.stLinkButton > a {
    background:var(--purple) !important;
    color:#fff !important;
    border-color:var(--purple) !important;
    text-decoration:none !important;
}

/* INPUTS */
.stTextInput input, .stTextArea textarea {
    border-radius:12px !important;
    border:1px solid var(--line) !important;
    background:#fff !important;
    font-size:11px !important;
}

.stTextInput label, .stTextArea label {
    font-size:10px !important;
    font-weight:600 !important;
}

[data-testid="stProgressBar"] > div > div {
    background:var(--purple) !important;
}

/* BOTTOM NAV */
.bottom-nav-space {height:12px;}

.footer {
    text-align:center;
    color:#aaa2b0;
    font-size:8px;
    margin-top:29px;
}

/* Extra-small phones */
@media (max-width:380px) {
    .block-container {padding-left:12px !important;padding-right:12px !important;}
    .hero h1 {font-size:38px;}
    .hero {padding:25px 21px;}
}
</style>
"""), unsafe_allow_html=True)

# -------------------- HEADER --------------------
st.markdown(textwrap.dedent("""
<div class="topbar">
    <div class="brand">My Portfolio<span class="brand-dot">.</span></div>
    <div class="available"><i></i> AVAILABLE</div>
</div>
"""), unsafe_allow_html=True)

# Compact navigation
navs = st.columns(5)
for col, page, icon in zip(
    navs,
    ["Home", "About", "Skills", "Projects", "Contact"],
    ["Home", "About", "Skills", "Projects", "Contact"],
):
    with col:
        if st.button(icon, key=f"nav_{page}", use_container_width=True):
            go(page)

# -------------------- HOME --------------------
if st.session_state.page == "Home":
    st.markdown(textwrap.dedent("""
<div class="hero">
    <div class="hero-kicker">STUDENT DEVELOPER</div>
    <h1>Hi, I'm<br><span>Jelaisa.</span></h1>
    <div class="hero-copy">
        I create simple digital experiences using Python,
        html, javascript, and css.
    </div>
    <div class="chips">
        <span class="chip">Python</span>
        <span class="chip">WebDev</span>
        <span class="chip">UI/UX</span>
    </div>
</div>
"""), unsafe_allow_html=True)

    st.write("")
    if st.button("Explore my work  →", key="explore", type="primary", use_container_width=True):
        go("Projects")

    if Path("profile.jpg").exists():
        st.markdown('<div class="profile-card"><div class="profile-photo">', unsafe_allow_html=True)
        st.image("profile.jpg", use_container_width=True)
        st.markdown(textwrap.dedent("""
</div>
<div class="profile-name">Jelaisa B. Daigdigan</div>
<div class="profile-role">Student · Python Developer · Web Developer</div>
</div>
"""), unsafe_allow_html=True)

    st.markdown(textwrap.dedent("""
<div class="section-head">
    <div class="eyebrow">OVERVIEW</div>
    <div class="section-title">A quick look.</div>
</div>
"""), unsafe_allow_html=True)

    a,b = st.columns(2)
    with a:
        st.markdown('<div class="stat-card"><div class="stat-number">01</div><div class="stat-label">About</div></div>', unsafe_allow_html=True)
    with b:
        st.markdown('<div class="stat-card"><div class="stat-number">03</div><div class="stat-label">Projects</div></div>', unsafe_allow_html=True)

    st.write("")
    a,b = st.columns(2)
    with a:
        st.markdown('<div class="stat-card"><div class="stat-number">02</div><div class="stat-label">Skills</div></div>', unsafe_allow_html=True)
    with b:
        st.markdown('<div class="stat-card"><div class="stat-number">04</div><div class="stat-label">Contact</div></div>', unsafe_allow_html=True)

# -------------------- ABOUT --------------------
elif st.session_state.page == "About":
    st.markdown(textwrap.dedent("""
<div class="section-head">
    <div class="eyebrow">01 / ABOUT</div>
    <div class="section-title">A little about me.</div>
    <div class="section-desc">Who I am and what I enjoy building.</div>
</div>
"""), unsafe_allow_html=True)

    st.markdown(textwrap.dedent("""
<div class="info-card">
    <div class="info-icon">✦</div>
    <div class="info-title">Hello! I'm Jelaisa.</div>
    <div class="info-text">
        I am a student passionate about learning, developing 
        innovative solutions, and continiously improving
        my skills. I enjoy turning ideas into
        simple and useful digital projects.
    </div>
</div>

<div class="info-card">
    <div class="info-icon">⌁</div>
    <div class="info-title">What I focus on</div>
    <div class="info-text">
        I focuses on building a strong foundation in programming,
        web development, databases, and basic IT concepts
        while gaining experience through simple hands-on projects.
    </div>
</div>

<div class="info-card">
    <div class="info-icon">＋</div>
    <div class="info-title">My goal</div>
    <div class="info-text">
        Keep learning, improve my development skills, and build
        projects that are useful, clean, and easy to understand.
    </div>
</div>
"""), unsafe_allow_html=True)

# -------------------- SKILLS --------------------
elif st.session_state.page == "Skills":
    st.markdown(textwrap.dedent("""
<div class="section-head">
    <div class="eyebrow">02 / SKILLS</div>
    <div class="section-title">My toolkit.</div>
    <div class="section-desc">Tools and technologies I'm working with.</div>
</div>
"""), unsafe_allow_html=True)

    skills = [
        ("Python", "Programming", 70),
        ("HTML", "Web Structure", 85),
        ("CSS", "Web Styling", 80),
        ("Figma", "UI/UX Design", 85),
        ("JavaScript", "Interactivity", 75),
        ("Git", "Version Control", 80),
    ]
    for name, kind, value in skills:
        st.markdown(
            f'<div class="skill-card"><div class="skill-line"><span class="skill-name">{name}</span>'
            f'<span class="skill-percent">{value}%</span></div>'
            f'<div class="skill-type">{kind}</div></div>',
            unsafe_allow_html=True,
        )
        st.progress(value / 100)

# -------------------- PROJECTS --------------------
elif st.session_state.page == "Projects":
    st.markdown(textwrap.dedent("""
<div class="section-head">
    <div class="eyebrow">03 / WORK</div>
    <div class="section-title">Selected projects.</div>
    <div class="section-desc">Some things I've built as a student developer.</div>
</div>
"""), unsafe_allow_html=True)

    # ============================================================
    # YOUR OWN PROJECT PICTURES
    # Put these image files in the SAME FOLDER as this Python file.
    # Portrait or landscape is fine. The original proportions are kept.
    # Change only the filenames below if you use different names.
    # ============================================================
    CAR_RENTAL_IMAGE = "car-rental.jpg"
    ONLINE_ENROLLMENT_IMAGE = "online-enrollment.jpg"

    # PROJECT 01
    st.markdown('<div class="project-card">', unsafe_allow_html=True)

    if Path(CAR_RENTAL_IMAGE).exists():
        st.image(CAR_RENTAL_IMAGE, use_container_width=True)
    else:
        st.info("Put your Car Rental picture here: car-rental.jpg")

    st.markdown(textwrap.dedent("""
<div class="project-index">PROJECT 01</div>
<div class="project-title">Car Rental Management System</div>
<div class="project-desc">
    A digital car rental platform designed to make vehicle reservations,
    customer information, rental records, and car management easier to organize.
</div>
<div>
    <span class="project-tag">HTML</span>
    <span class="project-tag">CSS</span>
    <span class="project-tag">JavaScript</span>
</div>
"""), unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("View details  →", key="view_car_rental", use_container_width=True):
        st.info(
            "The Car Rental Management System is designed to manage vehicles, "
            "customers, reservations, rental records, and available cars in one organized platform."
        )

    # PROJECT 02
    st.markdown('<div class="project-card">', unsafe_allow_html=True)

    if Path(ONLINE_ENROLLMENT_IMAGE).exists():
        st.image(ONLINE_ENROLLMENT_IMAGE, use_container_width=True)
    else:
        st.info("Put your Online Enrollment picture here: online-enrollment.jpg")

    st.markdown(textwrap.dedent("""
<div class="project-index">PROJECT 02</div>
<div class="project-title">Online Enrollment System</div>
<div class="project-desc">
    An online enrollment platform that allows students to submit their information,
    choose programs, and manage enrollment requirements digitally.
</div>
<div>
    <span class="project-tag">Python</span>
    <span class="project-tag">Streamlit</span>
    <span class="project-tag">Database</span>
</div>
"""), unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("View details  →", key="view_enrollment", use_container_width=True):
        st.info(
            "The Online Enrollment System provides students with a convenient way "
            "to submit enrollment information, select programs, and manage enrollment requirements."
        )

# -------------------- CONTACT --------------------
elif st.session_state.page == "Contact":
    st.markdown(textwrap.dedent("""
<div class="section-head">
    <div class="eyebrow">04 / CONTACT</div>
    <div class="section-title">Let's connect.</div>
    <div class="section-desc">Have an idea or want to collaborate?</div>
</div>

<div class="contact-card">
    <h2>Say hello. 👋</h2>
    <p>
        I'm open to student projects, collaboration, and opportunities
        to learn and build.
    </p>
    <div class="contact-row">✉ &nbsp; jelaisadaigdigan17@gmail.com</div>
    <div class="contact-row">☎ &nbsp; +63 909 976 3104</div>
    <div class="contact-row">⌖ &nbsp; Philippines</div>
</div>
"""), unsafe_allow_html=True)

    st.write("")
    st.link_button(
        "Send me an email  →",
        "mailto:jelaisadaigdigan17@gmail.com",
        use_container_width=True,
    )

    st.write("")
    with st.form("contact_form"):
        st.markdown('<div class="info-title" style="margin-bottom:12px;">Quick message</div>', unsafe_allow_html=True)
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message", height=120)
        submit = st.form_submit_button("Submit message  →", use_container_width=True)

        if submit:
            if not name or not email or not message:
                st.warning("Please complete all fields.")
            elif "@" not in email:
                st.warning("Please enter a valid email.")
            else:
                st.success("Your message form was submitted.")

st.markdown('<div class="footer">Jelaisa B. Daigdigan · Built with Python + Streamlit</div>', unsafe_allow_html=True)
