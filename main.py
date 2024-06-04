import feedparser, time

URL = "http://gukka94.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 3

markdown_text = """
# <img src="https://github.com/JustDoYoung/JustDoYoung/assets/63029463/312b6a4a-8df0-4ae7-9a19-42dc5d5e3a7b" width="50" height="50"/> Nice to meet you! ✌️

저는 클라이언트 개발자 **DoYoung** 입니다.  
수학을 좋아하고 그래픽 분야에 관심이 있습니다.   
![Unity](https://img.shields.io/badge/unity-%23000000.svg?style=plastic&logo=unity&logoColor=white) 와 ![Unreal Engine](https://img.shields.io/badge/unrealengine-%23313131.svg?style=plastic&logo=unrealengine&logoColor=white) 을 다룰 수 있습니다.
   
📞 Contact : guckka94@gmail.com   
✒️ Blog : https://gukka94.tistory.com
   
### 🌱 Things I code with ...
  ![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=plastic&logo=c%2B%2B&logoColor=white)
  ![C#](https://img.shields.io/badge/c%23-%23239120.svg?style=plastic&logo=csharp&logoColor=white)
  ![Unity](https://img.shields.io/badge/unity-%23000000.svg?style=plastic&logo=unity&logoColor=white) 
  ![Unreal Engine](https://img.shields.io/badge/unrealengine-%23313131.svg?style=plastic&logo=unrealengine&logoColor=white) 


### Online Judge
![solvedac badge](https://solvedac-readme-badge.vercel.app/api/v1/badge?user=tornado0310&theme=github-dark&compact=1)
   
   
## ✅ Latest Blog Post

"""  # list of blog posts will be appended here

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"
        
f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
