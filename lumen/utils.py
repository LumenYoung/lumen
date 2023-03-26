import os

def notify(title:str, notification:str, icon:str="arch")-> None:
    cmd = f"notify-send '{title}' '{notification}' --icon={icon}"
    os.system(cmd)

def print_calendars_demo(calendars):
    """
    This example prints the name and URL for every calendar on the list
    """
    if calendars:
        ## Some calendar servers will include all calendars you have
        ## access to in this list, and not only the calendars owned by
        ## this principal.
        print("your principal has %i calendars:" % len(calendars))
        for c in calendars:
            print("    Name: %-36s  URL: %s" % (c.name, c.url))
    else:
        print("your principal has no calendars")

def main():
    notify("test", "test")
    
if __name__ == "__main__":
    main()