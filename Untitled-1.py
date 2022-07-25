"""Dro Drop"""
def main():
    """prepro65"""
    grade = float(input())
    if grade < 1.00:
        print("I'm so sad.")
    elif grade < 2.00:
        print("%.2f"%(4.00 - grade))
    else:
        print("I'm so happy.")
main()
