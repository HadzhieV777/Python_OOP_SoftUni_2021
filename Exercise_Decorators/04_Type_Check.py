# 04. Type Check

def type_check(t):
    def compile_func(function):
        def wrapper(element):
            if t == type(element):
                return function(element)
            else:
                return "Bad Type"

        return wrapper
    return compile_func


@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
