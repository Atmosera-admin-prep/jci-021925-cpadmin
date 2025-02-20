# GitHub CLI api
# https://cli.github.com/manual/gh_api

# authenticate to GitHub
gh auth login

# prompt the user for the organization name 'ORG_NAME'. The default value of the organization name is "Atmosera-CoPilot-Dev".
read -p "Enter the organization name (default: Atmosera-CoPilot-Dev): " ORG_NAME
ORG_NAME=${ORG_NAME:-Atmosera-CoPilot-Dev}

# prompt the user to choose an operation
echo "Choose an operation:"
echo "1. Get the billing information for the organization"
echo "2. Get all copilot business seat assignments for the organization"
echo "3. Get copilot seat details for a specific user"
echo "4. Quit"
read -p "Enter your choice (1/2/3/4): " CHOICE

case $CHOICE in
  1)
    echo "get the billing information for the $ORG_NAME organization:\n"
    gh api \
      -H "Accept: application/vnd.github+json" \
      -H "X-GitHub-Api-Version: 2022-11-28" \
      orgs/$ORG_NAME/copilot/billing
    ;;
  2)
    echo "get all copilot business seat assignments for the $ORG_NAME organization:\n"
    gh api \
      -H "Accept: application/vnd.github+json" \
      -H "X-GitHub-Api-Version: 2022-11-28" \
      orgs/$ORG_NAME/copilot/billing/seats
    ;;
  3)
    read -p "Enter the username: " USERNAME
    echo "get copilot seat details for $USERNAME in the $ORG_NAME organization:\n"
    gh api \
      -H "Accept: application/vnd.github+json" \
      -H "X-GitHub-Api-Version: 2022-11-28" \
      orgs/$ORG_NAME/members/$USERNAME/copilot
    ;;
  4)
    echo "Quitting..."
    exit 0
    ;;
  *)
    echo "Invalid choice. Please enter 1, 2, 3, or 4."
    ;;
esac



