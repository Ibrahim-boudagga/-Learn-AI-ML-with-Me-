from colorama import init, Fore, Style
import datetime


class Debugger:
    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Debugger, cls).__new__(cls)
            cls.instance.init_colorama()
        return cls.instance

    def init_colorama(self):
        init()

    @staticmethod
    def info(message):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"{Fore.BLUE}[INFO] {timestamp}: {message}{Style.RESET_ALL}")

    @staticmethod
    def success(message):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"{Fore.GREEN}[SUCCESS] {timestamp}: {message}{Style.RESET_ALL}")

    @staticmethod
    def warning(message):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"{Fore.YELLOW}[WARNING] {timestamp}: {message}{Style.RESET_ALL}")

    @staticmethod
    def error(message):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"{Fore.RED}[ERROR] {timestamp}: {message}{Style.RESET_ALL}")

    @staticmethod
    def debug(message):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"{Fore.CYAN}[DEBUG] {timestamp}: {message}{Style.RESET_ALL}")

    @staticmethod
    def critical(message):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"{Fore.MAGENTA}[CRITICAL] {timestamp}: {message}{Style.RESET_ALL}")

    @staticmethod
    def log(message):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"{Style.DIM}[LOG] {timestamp}: {message}{Style.RESET_ALL}")

    # Color-specific methods
    @staticmethod
    def red(message):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"{Fore.RED}[RED] {timestamp}: {message}{Style.RESET_ALL}")

    @staticmethod
    def yellow(message):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"{Fore.YELLOW}[YELLOW] {timestamp}: {message}{Style.RESET_ALL}")

    @staticmethod
    def green(message):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"{Fore.GREEN}[GREEN] {timestamp}: {message}{Style.RESET_ALL}")

    @staticmethod
    def cyan(message):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"{Fore.CYAN}[CYAN] {timestamp}: {message}{Style.RESET_ALL}")

    @staticmethod
    def blue(message):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"{Fore.BLUE}[BLUE] {timestamp}: {message}{Style.RESET_ALL}")

    @staticmethod
    def magenta(message):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"{Fore.MAGENTA}[MAGENTA] {timestamp}: {message}{Style.RESET_ALL}")

    @staticmethod
    def white(message):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"{Fore.WHITE}[WHITE] {timestamp}: {message}{Style.RESET_ALL}")

    @staticmethod
    def custom(message, color):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"{color}[CUSTOM] {timestamp}: {message}{Style.RESET_ALL}")

    @staticmethod
    def purple(message):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"{Fore.LIGHTMAGENTA_EX}[PURPLE] {timestamp}: {message}{Style.RESET_ALL}")


# Example usage
if __name__ == "__main__":
    log = Debugger()

    # Test all colors
    log.red("This is a red message")
    log.yellow("This is a yellow message")
    log.green("This is a green message")
    log.cyan("This is a cyan message")
    log.blue("This is a blue message")
    log.magenta("This is a magenta message")
    log.white("This is a white message")

    # Test standard methods
    log.info("This is an info message")
    log.success("This is a success message")
    log.warning("This is a warning message")
    log.error("This is an error message")
    log.debug("This is a debug message")
    log.critical("This is a critical message")
    log.log("This is a regular log message")

    # Test custom color
    log.custom("This is a custom colored message", Fore.LIGHTRED_EX)
