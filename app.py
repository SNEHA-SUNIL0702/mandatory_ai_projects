import streamlit as st
import requests
import wikipedia
st.markdown("""
    <style>
    .main {
        background-color: #fff8f0;
        padding: 20px;
        border-radius: 10px;
    }
    .title {
        color: #ff5e5e;
        font-size: 36px;
        font-weight: bold;
        text-align: center;
    }
    .caption {
        color: #6c757d;
        text-align: center;
        margin-bottom: 20px;
    }
    .chat-box {
        background-color: #f9f1f0;
        border-left: 4px solid #ff7a7a;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

def get_weather(city):
    api_key = "2c0bdc8c9184b5f12e1f12e4b6f1261f"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            return f"🌤️ Weather in {city.title()}:\nTemperature: {temp}°C\nCondition: {desc}"
        else:
            return f"⚠️ Could not get weather for '{city}'."
    except:
        return "⚠️ Weather service error."

def get_wiki_summary(topic):
    try:
        summary = wikipedia.summary(topic, sentences=2)
        return f"📚 {summary}"
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Too many results. Try something more specific: {e.options[:3]}"
    except:
        return "⚠️ Could not fetch information from Wikipedia."


# Store tasks in Streamlit session
if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.markdown('<div class="title">💬 Smart Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="caption">🌸 Ask me anything! Try "quote of the day", "weather in Kochi", or "who is Spiderman"</div>', unsafe_allow_html=True)


user_input = st.text_input("Enter your message", "")

def get_quote_of_the_day():
    response = requests.get('https://api.quotable.io/random', verify=False)
    if response.status_code == 200:
        data = response.json()
        quote = data.get('content')
        author = data.get('author')
        return f'🌟 "{quote}" - {author}'
    else:
        return '⚠️ Could not fetch quote.'

def process_input(user_input):
    user_input = user_input.lower()

    if "quote" in user_input:
        return get_quote_of_the_day()
        #return f'<div class="chat-box">{get_quote_of_the_day()}</div>'


    elif "add task" in user_input:
        task = user_input.replace("add task", "").strip()
        st.session_state.tasks.append(task)
        return f"✅ Task added: {task}"
        #return f'<div class="chat-box">✅ Task added: {task}</div>'


    elif "show tasks" in user_input:
        if st.session_state.tasks:
            return "📝 Tasks:\n" + "\n".join(f"- {t}" for t in st.session_state.tasks)
        else:
            return "📭 No tasks found."

    elif "clear tasks" in user_input:
        st.session_state.tasks.clear()
        return "🧹 All tasks cleared."
    elif "weather in" in user_input:
        city = user_input.replace("weather in", "").strip()
        return get_weather(city)

    elif "what is" in user_input or "who is" in user_input:
        topic = user_input.replace("what is", "").replace("who is", "").strip()

        return get_wiki_summary(topic)


    else:
        return "🤔 Try: 'add task', 'show tasks', 'quote of the day'."

if user_input:
    st.markdown(process_input(user_input))
