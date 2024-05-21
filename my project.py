import datetime

def greet(name="world"):
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        message = "Good morning, "
    elif 12 <= current_hour < 18:
        message = "Good afternoon, "
    else:
        message = "Good evening, "
    print(f"{message}{name}!")

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    greet(user_name)
