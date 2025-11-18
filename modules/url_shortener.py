import requests 
from urllib.parse import quote_plus # Used to parse URL and clean it

# is.gd API call
is_gd_path = "https://is.gd/create.php?format=simple&url="

# tinyurl API call
tinyutl_path = "https://tinyurl.com/api-create.php?url="

# Pretending to be a browser
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

def shorten(url: str):

    ## Checking if url is valid
    if not (url.startswith("https://") or url.startswith("http://")):
        return False

    for banned in ("localhost" , "127." , "192.168" , "10." , "172.16" , "0.0.0.0"):
        if banned in url.lower():
            return False


    # Shortening it
    safe_url = quote_plus(url)
    api_call = f"{is_gd_path}{safe_url}"
    request = requests.get(api_call ,headers=headers , timeout=5)  # If no response within 5sec, throws an error
    request.raise_for_status()
    
    # Returning the shortened url
    return request.text.strip()
    

if __name__ == "__main__":
    print(shorten("https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUJcmljayByb2xs")) # testing