import threading
import requests
import json

URLS = [
        'https://jsonplaceholder.typicode.com/posts',
        'https://jsonplaceholder.typicode.com/comments',
        'https://jsonplaceholder.typicode.com/albums',
        'https://jsonplaceholder.typicode.com/photos',
        'https://jsonplaceholder.typicode.com/todos',
        'https://jsonplaceholder.typicode.com/users'
        ]
chars_len_list = [0]*len(URLS)


def downloader(i, url):
    global chars_len_list
    response = requests.get(url).json()
    chars_len_list[i] = len(json.dumps(response))
    print("Thread " + str(i) + " downloaded " + str(chars_len_list[i]) + " chars from " + url)
    

def main():
    threads_list = []

    for i, url in enumerate(URLS):
        thread = threading.Thread(target = downloader, args=(i, url))
        thread.start()
        threads_list.append(thread)
    
    for thread in threads_list:
        thread.join()
    
    print("Total number of chars downloaded is " + str(sum(chars_len_list)))


if __name__ == "__main__":
    main()