"""Onsite Day1"""
def main():
    """เบื่อแล้วขนมตู้ อยากเป็นชู้กับเธอ"""
    money_in_bank = int(input())
    amount_drink = int(input())
    snack1 = int(input())
    snack2 = int(input())
    snack3 = int(input())
    mmm = (money_in_bank - amount_drink)%3
    if mmm == 0:
        price_snack1 = money_in_bank - (snack1 * 10)
        print("Snack number 1:", money_in_bank - (snack1 * 10))
        if ((money_in_bank - amount_drink) - price_snack1)%3 == 0:
            price_snack2 = money_in_bank - (snack2 * 12)
    elif mmm == 1:
        price_snack1 = money_in_bank - snack1 * 15
        if ((money_in_bank - amount_drink) - price_snack1)%3 == 1:
            price_snack2 = money_in_bank - (snack2 * 15)
            print("Snack number 1:", money_in_bank - (snack1 * 10))
    elif mmm == 2:
        price_snack1 = money_in_bank - snack1 * 20
        print("Snack number 1:", money_in_bank - snack1 * 20)
        if ((money_in_bank - amount_drink) - price_snack1)%3 == 2:
            price_snack2 = money_in_bank - (snack2 * 18)
main()
