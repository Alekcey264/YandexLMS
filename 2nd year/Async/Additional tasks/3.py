import asyncio


async def buying_a_gift():
    pass


async def main():
    stops = []
    stop = input()
    while stop != '':
        stops.append(stop)
        stop = input()
    gifts = []
    gift = input()
    while gift != '':
        gifts.append(gift)
        gift = input()
    gifts.sort(key=lambda x:x[1] + x[2])
    gifts = gifts[::-1]
    for i in range(len(stops)):
        tasks = []
        for item in gifts:
            



if __name__ == '__main__':
    asyncio.run(main())