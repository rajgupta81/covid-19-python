from requests import get
from bs4 import BeautifulSoup

def getdata(show=True):
    """
    this module help you to find the latest data of covid-19 for india only
    """
    if show == True:
        print("""
    if getdata() == a
    to get the data use the sequence of data
    a = [0, 1, 2]
    a[0] = active_cases
    a[1] = descharged
    a[2] = deaths
    """
    )
    headders = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
    data = get("https://www.mohfw.gov.in/", headers=headders)
    htmldata = data.content

    soup = BeautifulSoup(htmldata, "html.parser")
    main = soup.find_all("div", class_="col-xs-8 site-stats-count")
    miandata = main[0].find_all("li")
    #collected data
    complete_data = []
    for i in miandata:
        htmlimpodata = i.find_all("span", class_="mob-show")
        using = htmlimpodata[2]
        #data
        values = using.find_all("strong")[0].text
        real_data = ""
        for k in values:
            if k == "(":
                break
            else:
                real_data += k
        complete_data.append(int(real_data))
    return complete_data

if __name__ == "__main__":
    print(getdata())

