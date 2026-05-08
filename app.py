import streamlit as st
import time
import json
import os
import random

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(page_title="Typing Speed Test", page_icon="⌨️", layout="centered")

# ── Styling ────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Bebas+Neue&family=Inter:wght@300;400;600&display=swap');

html, body, [class*="css"] {
    background-color: #0a0a0a;
    color: #e0e0e0;
    font-family: 'Inter', sans-serif;
}

.title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 3.5rem;
    letter-spacing: 6px;
    color: #ffffff;
    text-align: center;
    margin-bottom: 0;
    line-height: 1;
}

.subtitle {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.85rem;
    color: #00ffff;
    text-align: center;
    letter-spacing: 3px;
    margin-bottom: 2.5rem;
}

.sentence-box {
    background: #111;
    border: 1px solid #222;
    border-left: 3px solid #39ff14;
    padding: 1.4rem 1.8rem;
    border-radius: 4px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 1.1rem;
    color: #c8ffb0;
    line-height: 1.8;
    margin-bottom: 1.5rem;
    letter-spacing: 0.5px;
}

.result-box {
    background: #000;
    border: 2px solid #39ff14;
    border-radius: 6px;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 0 30px rgba(57,255,20,0.12), inset 0 0 40px rgba(0,0,0,0.8);
    margin: 1.5rem auto;
    font-family: 'Share Tech Mono', monospace;
    max-width: 340px;
    aspect-ratio: 1 / 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.result-label {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1rem;
    letter-spacing: 4px;
    color: #7fffd4;
    margin-bottom: 0.3rem;
}

.result-cpm {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 3.2rem;
    color: #39ff14;
    line-height: 1;
    text-shadow: 0 0 20px rgba(57,255,20,0.5);
}

.result-unit {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.75rem;
    color: #e0ffff;
    letter-spacing: 2px;
    margin-bottom: 1.2rem;
}

.result-divider {
    width: 60px;
    height: 1px;
    background: #333;
    margin: 0.8rem auto;
}

.result-rank-label {
    font-family: 'Bebas Neue', sans-serif;
    letter-spacing: 4px;
    font-size: 0.9rem;
    color: #e0ffff;
}

.result-rank {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2.2rem;
    letter-spacing: 4px;
    color: #ffffff;
    text-shadow: 0 0 12px rgba(255,255,255,0.2);
}

.result-percentile {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.75rem;
    color: #39ff14;
    margin-top: 0.5rem;
    opacity: 0.8;
}

.disqualified-box {
    background: #0d0000;
    border: 2px solid #ff2222;
    border-radius: 6px;
    padding: 2rem;
    text-align: center;
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2rem;
    color: #ff2222;
    letter-spacing: 4px;
    box-shadow: 0 0 20px rgba(255,34,34,0.15);
    margin: 1.5rem 0;
}

.disq-sub {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.75rem;
    color: #552222;
    letter-spacing: 2px;
    margin-top: 0.5rem;
}

.stTextArea textarea {
    background: #0d0d0d !important;
    border: 1px solid #2a2a2a !important;
    border-radius: 4px !important;
    color: #e0e0e0 !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 1rem !important;
    caret-color: #39ff14 !important;
}

.stTextArea textarea:focus {
    border-color: #39ff14 !important;
    box-shadow: 0 0 0 1px #39ff14 !important;
}

.stButton > button {
    background: transparent;
    border: 1px solid #39ff14;
    color: #39ff14;
    font-family: 'Bebas Neue', sans-serif;
    letter-spacing: 3px;
    font-size: 1rem;
    padding: 0.6rem 2rem;
    border-radius: 3px;
    width: 100%;
    transition: all 0.2s;
}

.stButton > button:hover {
    background: #39ff14;
    color: #000;
}

.stat-pill {
    display: inline-block;
    background: #111;
    border: 1px solid #222;
    border-radius: 20px;
    padding: 0.25rem 0.9rem;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.75rem;
    color: #d3d3d3;
    margin: 0.2rem;
}

.timer-display {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.8rem;
    color: #39ff14;
    text-align: center;
    margin-bottom: 0.5rem;
    letter-spacing: 2px;
}
</style>
""", unsafe_allow_html=True)

# ── Sentence bank ──────────────────────────────────────────────────────────────
SENTENCES = [
    "The quick brown fox jumps over the lazy dog near the river.",
    "Speed is nothing without accuracy when the stakes are high.",
    "The human brain can generate about 20 watts of electrical power.",
    "A fast typist knows when to slow down and be precise.",
    "YouTube Shorts get roughly 6 to 10 times more views on average.",
    "Air pollution causes approximately 7M premature deaths per year worldwide.",
    "Consistency beats raw speed over a long career.",
    "Have you ever thought about death?",
    "Type with confidence and the speed will come naturally.",
    "Fall seven times, stand up eight. That is the Japanese way.",
]

SCORES_FILE = "scores.json"

# ── Helpers ────────────────────────────────────────────────────────────────────
def load_scores():
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, "r") as f:
            return json.load(f)
    return []

def save_score(cpm):
    scores = load_scores()
    scores.append(round(cpm, 1))
    with open(SCORES_FILE, "w") as f:
        json.dump(scores, f)

def get_percentile(cpm):
    scores = load_scores()
    if len(scores) <= 1:
        return None
    beaten = sum(1 for s in scores if s < cpm)
    return round((beaten / len(scores)) * 100, 1)

def get_rank(cpm):
    if cpm >= 400:
        return "ELITE"
    elif cpm >= 300:
        return "FAST"
    elif cpm >= 200:
        return "INTERMEDIATE"
    else:
        return "BEGINNER"

def reset_game():
    st.session_state.sentence = random.choice(SENTENCES)
    st.session_state.start_time = None
    st.session_state.result = None
    st.session_state.submitted = False

# ── Session state init ─────────────────────────────────────────────────────────
if "sentence" not in st.session_state:
    st.session_state.sentence = random.choice(SENTENCES)
if "start_time" not in st.session_state:
    # Start time is set ONCE when user submits
    # We use a JS timestamp approach via a hidden input trick
    st.session_state.start_time = None
if "result" not in st.session_state:
    st.session_state.result = None
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# ── UI ─────────────────────────────────────────────────────────────────────────
st.markdown('<div class="title">TYPE TEST</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">// MEASURE YOUR SPEED //</div>', unsafe_allow_html=True)

# Global stats
all_scores = load_scores()
if all_scores:
    st.markdown(
        f'<div style="text-align:center;margin-bottom:1rem;">'
        f'<span class="stat-pill">⚡ {len(all_scores)} games played</span>'
        f'<span class="stat-pill">avg {round(sum(all_scores)/len(all_scores), 1)} cpm</span>'
        f'</div>',
        unsafe_allow_html=True
    )

# Target sentence
st.markdown(f'<div class="sentence-box">{st.session_state.sentence}</div>', unsafe_allow_html=True)

# ── Game input ─────────────────────────────────────────────────────────────────
if not st.session_state.submitted:

    user_input = st.text_area(
        "Type here:",
        height=100,
        key="typing_input",
        placeholder="Start typing the text above — timer starts when you click START...",
        label_visibility="collapsed"
    )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        start = st.button("START", use_container_width=True)
    with col2:
        submit = st.button("SUBMIT", use_container_width=True)
    with col3:
        new_text = st.button("NEW TEXT", use_container_width=True)

    # START button locks the timer
    if start:
        if st.session_state.start_time is None:
            st.session_state.start_time = time.time()
            st.rerun()

    # Show timer status
    if st.session_state.start_time is not None:
        live_elapsed = round(time.time() - st.session_state.start_time, 1)
        st.markdown(f'<div class="timer-display">⏱ {live_elapsed}s — TIMER RUNNING</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="timer-display" style="color:#555;">Press START when ready</div>', unsafe_allow_html=True)

    if new_text:
        reset_game()
        st.rerun()

    if submit:
        if st.session_state.start_time is None:
            st.warning("Press START first to begin the timer.")
        elif not user_input or len(user_input.strip()) == 0:
            st.warning("Type something before submitting.")
        else:
            end_time = time.time()
            elapsed = end_time - st.session_state.start_time

            target = st.session_state.sentence.strip()
            typed = user_input.strip()

            if typed != target:
                st.session_state.result = {"disqualified": True}
            else:
                cpm = round((len(typed) / elapsed) * 60, 1)
                wpm = round(cpm / 5, 1)
                save_score(cpm)
                percentile = get_percentile(cpm)
                rank = get_rank(cpm)
                st.session_state.result = {
                    "disqualified": False,
                    "cpm": cpm,
                    "wpm": wpm,
                    "rank": rank,
                    "percentile": percentile,
                    "elapsed": round(elapsed, 2),
                    "chars": len(typed),
                }

            st.session_state.submitted = True
            st.rerun()

# ── Results ────────────────────────────────────────────────────────────────────
if st.session_state.submitted and st.session_state.result:
    r = st.session_state.result

    if r["disqualified"]:
        st.markdown("""
        <div class="disqualified-box">
            ✕ DISQUALIFIED
            <div class="disq-sub">TEXT DOES NOT MATCH — TRY AGAIN</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        percentile_html = (
            f'<div class="result-percentile">faster than {r["percentile"]}% of players</div>'
            if r["percentile"] is not None
            else '<div class="result-percentile">first result recorded</div>'
        )

        st.markdown(f"""
        <div class="result-box">
            <div class="result-label">YOUR SPEED</div>
            <div class="result-cpm">{r['cpm']}</div>
            <div class="result-unit">CHARACTERS PER MINUTE</div>
            <div class="result-divider"></div>
            <div class="result-rank-label">YOUR RANK</div>
            <div class="result-rank">{r['rank']}</div>
            {percentile_html}
        </div>
        """, unsafe_allow_html=True)

        st.markdown(
            f'<div style="text-align:center;">'
            f'<span class="stat-pill">⏱ {r["elapsed"]}s</span>'
            f'<span class="stat-pill">{r["chars"]} chars</span>'
            f'<span class="stat-pill">📊 {r["wpm"]} WPM</span>'
            f'</div>',
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("PLAY AGAIN", use_container_width=True):
        reset_game()
        st.rerun()
