class EmptyStackError(Exception):
    pass

class Stack:

    def __init__(self) -> None:
        self.pile = []

    def is_empty(self) -> bool:
        if self.pile == []:
            return True
        return False
        
    def pop(self) -> None:
        try:
            if self.is_empty():
                raise EmptyStackError
        except EmptyStackError:
            print("C'est pas bien")
        else:
            r = self.pile[len(self.pile) - 1]
            del(self.pile[len(self.pile) - 1])
            return r
        
    def push(self, value) -> None:
        self.pile.append(value)

    def __str__(self) -> str:
        r = ""
        for i in self.pile:
            r += f"{i}\n"
        return r

def calcul(stack:Stack, operator:str) -> None:
    if operator == "+":
        stack.push(stack.pop() + stack.pop())
    if operator == "-":
        stack.push(stack.pop() - stack.pop())
    if operator == "/":
        stack.push(stack.pop() / stack.pop())
    if operator == "*":
        stack.push(stack.pop() * stack.pop())

def evalutation_lst(liste:list):
    jaaj = Stack()
    for i in range(len(liste)):
        if liste[i] == "+":
            jaaj.push(liste[i - 1])
            jaaj.push(liste[i - 2])
            calcul(jaaj, "+")
        if liste[i] == "-":
            jaaj.push(liste[i - 1])
            jaaj.push(liste[i - 2])
            calcul(jaaj, "-")
        if liste[i] == "/":
            jaaj.push(liste[i - 1])
            jaaj.push(liste[i - 2])
            calcul(jaaj, "/")
        if liste[i] == "*":
            jaaj.push(liste[i - 1])
            jaaj.push(liste[i - 2])
            calcul(jaaj, "*")
    return jaaj.pile[0]

feur = Stack()
for i in range(30):
    feur.push(30)

print(evalutation_lst([2, 3, "*", 4, 2, "+"]))