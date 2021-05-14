"""
A szinonimaszotar.hu oldal a segítségével szavak szinonímáját lehet megkeresni.
"""
import urllib.request
import requests
import html2text

def szinonima(szoveg):
    page = html2text.html2text(requests.get("https://szinonimaszotar.hu/keres/"+szoveg).text)
    splitedpage = page.split("# ")
    try:
        return splitedpage[2].split("szinonimái:")[1][2:].split("+ !")[0][:-2].replace("\n","").replace(", ",",").split(",")
    except:
        return []

if __name__ == "__main__":
    print(szinonima(input("szó: ")))
