#zad5
import asyncio

async def main(N) -> None:
    for i in range (1,N+1):
        await asyncio.sleep(1)
        liczba = Fibbonaci(i)
        print(liczba)

def Fibbonaci(N) -> int:
    if (N==1 or N==2):
        return 1
    else:
        pierwsza = Fibbonaci(N-2)
        druga = Fibbonaci(N-1)
        suma = pierwsza + druga
        return suma

if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main(7))