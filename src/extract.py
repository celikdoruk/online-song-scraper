# type: ignore

import requests

from bs4 import BeautifulSoup

def find_song_details(url: str) -> dict:
    html = requests.get(url)
    markup = str(html.text)
    soup = BeautifulSoup(markup, "html.parser") 

    def find_tempo():
        for dt in soup.find_all("dt"): # dt stands for description term in html
            if dt.get_text(strip=True) == "Tempo (BPM)": 
                tempo = dt.find_next_sibling("dd").get_text(strip=True) # dd stands for description detail 
                return tempo # dl stands for description list (paired containers)
                

    def find_key():
        for dt in soup.find_all("dt"): 
                    if dt.get_text(strip=True) == "Key": 
                        key = dt.find_next_sibling("dd").get_text(strip=True) 
                        return key 
                        
    def find_duration():
        for dt in soup.find_all("dt"): 
                    if dt.get_text(strip=True) == "Duration": 
                        duration = dt.find_next_sibling("dd").get_text(strip=True)
                        return duration
                        

    def find_artist():
        try:
            artist = soup.find("h2").find_next("a").get_text(strip=True)
        except Exception:
            artist = "notfound"
        return artist

    def find_song():
        song = soup.find("h1").get_text(strip=True)
        return song

    total_details = {
        "tempo": find_tempo(),
        "key": find_key(),
        "duration": find_duration(),
        "artist": find_artist(),
        "song": find_song()
    }

    return total_details
