import caldav
from typing import List
from ConfigLoader import ConfigLoader
from utils import print_calendars_demo

# function to connect to caldav client using url and username and password
def connect_caldav(url: str, username: str, password: str) -> caldav.DAVClient:
    return caldav.DAVClient(url, username=username, password=password)

def get_calendars(client: caldav.DAVClient) -> List[caldav.Calendar]:
    principal: caldav.Principal = client.principal()
    calendars: List[caldav.Calendar] = principal.calendars()
    return calendars

def add_event_to_calendar(client: caldav.DAVClient, calendar_name: str, event: caldav.Event) -> None:
    principal: caldav.Principal = client.principal()
    calendars: List[caldav.Calendar] = principal.calendars()
    for calendar in calendars:
        if calendar.name == calendar_name:
            calendar.add_event(event)
            break
    
# display all events of given day
def get_events_of_day(client: caldav.DAVClient, calendar_name: str, day: str) -> List[caldav.Event]:
    principal: caldav.Principal = client.principal()
    calendars: List[caldav.Calendar] = principal.calendars()
    for calendar in calendars:
        if calendar.name == calendar_name:
            events: List[caldav.Event] = calendar.date_search(day)
            return events

def test_connect_caldav():
    
    config_loader = ConfigLoader()
    config = config_loader.get_config()
    caldav_config = config["caldav"]

    client: caldav.DAVClient = connect_caldav(
        caldav_config["url"], caldav_config["username"], caldav_config["password"]
    )
    
    principal: caldav.Principal = client.principal()
    
    calendars: List[caldav.Calendar] = principal.calendars()
    
    print_calendars_demo(calendars)

if __name__ == "__main__":
    test_connect_caldav()