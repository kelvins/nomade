from colorama import Fore, init

init()


def colorize(fore_color):
    def decorator(func):
        def wrapper(content):
            print(fore_color + content + Fore.RESET)

        return wrapper

    return decorator


@colorize(Fore.RESET)
def default(content):
    pass


@colorize(Fore.BLUE)
def debug(content):
    pass


@colorize(Fore.CYAN)
def info(content):
    pass


@colorize(Fore.GREEN)
def success(content):
    pass


@colorize(Fore.YELLOW)
def warning(content):
    pass


@colorize(Fore.MAGENTA)
def error(content):
    pass


@colorize(Fore.RED)
def critical(content):
    pass
