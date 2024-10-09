import multiprocessing
import requests
import json

def downloader(i, url, queue, mutex):
    response = requests.get(url).json()
    response_len = len(json.dumps(response))
    with mutex:
        current_counter = queue.get()
        current_counter += response_len
        queue.put(current_counter)
    print("Thread " + str(i) + " downloaded " + str(response_len) + " chars from " + url)


def main():
    URLS = [
        'https://jsonplaceholder.typicode.com/posts',
        'https://jsonplaceholder.typicode.com/comments',
        'https://jsonplaceholder.typicode.com/albums',
        'https://jsonplaceholder.typicode.com/photos',
        'https://jsonplaceholder.typicode.com/todos',
        'https://jsonplaceholder.typicode.com/users'
        ]
    processes_list = []
    queue = multiprocessing.Queue()
    queue.put(0)
    mutex = multiprocessing.Lock()

    for i, url in enumerate(URLS):
        process = multiprocessing.Process(target = downloader, args=(i, url, queue, mutex))
        process.start()
        processes_list.append(process)
    
    for process in processes_list:
        process.join()
    
    print("Total number of chars downloaded is " + str(queue.get()))


if __name__ == "__main__":
    main()