import miniflux
from typing import Any, Dict, List
from ConfigLoader import ConfigLoader

# write a function that connects to miniflux client using api key and url
def connect_miniflux(url: str, api_key: str) -> miniflux.Client:
    return miniflux.Client(url, api_key=api_key)

def get_feed(client: miniflux.Client, feed_id: int) -> Dict:
    return client.get_feed(feed_id)

def get_stared_entries(client: miniflux.Client) -> Dict:
    return client.get_entries(starred=True)
    # return client.get_entries(starred=True, limit=10)

def test():

    config_loader = ConfigLoader()
    
    # connect to miniflux client using config
    config = config_loader.get_config()
    miniflux_config = config["miniflux"]
    client: miniflux.Client = connect_miniflux(
        miniflux_config["url"], miniflux_config["api"]
    )
    

    feeds: List[Dict] = client.get_feeds()
    
    starred_entries: Dict = get_stared_entries(client)

    # print the feeds title
    entries: Dict = get_stared_entries(client)
    
    print(f"There are {len(entries['entries'])} entries")
    print(f"Reported from totoal is {entries['total']}")

if __name__ == "__main__":
    test()
