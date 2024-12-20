# Multi-Personality Agent (MPA)

This project that utilizes the `RoundRobinSwarm` model from [Swarms](https://github.com/kyegomez/swarms/) to simulate multiple personalities which tweet out dynamic content. By harnessing RoundRobinSwarm's distributed processing with multiple personalities (agents), this project allows a single agent to contain multiple personalities which have their own memories, perspectives, and style of content generated.

A live demo can be found here: https://x.com/SchizoSwarms

## 📚 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [How It Works](#how-it-works)
- [Example Use Case](#example-use-case)
- [Contributing](#contributing)
- [License](#license)

---

## ✨ Features

- Implements a **round-robin scheduling algorithm** for fair task distribution.
- Leverages **personalized AI agents** to mimic multiple personalities.
- Dynamic and customizable agent configurations stored in a JSON file.
- Easy extensibility for adding new personalities and adapting tasks beyond tweets.

---

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/schizoaidev/multi-personality-agent.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd multi-personality-agent
   ```
3. **Install required dependencies:**
   Use a Python virtual environment for dependency isolation:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Set up your OpenAI/X  API keys:**
   Ensure your API Keys are set in your environment variables:
   ```bash
   export OPENAI_API_KEY=""
   export X_CONSUMER=""
   export X_CONSUMER_SECRET=""
   export X_ACCESS_TOKEN=""
   export X_ACCESS_TOKEN_SECRET=""
   ```

5. **Create a `personalities.json` file:**
   Add the configuration for your agents (see [Configuration](#configuration) below).

---

## 📖 Usage

Run the script to begin generating tweets from your agents:
   ```bash
   python src/__init__.py
   ```
---

## ⚙️ Configuration

The project uses a `personalities.json` file to define agent configurations. An example format is as follows:

```json
[
    {
        "agent_name": "Motivational Speaker",
        "system_prompt": "You're a motivational speaker. Generate uplifting and inspiring tweets for your followers.",
        "agent_description": "Focus on positivity and inspiration.",
        "max_loops": 1,
        "autosave": true,
        "dashboard": false,
        "verbose": true,
        "streaming_on": true,
        "context_length": 500
    },
    {
        "agent_name": "Tech Enthusiast",
        "system_prompt": "You're a tech expert who loves sharing cutting-edge news about AI and technology advancements.",
        "agent_description": "Provide engaging tweets about technology and AI.",
        "max_loops": 1,
        "autosave": true,
        "dashboard": false,
        "verbose": true,
        "streaming_on": true,
        "context_length": 500
    }
]
```

To configure the swarm, add or modify the JSON file to include different personality types with unique `system_prompt` fields.

---

## 🧩 How It Works

1. ### **Agent Initialization**:
   The script reads the `personalities.json` file to load agent configurations. Each agent is instantiated with unique attributes such as its name, description, context focus, and maximum loop count.

2. ### **Round-Robin Distribution**:
   A `RoundRobinSwarm` is instantiated with the list of agents, and tasks are cyclically distributed to ensure fair participation. Each agent takes a turn tweeting based on the round-robin strategy.

3. ### **Tweet Generation**:
   From the list of agents, the swarm picks one to generate a tweet based on its personality and system prompt.

4. ### **Randomization (Optional)**:
   You can randomize the selection of agents for added variety, allowing the swarm to inject spontaneity into the output.

---

## 💡 Example Use Case

Imagine a Twitter account that mimics the voices of different characters or themes:

1. A **motivational speaker** tweets uplifting content for audience engagement.
2. A **tech enthusiast** generates tweets about AI and innovation.
3. A **sales agent** tweets persuasive content about automation tools.

By using this project, these tweets are seamlessly generated and rotated in a way that feels dynamic, natural, and engaging.

Sample Code for Tweeting:

```python
response = get_ai_response()
print("Tweeting as agent:", response)
# Here you can use a Twitter API wrapper like Tweepy to post the generated response.
```
---

## 🤝 Contributing

You are welcome to contribute to this project by:

1. Adding new agent personalities.
2. Improving task distribution logic.
3. Optimizing the integration with other APIs (e.g., Twitter API).
4. Enhancing documentation or providing examples for more use cases.

To contribute, fork the repository, make your changes, and create a pull request.

---

## 📜 License

This project is licensed under the MIT License. Feel free to use, modify, and distribute as you see fit.

## 🚀 Future Improvements

- **Twitter API Integration**: Automatically post generated tweets to a live Twitter account.
- **Task Customization**: Extend functionality for tasks beyond tweeting.
- **Personality Expansion**: Add more nuanced personalities for diverse use cases (e.g., humor, storytelling, etc.).

Happy tweeting! 
