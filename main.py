import requests
from collections import Counter
from rich.console import Console
from rich.table import Table

console = Console()

BASE_URL = "https://api.github.com/users"


def validate_username(username):
    username = username.strip()

    if not username:
        return False

    if " " in username:
        return False

    return True


def fetch_user(username):
    url = f"{BASE_URL}/{username}"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 404:
            console.print("[red]User not found.[/red]")
            return None

        if response.status_code != 200:
            console.print(f"[red]API Error: {response.status_code}[/red]")
            return None

        return response.json()

    except requests.exceptions.Timeout:
        console.print("[red]Request timed out. The API is taking too long to respond.[/red]")
        return None

    except requests.exceptions.ConnectionError:
        console.print("[red]Connection error. Please check your internet.[/red]")
        return None

    except Exception as e:
        console.print(f"[red]Unexpected error: {e}[/red]")
        return None


def fetch_repositories(username):
    url = f"{BASE_URL}/{username}/repos"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return []

        return response.json()

    except:
        return []


def analyze_repositories(repos):
    total_stars = 0
    languages = []

    for repo in repos:
        total_stars += repo.get("stargazers_count", 0)

        language = repo.get("language")

        if language:
            languages.append(language)

    most_used_language = "N/A"

    if languages:
        counter = Counter(languages)
        most_used_language = counter.most_common(1)[0][0]

    return total_stars, most_used_language


def display_user(data, total_stars, language):
    table = Table(title="GitHub Developer Analysis")

    table.add_column("Field", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Username", data.get("login", "N/A"))
    table.add_row("Name", str(data.get("name", "N/A")))
    table.add_row("Followers", str(data.get("followers", 0)))
    table.add_row("Following", str(data.get("following", 0)))
    table.add_row("Public Repositories", str(data.get("public_repos", 0)))
    table.add_row("Most Used Language", language)
    table.add_row("Total Stars", str(total_stars))
    table.add_row("Profile URL", data.get("html_url", "N/A"))

    console.print(table)


def compare_users():
    console.print("\n[yellow]Compare Two GitHub Users[/yellow]\n")

    user1 = input("Enter first username: ")
    user2 = input("Enter second username: ")

    if not validate_username(user1) or not validate_username(user2):
        console.print("[red]Invalid username input.[/red]")
        return

    data1 = fetch_user(user1)
    data2 = fetch_user(user2)

    if not data1 or not data2:
        return

    repos1 = fetch_repositories(user1)
    repos2 = fetch_repositories(user2)

    stars1, lang1 = analyze_repositories(repos1)
    stars2, lang2 = analyze_repositories(repos2)

    console.print("\n[bold cyan]Comparison Result[/bold cyan]\n")

    if stars1 > stars2:
        console.print(f"{user1} has more total stars.")
    elif stars2 > stars1:
        console.print(f"{user2} has more total stars.")
    else:
        console.print("Both users have equal stars.")

    if data1["followers"] > data2["followers"]:
        console.print(f"{user1} has more followers.")
    elif data2["followers"] > data1["followers"]:
        console.print(f"{user2} has more followers.")
    else:
        console.print("Both users have equal followers.")


def single_user_analysis():
    username = input("Enter GitHub username: ")

    if not validate_username(username):
        console.print("[red]Please enter a valid username.[/red]")
        return

    user_data = fetch_user(username)

    if not user_data:
        return

    repos = fetch_repositories(username)

    total_stars, language = analyze_repositories(repos)

    display_user(user_data, total_stars, language)


def main():
    while True:
        console.print("\n[bold blue]DevScope - GitHub Developer Analyzer[/bold blue]\n")

        console.print("1. Analyze GitHub User")
        console.print("2. Compare Two Users")
        console.print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            single_user_analysis()

        elif choice == "2":
            compare_users()

        elif choice == "3":
            console.print("[green]Goodbye![/green]")
            break

        else:
            console.print("[red]Invalid choice. Please try again.[/red]")


if __name__ == "__main__":
    main()