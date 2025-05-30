#Simple Compound Interest Calculator 

from colorama import init, Fore
init(Fore)

print(Fore.LIGHTBLACK_EX + "   _____                    _____       _      _____      _      ")
print(Fore.LIGHTBLACK_EX + "  / ____|                  |_   _|     | |    / ____|    | |     ")
print(Fore.LIGHTBLACK_EX + " | |     ___  _ __ ___ ______| |  _ __ | |_  | |     __ _| | ___ ")
print(Fore.LIGHTBLACK_EX + " | |    / _ \| '_ ` _ \______| | | '_ \| __| | |    / _` | |/ __|")
print(Fore.LIGHTBLACK_EX + " | |___| (_) | | | | | |    _| |_| | | | |_  | |___| (_| | | (__ ")
print(Fore.LIGHTBLACK_EX + "  \_____\___/|_| |_| |_|   |_____|_| |_|\__|  \_____\__,_|_|\___|")

initialInvest = float(input("Please enter your intial investment: "))
anualRate = int(input("Please enter your anual rate(%): "))
intCom = int(input("Please enter how many times the interest is compounded per year: "))
numYears = int(input("Please enter how many years: "))

rateDec = anualRate / 100

comintFormula = initialInvest * (1 + rateDec / intCom) ** (intCom * numYears)
print(f"You final result is: ${comintFormula}")