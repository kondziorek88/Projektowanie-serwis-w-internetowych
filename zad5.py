#zad5
import asyncio
async def main(N) -> None:
    for i in range (1,N+1):
        liczba = await fib(i)
        print(liczba)
# async def fib(n: int) -> int:
#     lista = []
#     await asyncio.sleep(1)
#     lista.append(1)
#     print(lista[0])
#     if n>=2:
#         lista.append(1)
#         print(lista[1])
#         while (len(lista)<(n+1)):
#             i=2
#             n=lista[i-1]+lista[i-2]
#             lista.append(n)
#             i+=1
#             await asyncio.sleep(1)
#             print(lista[i])
#

async def fib(n: int) -> int:
    if n <= 2:
        await asyncio.sleep(1)
        return 1
    a=1
    b=1
    await asyncio.sleep(1)
    for _ in range(2, n):

        temp=b
        b=a+b
        a=temp
    return b



# def Fibbonaci(N) -> int:
#     if (N==1 or N==2):
#         return 1
#     else:
#         pierwsza = Fibbonaci(N-2)
#         druga = Fibbonaci(N-1)
#         suma = pierwsza + druga
#         return suma

if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main(7))

