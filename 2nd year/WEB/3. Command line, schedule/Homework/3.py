import schedule


counter = 1

def foo():
    global counter
    print("Ку" * counter)
    if counter == 12:
        counter = 1
    else:
        counter += 1

schedule.every().hour.at(":00").do(foo)

while True:
    schedule.run_pending()
