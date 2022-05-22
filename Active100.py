import requests
from bs4 import BeautifulSoup

# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get('https://terms.naver.com/entry.naver?docId=5645159&cid=43667&categoryId=43667', headers=headers)
# soup = BeautifulSoup(data.text, 'html.parser')

url = "https://finance.naver.com/sise/sise_quant.naver"
response = requests.get(url)
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    #contentarea_left > h3
    # title2 = soup.select('#contentarea > div.box_type_l > table > tbody > tr:nth-child(1)')
    # title1 = soup.select('th')
    # print(len(title1))
    # print(title1)
    # col_list = []
    # for i in range(len(title1)):
    #     if i != 0:
    #         # col_list.append(title2[i].get_text())
    #         col_list.append(title1[i].text)
    # print(col_list)

    # title2 = soup.findAll("a", class_="tltle")
    # head_list = []
    # for i in range(len(title2)):
    #     head_list.append(title2[i].text)
    # print(head_list)
    # print(len(head_list))

    # title3 = soup.find_all("td", class_="number")
    # data_list = []
    # for i in range(len(title3)):
    #     j = divmod(i, 10)
    #     if (j[1] == 1) or (j[1] == 2) :
    #         title3[i] = 

    #         data_list.append(title3[i].text)
    # print(data_list)
    # print(len(data_list))

    title2 = soup.findAll("span", class_="tah p11 nv01")
    head_list = []
    for i in range(len(title2)):
        head_list.append(title2[i].text)
    print(head_list)
    print(len(head_list))


else:
    print(response.status_code)