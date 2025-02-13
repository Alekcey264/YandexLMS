import asyncio


async def to_fertilize(name):
    print(f'7 Application of fertilizers for {name}')
    asyncio.sleep(3 / 1000)
    print(f'7 Fertilizers for the {name} have been introduced')
    print(f'8 Treatment of {name} from pests')
    asyncio.sleep(5 / 1000)
    print(f'8 The {name} is treated from pests') 


async def to_plant(name, a, b, c):
    print(f'0 Beginning of sowing the {name} plant')
    print(f'1 Soaking of the {name} started')
    asyncio.sleep(a / 1000)
    await to_fertilize(name)
    print(f'2 Soaking of the {name} is finished')
    print(f'3 Shelter of the {name} is supplied')
    asyncio.sleep(b / 1000)
    print(f'4 Shelter of the {name} is removed')
    print(f'5 The {name} has been transplanted')
    asyncio.sleep(c / 1000)
    print(f'6 The {name} has taken root')
    print(f'9 The seedlings of the {name} are ready')


async def sowing(*data):
    tasks = []
    for item in data:
        tasks.append(to_plant(*item))
    asyncio.gather(*tasks)


data = [('carrot', 7, 18, 2), ('cabbage', 2, 6, 10), ('onion', 5, 12, 7)]
asyncio.run(sowing(*data))