"""CQ01 Functions"""
__author__ = "730575581"

def mimic(message: str) -> str:
    """Return back message"""
    return message

def main() -> None:
    """Main function to run mimic"""
    print(mimic(message=input("What is your message?")))

if __name__ == "__main__":
    main()