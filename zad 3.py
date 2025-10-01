#zad 3
import asyncio
async def pierwsza():
    await asyncio.sleep(3)
    return("Pierwsza skonczyła")

async def druga():
    await asyncio.sleep(1)
    return("Druga skończyła")

async def main():
    pierw = await pierwsza()
    print(pierw)
    drug = await druga()
    print(drug)

if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())