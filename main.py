import sys
import requests
from bs4 import BeautifulSoup


def main():
    global cells, value
    url = "https://www.burzochron.pl/meteo-data/metar/epkk/"
    response_content = requests.get(url)
    if (response_content.headers["Content-Type"].find("text/html") != -1 and response_content.status_code == 200):
        soup = BeautifulSoup(response_content.text, "lxml")
        if (soup.find(class_='table-metar')):
            headers = []
            rows = []
            for item in soup.find(class_='table-metar').find_all("th"):
                headers.append(item.text)
                rows.append(item.find_next_sibling().text)
            try:
                index = headers.index("Ciśnienie")
            except ValueError:
                print("Nie znaleziono ciśnienia w tabeli")
                sys.exit(1)
            temp = rows[index].split()
            result = temp[0]
            if int(result) > 1090 or int(result) < 870:
                print("Ciśnienie przyjmuje niemożliwe wartości")
                sys.exit(1)
            print("Ciśnienie w hPa na lotnisku w Balicach:")
            sys.stdout.write(result)
            sys.exit(0)
        else:
            print("Strona nie zawiera przewidywanej zawartości")
            sys.exit(1)
    else:
        print("Strona nie działa poprawnie")
        sys.exit(1)


if __name__ == "__main__":
    main()
