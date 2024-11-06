def test_function():
    def inner_function():
        a = "Я в области видимости функции test_function"
        print(a)

    inner_function()


# Вызов внешней функции, которая вызывает внутреннюю
test_function()

# Попытка вызова внутренней функции вне test_function
inner_function() # NameError: name 'inner_function' is not defined.
