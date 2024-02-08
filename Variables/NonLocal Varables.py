#Non-Local Varables
def outer_function():
    x = 10  # Local variable of outer_function
    print("Outer Before:", x)
    def inner_function():
        nonlocal x  # Using nonlocal to access the variable from the outer function
        x = 20  # Modifying the value of x from outer_function within inner_function
        print("Inner:", x)

    inner_function()
    print("Outer After:", x)

outer_function()
