# ANSWERS

## 1. How to run

### Requirements

- Python 3 installed
- Internet connection

### Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

### Run

```bash
python main.py
```

---

## 2. Stack choice

I chose Python for this task because it allows rapid development and has strong support for HTTP requests and CLI applications.

The `requests` library made API communication simple and reliable, while the `rich` library helped create a cleaner command-line interface for a better user experience.

I selected a CLI-based approach because it keeps the project lightweight and easy to run on any machine without requiring browser setup or deployment.

A worse choice for this task would have been a lower-level language like C because the task focuses more on API integration, error handling, and usability rather than low-level memory management or performance optimization.

---

## 3. One real edge case

One important edge case handled in this project is API timeout handling.

### File and line reference

File: `main.py`

Lines: Inside the `fetch_user()` function:

```python
except requests.exceptions.Timeout:
    console.print("[red]Request timed out. The API is taking too long to respond.[/red]")
    return None
```

This prevents the application from crashing or freezing if the GitHub API becomes slow or unresponsive.

Without this handling, the user would experience a poor experience where the application might hang indefinitely or terminate unexpectedly.

Another edge case handled is invalid user input such as empty usernames or usernames containing spaces.

---

## 4. AI usage

I used ChatGPT during development for:
- Brainstorming project ideas
- Improving README structure
- Refining error handling logic
- Reviewing CLI design decisions

One example where I modified the AI-generated output was simplifying the exception handling structure.

The original suggestion used more nested logic and additional abstraction, but I simplified it into smaller direct checks to improve readability and make the code easier to maintain and explain.

I also adjusted some variable names and output formatting to make the CLI cleaner and more user-friendly.

---

## 5. Honest gap

One thing that could still be improved is the repository analysis depth.

Currently, the application only calculates total stars and the most-used programming language. With another day, I would add:
- Repository sorting
- Activity analysis
- Commit frequency tracking
- Exporting reports to JSON or CSV
- Better visual charts for comparisons

I would also improve automated testing coverage for API failure scenarios.