import requests
response = requests.get("https://api.github.com/users/avielb/repos")

print(response.status_code)
print("*********************")
print("Name ID content in JSON")
repos_list = response.json()
for repo in repos_list:
    print(repo["name"])
print("*********************")