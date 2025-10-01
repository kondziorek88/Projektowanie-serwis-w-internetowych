#zad 1
import asyncio
async def main() -> None:
    await asyncio.sleep(2)
    print("Oczekiwanie zakończone")

if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())