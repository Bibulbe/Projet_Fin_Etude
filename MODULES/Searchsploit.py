from googlesearch import search
print('------------------------------------')
print('* Mathis JEANNOT & Paul MASCARILLA *')
print('------------------------------------')
def searchsploit(service):
    recherche = service + " exploit"
    res = search(recherche, stop=5)
    urls = []
    for l in res:
        urls.append(l)
    displayInfos = " Exploits concernant " + service +"\n"
    for url in urls:
        displayInfos += f"{url}\n"
    return displayInfos
print(searchsploit("Wordpress 4.0"))