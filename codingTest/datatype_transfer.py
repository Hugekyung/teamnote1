import datetime

datas = """
 779091968 23 Sep 2009 system.zip
 284164096 14 Aug 2013 to-do-list.xml
 714080256 19 Jun 2013 blockbuster.mpeg
       329 12 Dec 2010 notes.html
 444596224 17 Jan 1950 delete-this.zip
       641 24 May 1987 setup.png
    245760 16 Jul 2005 archive.zip
 839909376 31 Jan 1990 library.dll
"""
d_list = datas.split('\n')
datas_lst = []
for i,d in enumerate(d_list):
    tmp = d.split()
    if not tmp:
        continue

    size = tmp.pop(0)
    filename = tmp.pop(-1)
    date = '-'.join(tmp)
    date = datetime.datetime.strptime(date, "%d-%b-%Y")
    date = date.strftime('%Y-%m-%d')
    print(date)
