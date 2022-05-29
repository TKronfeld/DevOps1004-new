import names
import requests
from selenium import webdriver

# Testing Github API - Create a program in python that goes to the following API and
# checks that at least 5 git repositories exists - https://api.github.com/users/avielb/repos
print("******* Testing Github API **************")
response = requests.get("https://api.github.com/users/avielb/repos")
assert len(response.json()) > 5
print("*********************")
# Testing agify API - Create a program in python that generates 3 random names and
# checks that the age from the reply in this link: https://api.agify.io/?name=<name> is
# between 0 - 120
print("******* Testing agify API **************")
my_names = []
for i in range(3):
    my_link = "https://api.agify.io/?name=" + names.get_first_name()
    my_response = requests.get(my_link)
    my_repos_list = my_response.json()
    if my_repos_list['age'] in range(0, 120):
        my_names.append(i)
assert len(my_names) != 0
print("*********************")
# Testing universities API - Go to http://universities.hipolabs.com/search?country=Israel
# and make sure that israel has at least 5 universities
print("******* Testing universities API **************")
uni_response = requests.get("http://universities.hipolabs.com/search?country=Israel")
assert len(uni_response.json()) > 5
print("*********************")

print("******* UI Testing **************")
my_driver1 = webdriver.Chrome()
my_driver2 = webdriver.Chrome()
my_driver1.get("https://www.ycombinator.com/")
my_driver2.get("https://hub.docker.com")
assert my_driver1.title == "Y Combinator"
assert my_driver2.title == "Docker Hub Container Image Library |App Containerization"
print("*********************")