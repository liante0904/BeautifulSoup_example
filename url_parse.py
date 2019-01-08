from bs4 import BeautifulSoup
import requests

response = requests.get('http://www.kocw.net/home/search/kemView.do?kemId=1284599&ar=relateCourse')
parsedHtml = response.text
soup = BeautifulSoup(parsedHtml, 'html.parser')

links = soup.find_all('a')



start = False
i = 1
cnt = 1284600
for link in links:
        #print(link)

        if link.has_attr('onclick'):
                #url = link.attrs['onclick'].split('f_openLecture(')
                num = "21," + str(i)
                loopnum = "'" + "128460" + str(i - 1) + "'"
                loopnum1 = "'" + str(1284600+ i - 1) + "'"
                
                attr_onclick = link.attrs['onclick']
                edit_onclick = attr_onclick.replace("f_openLecture('", "").replace("'http://www.kocw.net/home/cview.do?cid=cc576859babd7a01');","").replace("','1284599',","")
                
                result = edit_onclick.replace(num, "").replace(",,","").replace(loopnum, "").replace(loopnum1, "")
                #print(i , link.attrs['onclick'])
                if i == 46:
                    break


                print("강의" + str(i) + "번URL: " + str(result))
                #print(url)
                i  =  i + 1
