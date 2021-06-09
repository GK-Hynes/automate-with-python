#! python3
# threaded_download_xkcd.py - Downloads XKCD comics using multiple threads

import requests, os, bs4, threading

# store comics in ./xkcd
os.makedirs('xkcd', exist_ok=True)

def download_xkcd(start_comic, end_comic):
    for url_number in range(start_comic, end_comic):
        # Download the page
        print(f'Downloading page https://xkcd.com/{url_number}...')
        res = requests.get(f'https://xkcd.com/{url_number}')
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        # Find the url of the comic image
        comic_elem = soup.select('#comic img')
        if comic_elem == []:
            print('Could not find comic image')
        else:
            comic_url = 'https:' + comic_elem[0].get('src')

            # Handle certain images
            if not comic_url.startswith('https://imgs.xkcd.com'):
                comic_url = 'https://xkcd.com' + comic_elem[0].get('src')

            # Download the image
            print(f'Downloading image {comic_url}')
            res = requests.get(comic_url)
            res.raise_for_status()

            # Save the image to ./xkcd
            image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()

# List all Thread objects
download_threads = []
# Loop 14 times, create 14 threads
for i in range(0, 140, 10):
    start = i
    end = i + 9
    # There is no comic 0, so set it to 1
    if start == 0:
        start = 1
    download_thread = threading.Thread(target=download_xkcd, args=(start, end))
    download_threads.append(download_thread)
    download_thread.start()

# Wait for all threads to end
for download_thread in download_threads:
    download_thread.join()
print('Done')