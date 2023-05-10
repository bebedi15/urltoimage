import requests
import os
from datetime import datetime
import colorama
from loguru import logger


colorama.init()


url_file = 'urls.txt'
output_dir = 'output'
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
output_file = f'output_{timestamp}.jpg'


if not os.path.exists(output_dir):
    os.makedirs(output_dir)


with open(url_file, 'r') as f:
    urls = list(set(f.readlines()))


for i, url in enumerate(urls):
    try:
        response = requests.get(url.strip(), stream=True)
        response.raise_for_status()
        with open(os.path.join(output_dir, f'{i}_{output_file}'), 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        logger.info(f"{colorama.Fore.MAGENTA}[log]{colorama.Style.RESET_ALL} Downloaded image: {url.strip()}")
    except Exception as e:
        logger.error(f"{colorama.Fore.RED}[err]{colorama.Style.RESET_ALL} Failed to download image: {url.strip()}. Error message: {str(e)}")

logger.info(f"{colorama.Fore.GREEN}[ok]{colorama.Style.RESET_ALL} Done!")
