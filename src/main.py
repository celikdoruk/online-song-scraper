from extract import find_song_details
from sql import insert
from url_list import url_list

def main():
    for url in url_list:
        details = find_song_details(url)
        insert([
            details["song"],
            details["artist"],
            details["tempo"],
            details["song"],
            details["duration"],
        ])
        
if __name__ == "__main__":
    main()