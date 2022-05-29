from datetime import datetime
def my_decorator(func):
    def wrapper():
        print("something is happening before the function is called")
        print(datetime.now())
        func()
        print("something id happening after the function is called")
        print(datetime.now())

    return wrapper


@my_decorator
def say_whee():
    print("Whee!")


@my_decorator
def say_bark():
    print("Bark!")

say_whee()
say_bark()

# Instead
# def say_whee():
#    print("Whee!")

# say_whee = my_decorator(say_whee)
# say_whee()