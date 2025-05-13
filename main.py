import matplotlib.pyplot as plt


def vanEckSequence(limit):
    numbers = {}
    prevNum = 0
    lst = [0]
    for index in range(1, limit):
        try:
            numbers[prevNum]
            temp = prevNum
            prevNum = index - numbers[temp] - 1
            numbers[temp] = index - 1
            del temp
            lst.append(prevNum)
        except KeyError:
            numbers[prevNum] = index - 1
            prevNum = 0
            lst.append(0)
    return lst


plt.xlabel("Term number")
plt.ylabel("Term")
terms = int(input("How many terms would you like to see? "))
plt.plot(list(range(1, terms + 1)), vanEckSequence(terms), "r")
plt.plot(list(range(1, terms + 1)), "b")
plt.show()
