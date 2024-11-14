import asyncio


async def create_file(file_name):
    text = ["Hi my name is Khan"]
    with open(file_name, "w+") as f:
        for t in 5*text:
            f.write(t+"\n")
    await asyncio.sleep(1)

async def main():
    await create_file("test.txt")


if __name__ == "__main__":
    asyncio.run(main())
