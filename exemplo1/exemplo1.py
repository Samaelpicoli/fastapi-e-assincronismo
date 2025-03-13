import asyncio

# Corrotina
async def say_hello(name: str):
    print(f'{name} is starting...')
    await asyncio.sleep(2) # Simulando I/o
    print(f'Hello, {name}')


async def main():
    await asyncio.gather(
        say_hello('Sama'),
        say_hello('Rogério')
    )
    

asyncio.run(main())                                                