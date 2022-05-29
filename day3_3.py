import requests

def save_name():
    n = input("Get your file name: ")
    my_file = open ("names.txt", "a")
    my_file.write(f"{n}\n")


def show_names():
    with open("names.txt") as my_file:  #temprorary opening
        for line in my_file.readlines():
            print(f"hello {line}", end ='')


def url_caller(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(f"{url} is OK")

def call_urls():
    with open("urls.txt") as urls:
        for line in urls.readlines():
            url_caller(line.strip())

save_name()
call_urls()
