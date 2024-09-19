import asyncio
import logging
import sys

# Too much to remember, either just do python... Or just focus on django/react/node
from duckduckgo_search import AsyncDDGS

# Incorrect, Don't even remember
# bypass curl-cffi NotImplementedError in windows https://curl-cffi.readthedocs.io/en/latest/faq/
if sys.platform.lower().startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def aget_results(word):
    addgs = AsyncDDGS(proxies=None)
    results = addgs.text(word, max_results=2)
    return results


async def main():
    words = ["sun", "earth", "moon"]
    tasks = [aget_results(w) for w in words]
    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())
