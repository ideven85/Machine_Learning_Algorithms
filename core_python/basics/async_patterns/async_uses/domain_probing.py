import asyncio
import socket
import sys
from keyword import kwlist


async def probe_domain(domain):
    loop = asyncio.get_running_loop()
    try:
        address = await loop.getaddrinfo(domain, None)

    except socket.gaierror as e:

        return domain, False
    return address, True


async def main():
    names = [name for name in kwlist if len(name) <= 4]
    domains = [f"{name}.dev".lower() for name in names] + [
        "wikipedia.org",
        "twitter.com",
    ]
    coros = [probe_domain(domain) for domain in domains]
    for coro in asyncio.as_completed(coros):
        domain, found = await coro
        mark = "Exists: " if found else "Not found "
        print(f"{mark}{domain}")


if __name__ == "__main__":
    asyncio.run(main())
