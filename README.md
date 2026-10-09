# LangChain Breakfast Ideas Generator

A simple Python application using LangChain and OpenAI's `gpt-4o-mini` model to generate exactly five healthy breakfast ideas.

## Features

* Uses LangChain's `ChatOpenAI`.
* Generates five healthy breakfast ideas.
* Displays numbered ideas, one per line.
* Prints only the response text using `reply.content`.
* Reads the OpenAI API key from an environment variable.
* Uses `temperature=0` for more consistent results.

## Technologies Used

* Python
* LangChain
* LangChain OpenAI
* OpenAI API

## Setup and Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd breakfast
```

### 2. Create and activate a virtual environment

**Windows CMD:**

```cmd
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```cmd
python -m pip install langchain langchain-openai
```

### 4. Set your OpenAI API key

**Windows CMD:**

```cmd
set OPENAI_API_KEY=your_actual_api_key
```

Replace `your_actual_api_key` with your own API key.

**Security:** Never hard-code your API key or commit it to GitHub.

## Run the Application

```cmd
python breakfast.py
```

## Example Output

```text
1. Vegetable oats upma with peanuts
2. Greek yogurt with berries and chia seeds
3. Whole-wheat toast with scrambled eggs
4. Moong dal chilla with mint chutney
5. Overnight oats with banana and peanut butter
```

*The actual output may vary between runs.*

## Learning Outcomes

* Understand how to use LangChain's `ChatOpenAI`.
* Learn how `invoke()` returns an AI message object.
* Extract response text using `reply.content`.
* Control output formatting through prompt engineering.
* Use environment variables to protect API credentials.
* Explore model consistency using `temperature=0`.

## Project Structure

```text
breakfast/
├── breakfast.py
└── README.md
```

## Assignment

**Title:** LangChain Breakfast Ideas Generator

**Objective:** Generate five healthy breakfast ideas using LangChain and print only the model's response text.

**Submission:** Python source code, terminal screenshot, and a note comparing the results of two runs.

---

Created as part of the *Learn. Build. Operate.* assignment.
