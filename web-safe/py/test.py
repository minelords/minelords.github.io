import re

def one():
    with open('url1.html','r',encoding='utf-8') as f:
        lines=f.readlines()
    with open('url1.html','w',encoding='utf-8') as f:
        for line in lines:
            try:
                url=re.findall(r'.*?(http.*?index.m3u8)',line)[0]
                title=re.findall(r'<br>(.*?):http.*?',line)[0]
                final=f'<br><a href="https://www.dplayer.top/index.php?url={url}" target="_blank">{title}</a>:{url}'
                print(final)
                f.write(final+"\n")
            except:
                print(line)
                f.write(line)
                
def two(i):
    with open(f'url{i}.html','r',encoding='utf-8') as f:
        lines=f.readlines()                
    
    with open(f'url{i}.html','w',encoding='utf-8') as f:
        lines = lines[:-2]
        titles=[]
        urls=[]
        for line in lines:
            try:    
                title=re.findall(r'<p>(.*?)：</p>',line)[0]
                titles.append(title)
            except:
                try:
                    url=re.findall(r'<p>(http.*?)</p>',line)[0] 
                    urls.append(url)
                except:
                    f.write(line)        
        for title,url in zip(titles,urls):
            final=f'<p><a href="https://www.dplayer.top/index.php?url={url}"  target="_blank">{title}</a><p>\n<p>{url}</p>\n'
            f.write(final)
        f.write("</body>\n</html>")
        

one()