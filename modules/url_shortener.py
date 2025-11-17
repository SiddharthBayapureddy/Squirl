import requests 
from urllib.parse import quote_plus # Used to parse URL and clean it

# is.gd API call
is_gd_path = "https://is.gd/create.php?format=simple&url="

def shorten(url: str):

    ## Checking if url is valid
    if not (url.startswith("https://") or url.startswith("http://")):
        return False

    for banned in ("localhost" , "127." , "192.168" , "10." , "172.16" , "0.0.0.0"):
        if banned in url.lower():
            return False


    # Shortening it
    api_call = f"{is_gd_path}{url}"
    request = requests.get(api_call , timeout=5)  # If no response within 5sec, throws an error
    request.raise_for_status()
    
    # Returning the shortened url
    return request.text.strip()
    

if __name__ == "__main__":
    print(shorten("https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUJcmljayByb2xs")) # testing