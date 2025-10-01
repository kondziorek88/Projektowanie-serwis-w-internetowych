#zad6
import asyncio
import random
async def fetch(delay: int):
    await asyncio.sleep(delay)
    return random(1,20)

async def main() -> None:
    pierwsze = await fetch(3)
    drugie = await fetch(4)
    trzecie = await fetch(1)
    czwarte = await fetch(10)
