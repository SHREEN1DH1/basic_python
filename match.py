def http_error(status):
    match status:
        case 400:
            print("Bad request")
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

stat=int(input("enter a number"))
http_error(stat)
