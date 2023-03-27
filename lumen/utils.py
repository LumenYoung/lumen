import os
import timeit

def notify(title:str, notification:str, icon:str="arch")-> None:
    cmd = f"notify-send '{title}' '{notification}' --icon={icon}"
    os.system(cmd)


# write a decorator to time functions
def time_usage(func):
    def wrapper(*args, **kwargs):
        start = timeit.default_timer()
        result = func(*args, **kwargs)
        end = timeit.default_timer()
        # print in green: Time taken
        print(f"\033[1;32mTime usage: {end - start}\033[0m")
        return result
    return wrapper

def main():
    notify("test", "test")
    
if __name__ == "__main__":
    main()