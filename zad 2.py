#zad 2
import asyncio
async def main() -> None:
    await asyncio.sleep(1)
    print("Hello")
    await asyncio.sleep(1)
    print("world")

if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())