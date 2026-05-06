# typing-speed-test
Typing speed test built with Python and Streamlit. Measures your characters per second and ranks you against all previous players. And u're LOUDLY announced disqualified for any mistake.

⌨️ Typing Speed Test
A browser-based typing speed test built with Python and Streamlit.
Type fast. Type accurate. One wrong character and you're disqualified.

🚀 Live Demo
👉 Play it here ← (update this after deploying)

🎮 How It Works

A random sentence is shown on screen
Type it exactly as shown
Hit Submit
If your input doesn't match exactly → Disqualified
If correct → your CPS (characters per second) is calculated
You get a rank based on your speed
Your score is compared against all previous players anonymously — no username needed


🏆 Rank System
RankSpeed🟢 Elite7+ CPS🔵 Fast5–7 CPS🟡 Intermediate3–5 CPS⚪ Beginner0–3 CPS
Your percentile is also shown — "faster than X% of all players"

🛠️ Built With

Python 3
Streamlit


📦 Run Locally
1. Clone the repo
bashgit clone https://github.com/shatlah-namiyah/typing-speed-test.git
cd typing-speed-test
2. Install dependencies
bashpip install -r requirements.txt
3. Run the app
bashstreamlit run app.py
Opens at localhost:8501 in your browser.

📁 Project Structure
typing-speed-test/
├── app.py            # Main application
├── requirements.txt  # Dependencies
├── scores.json       # Auto-generated, stores anonymous CPS scores
└── README.md

☁️ Deployed on Streamlit Cloud

▶️🤾‍♀️ play it here   https://typing-speed-test-here.streamlit.app



📝 License
MIT — free to use and modify.
