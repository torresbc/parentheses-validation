def validation(code):
    open_list = ["[", "{", "(", "<"]
    close_list = ["]", "}", ")", ">"]

    stack = []
    for i in code:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            comparison_index = close_list.index(i)
            if (len(stack) > 0) and (open_list[comparison_index] == stack[len(stack) - 1]):
                stack.pop()
            else:
                return "Not Valid"
    if len(stack) == 0:
        return "Valid :)"
    else:
        return "Not Valid :("


def main():
    print(f'\n\n {validation(input())}')


if __name__ == "__main__":
    main()
