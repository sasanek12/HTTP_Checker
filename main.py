import sys
import requests


def main():
    url = "http://th.if.uj.edu.pl/"
    response_head = requests.head(url)
    response_content = requests.get(url)
    if (response_head.headers["Content-Type"] == "text/html" and response_content.status_code == 200):
        if (response_content.text.find("Institute of Theorethical Physics")):
            print("Strona dziala poprawnie!")
            sys.exit(0)

    print("Strona nie dziala poprawnie")
    sys.exit(1)


if __name__ == "__main__":
    main()
