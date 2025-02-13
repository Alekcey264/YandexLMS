import asyncio
import time


async def interview(name, a, b, c, d):
    print(f'{name} started the 1 task.')
    await asyncio.sleep(a / 100)
    print(f'{name} moved on to the defense of the 1 task.')
    await asyncio.sleep(b / 100)
    print(f'{name} completed the 1 task.')
    print(f'{name} is resting.')
    await asyncio.sleep(5 / 100)
    print(f'{name} started the 2 task.')
    await asyncio.sleep(c / 100)
    print(f'{name} moved on to the defense of the 2 task.')
    await asyncio.sleep(d / 100)
    print(f'{name} completed the 2 task.')


async def interviews(*guys):
    tasks = []
    for guy in guys:
        tasks.append(asyncio.create_task(interview(*guy)))
    await asyncio.gather(*tasks)


data = [('Ivan', 5, 2, 7, 2), ('John', 3, 4, 5, 1), ('Sophia', 4, 2, 5, 1)]
t0 = time.time()
asyncio.run(interviews(*data))
print(time.time() - t0)