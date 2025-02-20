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
    org_name = input("Enter the organization name (default: Atmosera-adv-sec-prep): ")
    return org_name if org_name else "Atmosera-adv-sec-prep"

def get_repo_name():
    repo_name = input("Enter the repository name (default: swiss-cheese): ")
    return repo_name if repo_name else "swiss-cheese"

def list_security_advisories(org_name, repo_name, token):
    url = f"https://api.github.com/repos/{org_name}/{repo_name}/security-advisories"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    params = {
        "direction": "asc",
        "sort": "created"
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        advisories = response.json()
        for advisory in advisories:
            print(f"ID: {advisory['id']}")
            print(f"Summary: {advisory['summary']}")
            print(f"Description: {advisory['description']}")
            print(f"Published At: {advisory['published_at']}")
            print(f"Updated At: {advisory['updated_at']}")
            print(f"Severity: {advisory['severity']}")
            print(f"CVSS Score: {advisory['cvss']['score']}")
            print(f"CVSS Vector: {advisory['cvss']['vector']}")
            print(f"References: {advisory['references']}")
            print(f"Identifiers: {advisory['identifiers']}")
            print(f"State: {advisory['state']}")
            print("-" * 40)
    else:
        print(f"Failed to list security advisories: {response.status_code} - {response.text}")

def main():
    token = get_github_token()
    org_name = get_org_name()
    repo_name = get_repo_name()
    list_security_advisories(org_name, repo_name, token)

if __name__ == "__main__":
    main()