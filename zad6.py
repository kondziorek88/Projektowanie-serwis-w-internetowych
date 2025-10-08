#zad6
import asyncio
import random
async def fetch(delay: int):
    await asyncio.sleep(delay)
    wynik = random.randint(1,20)
    print(wynik)
    return wynik

async def main() -> None:
    lista = [1,3,2,5]
    kolejne = [fetch(d) for d in lista]
    wynik = await asyncio.gather(*kolejne)
    print("wszystkie wyniki")
    for i in wynik:
        print(i)

if __name__ == "__main__":
    asyncio.run(main())