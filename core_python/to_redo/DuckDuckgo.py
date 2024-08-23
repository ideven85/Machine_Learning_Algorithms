import asyncio
import logging
import sys

from duckduckgo_search import AsyncDDGS
#Incorrect, Don't even remember
# bypass curl-cffi NotImplementedError in windows https://curl-cffi.readthedocs.io/en/latest/faq/
if sys.platform.lower().startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def aget_results(word):
    addgs = AsyncDDGS(proxies=None)
    results = await addgs.text(word, max_results=100)
    return results


async def main():
    words = ["sun", "earth", "moon"]
    tasks = [aget_results(w) for w in words]
    results = await asyncio.gather(*tasks)
    print(results)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())
