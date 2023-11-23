import aiohttp
import asyncio
import time
import re

title_pattern = r"<title>(.*?)</title>"

async def find_titles(content):
    titles = re.findall(title_pattern, content)
    return titles

async def fetch_page_content(session, url, semaphore):
    async with semaphore:
        async with session.get(url) as response:
            response.raise_for_status()
            page_content = await response.text()
            # Call find_titles immediately after fetching the content
            titles = await find_titles(page_content)
            print(f"Titles for {url}: {titles}")
            return page_content

async def main():
    urls = ["http://google.com", "http://youtube.com",] * 5
    batch_size = 5  # Adjust the batch size based on your preferences

    async with aiohttp.ClientSession() as session:
        semaphore = asyncio.Semaphore(batch_size)
        tasks = [fetch_page_content(session, url, semaphore) for url in urls]

        contents = await asyncio.gather(*tasks)
        # You can still gather titles if needed for further processing
        title_tasks = [find_titles(content) for content in contents]
        titles = await asyncio.gather(*title_tasks)

        # If you want to access all titles together
        print("All Titles:", titles)

# Run the event loop
if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print(f"Time Consumed: {end_time - start_time}")
