import turtle

def draw_tree(branch_len, level):
    if level > 0:
        turtle.forward(branch_len)
        turtle.right(45)
        draw_tree(0.8 * branch_len, level-1)
        turtle.left(90)
        draw_tree(0.8 * branch_len, level-1)
        turtle.right(45)
        turtle.backward(branch_len)

def main():
    # Запит у користувача на введення рівня рекурсії
    level = int(input("Введіть рівень рекурсії: "))

    # Налаштування вікна
    turtle.setup(width=1024, height=768)
    turtle.speed(0)
    turtle.left(90)
    turtle.up()
    turtle.backward(300)
    turtle.down()
    turtle.color("red")
    turtle.pensize(2)

    # Виклик функції для малювання дерева
    draw_tree(150, level)

    # Закриття вікна при натисканні клавіші
    turtle.done()

if __name__ == "__main__":
    main()