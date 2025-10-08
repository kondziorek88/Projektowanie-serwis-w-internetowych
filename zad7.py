import asyncio


async def main() ->None:
    kurciok = [krojenie,gotowanie,smazenie]
    salatka = [krojenie, krojenie, krojenie]
    schab = [smazenie, smazenie, smazenie]
    dania=[przygotowanie("kurczak", kurciok), przygotowanie("salatka", salatka), przygotowanie("schab", schab)]
    await asyncio.gather(*dania)
async def krojenie()->None:
    await asyncio.sleep(2)
    print("koniec krojenia")

async def gotowanie()->None:
    await asyncio.sleep(5)
    print("Koniec gotowania")

async def smazenie()->None:
    await asyncio.sleep(3)
    print("koniec smażenia")

async def przygotowanie(nazwa: str, etapy: list):
    print(f"\n kucharz gotuje{nazwa}")
    for etap in etapy:
        await etap()
    print(f"\nzakonczono gotwanie {nazwa}")
if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())