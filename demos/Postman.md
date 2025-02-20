Open Postman and create a new request.

Set the request type to GET.

Enter the URL: https://api.github.com/orgs/YOUR_ORG/settings/billing/actions

Add Headers:

Key: Accept, Value: application/vnd.github+json
Key: X-GitHub-Api-Version, Value: 2022-11-28
Add Authorization:

Go to the Authorization tab.
Select Bearer Token from the Type dropdown.
Enter your GitHub token in the Token field.
Send the request by clicking the Send button.