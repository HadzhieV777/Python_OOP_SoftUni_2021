# 06. HTML Tags

def tags(tag):
    def add_tag(func):
        def wrapper(*args):
            return f"<{tag}>{func(*args)}</{tag}>"
        return wrapper
    return add_tag


@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))

@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))