import asyncio


async def name():

    print("Deven")
    await asyncio.sleep(2)


async def profession():
    print("Learning Python")
    await asyncio.sleep(5)
    print("Stupid")

async def main():
    await asyncio.gather(name(),profession())
    await profession()
    await name()

#asyncio.run(main())
asyncio.run(main()) # Cannot Write this... No idea why
#main()