def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():

    num1=float(input("What's the first number?: "))
    should_accumulate=True
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        pick_oprn=input("Pick an operation: ")
        num2=float(input("What's the next number: "))
        answer=operations[pick_oprn](num1,num2)
        print(f"{num1} {pick_oprn} {num2} = {answer}")

        choice=input(f"Type y to continue calculating with {answer}. Type n to start new operation ")

        if choice=="y":
            num1=answer
        else:
            should_accumulate=False

calculator()