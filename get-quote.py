import random


def primary():
    #print("Keep it logically awesome.")

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    numQuotes = random.randint(0, len(quotes))

    mySet = set()
    i = 0
    while len(mySet) < numQuotes:
      last = len(quotes) - 1
      rnd = random.randint(0, last)
      quote = quotes[rnd].rstrip()
      if quote not in mySet:
        print(quote)
        mySet.add(quote)
      i += 1

def writeQuote(quote):
    f = open("quotes.txt","a")
    f.write(quote)
    f.close()


if __name__ == "__main__":
    print("Please enter a new quote")
    try:
      quote = input()
    except:
      quote: None
    if quote != '' and quote != None:
      writeQuote(quote)
    primary()
