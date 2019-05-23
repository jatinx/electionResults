import requests
from bs4 import BeautifulSoup
import time
import os
import colored
from colored import fg, bg, attr

def start():
    while 1:
        d = requests.get('https://results.eci.gov.in/pc/en/partywise/index.htm')
        soup = BeautifulSoup(d.text, 'html.parser')
        td = soup.findAll('td')
        useable = td[15:151]
        data = [('Name', 'Won', 'Leading','Total'),]
        t = list()
        for i, item in enumerate(useable):
            t.append(item.string)
            if (i+1) % 4 == 0:
                data.append(tuple(t))
                t = list()
        sortdata = Sort_Tuple(data[1:])
        newList = [data[0]] + sortdata
        sdcalled = Sort_Tuple_called(data[1:])
        newListCalled = [data[0]] + sdcalled
        os.system('clear')
        print("Leading: ")
        prprnt(newList[0:15])
        if called(data[1:]) > 0: 
            print("\nCalled: \n")
            prprnt(newListCalled[0:10])
        print('\n\nTotal: 542, Called: ',called(data[1:]))
        time.sleep(30)

def prprnt(data):
    for ii, i in enumerate(data):
        for id,j in enumerate(i):
            if id == 0:
                s = str()
                sl = list(j)
                spaces = 50 - len(j)
                for x in range(spaces):
                    sl.append(' ')
                for x in sl:
                    s += x
                if(ii == 0):
                    print('%s'% (fg('white')),s,'%s' % (attr('reset'))," ",end="")
                else:
                    print('%s'% (fg('blue')),s,'%s' % (attr('reset'))," ",end="")
            else:
                s = str()
                sl = list(j)
                spaces = 10 - len(j)
                for x in range(spaces):
                    sl.append(' ')
                for x in sl:
                    s += x
                if(ii == 0):
                    print('%s'% (fg('white')),s,'%s' % (attr('reset'))," ",end="")
                else:
                    print('%s' %(fg('green')),s,'%s' % (attr('reset'))," ",end="")
        print('')

def called(data):
    c = 0
    for i in data:
        c+=int(i[1])
    return c
    
def Sort_Tuple(tup):  
  
    # reverse = None (Sorts in Ascending order)  
    # key is set to sort using second element of  
    # sublist lambda has been used  
    tup.sort(key = lambda x: int(x[2]), reverse=True)  
    return tup

def Sort_Tuple_called(tup):  
  
    # reverse = None (Sorts in Ascending order)  
    # key is set to sort using second element of  
    # sublist lambda has been used  
    tup.sort(key = lambda x: int(x[1]), reverse=True)  
    return tup