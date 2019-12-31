def boost():
    global bitcoin
    global rboost
    if rboost == 0:
        rboost += 1
        d.set(rboost)
        time.sleep(3)
        rboost -= 1
        d.set(rboost)