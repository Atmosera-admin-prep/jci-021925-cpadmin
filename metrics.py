import requests
import sys
import os

def get_github_token():
    token = input("Enter your GitHub token (or press Enter to use the environment variable): ")
    if not token:
        token = os.getenv("GITHUB_TOKEN")
        if not token:
            print("GitHub token is required.")
            sys.exit(1)
    return token

def get_org_name():
    org_name = input("Enter the organization name (default: Atmosera-CoPilot-Dev): ")
    return org_name if org_name else "Atmosera-CoPilot-Dev"

def get_team_name():
    team_name = input("Enter the team name (default: sec-man): ")
    return team_name if team_name else "sec-man"

def choose_operation():
    print("Choose an operation:")
    print("1. Get the billing information for the organization")
    print("2. Get all copilot business seat assignments for the organization")
    print("3. Get copilot seat details for a specific user")
    print("4. Add a team to the GitHub subscription for the organization")
    print("5. Remove a team from the GitHub subscription for the organization")
    print("6. Quit")
    choice = input("Enter your choice (1/2/3/4/5/6): ")
    return choice

def get_billing_info(org_name, token):
    url = f"https://api.github.com/orgs/{org_name}/copilot/billing"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Failed to get billing information: {response.status_code} - {response.text}")

def get_seat_assignments(org_name, token):
    url = f"https://api.github.com/orgs/{org_name}/copilot/billing/seats"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Failed to get seat assignments: {response.status_code} - {response.text}")

def get_seat_details_for_user(org_name, token, username):
    url = f"https://api.github.com/orgs/{org_name}/members/{username}/copilot"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Failed to get seat details for user {username}: {response.status_code} - {response.text}")

def add_team_to_subscription(org_name, team_name, token):
    url = f"https://api.github.com/orgs/{org_name}/copilot/billing/selected_teams"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    data = {
        "selected_teams": [team_name]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print(f"Successfully added team {team_name} to the subscription.")
    else:
        print(f"Failed to add team {team_name} to the subscription: {response.status_code} - {response.text}")

def remove_team_from_subscription(org_name, team_name, token):
    url = f"https://api.github.com/orgs/{org_name}/copilot/billing/selected_teams/{team_name}"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f"Successfully removed team {team_name} from the subscription.")
    else:
        print(f"Failed to remove team {team_name} from the subscription: {response.status_code} - {response.text}")

def main():
    token = get_github_token()
    org_name = get_org_name()
    while True:
        choice = choose_operation()
        if choice == '1':
            get_billing_info(org_name, token)
        elif choice == '2':
            get_seat_assignments(org_name, token)
        elif choice == '3':
            username = input("Enter the username: ")
            get_seat_details_for_user(org_name, token, username)
        elif choice == '4':
            team_name = get_team_name()
            add_team_to_subscription(org_name, team_name, token)
        elif choice == '5':
            team_name = get_team_name()
            remove_team_from_subscription(org_name, team_name, token)
        elif choice == '6':
            print("Quitting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")

if __name__ == "__main__":
    main()