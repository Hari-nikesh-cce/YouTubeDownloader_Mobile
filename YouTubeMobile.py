import webbrowser

link=input("Copy the link")
real_link="https://www.youtubecp.com/watch?v="
follow="&feature=youtu.be"
hin=link.split("/")
leng=len(hin)
hin=hin[leng-1]
download_link=real_link+hin+follow
print(download_link)
webbrowser.open(download_link)