# DevScope - GitHub Developer Analyzer

DevScope is a command-line application built with Python that analyzes GitHub users using the GitHub public API.

It allows users to:
- Analyze GitHub profiles
- Compare two GitHub developers
- View repository statistics
- Detect most-used programming languages
- Handle invalid input and API failures gracefully

---

## Features

- GitHub profile analysis
- Repository statistics
- User comparison
- Error handling
- Timeout handling
- Input validation
- Clean CLI interface

---

## Installation

Clone the repository:

```bash
git clone <your-repo-url>
```

Move into the project folder:

```bash
cd devscope
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python main.py
```

---

## Example Usage

### Analyze User

Enter a GitHub username to view:
- Followers
- Following
- Public repositories
- Total stars
- Most used language

### Compare Users

Compare:
- Followers
- Total repository stars

---

## Technologies Used

- Python
- Requests
- Rich
- GitHub REST API

---

## Error Handling

The project handles:
- Invalid usernames
- API timeouts
- API failures
- Connection issues
- Empty input

---

## API Used

GitHub REST API:
https://api.github.com