import requests
from bs4 import BeautifulSoup
import time
import os
import colored
from colored import fg, bg, attr

def start():
    while 1:
        #d = requests.get('https://results.eci.gov.in/pc/en/partywise/index.htm')
        d = getData()
        soup = BeautifulSoup(d, 'html.parser')
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
        try:
            track_rahul()
        except Exception as e:
            pass
        time.sleep(30)

def getData(delay = 1):
    try:
        d = requests.get('https://results.eci.gov.in/pc/en/partywise/index.htm')
        if d.status_code != 200:
            print('Something wrong with eci website, trying again in ', delay, ' seconds..')
            time.sleep(delay)
            return getData(delay*2)
        return d.text
    except Exception as e:
        print('ECI Website Down, trying again in ',delay,' seconds..')
        time.sleep(delay)
        return getData(delay*2)

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
    newtup = list()
    for i in tup:
        if int(i[1]) != 0:
            newtup.append(i)
    newtup.sort(key = lambda x: int(x[1]), reverse=True)  
    return newtup

def track_rahul():
    d = requests.get('http://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseS2437.htm')
    soup = BeautifulSoup(d.text, 'html.parser')
    td = soup.findAll('td')
    irani = int(td[31].string)
    gandhi = int(td[24].string)
    rahulPercent = float(td[32].string)/100.0
    totalVotesDone = int(gandhi/rahulPercent)
    trail = 'green'
    lead = 'red'
    totalvotes = 508582
    if irani > gandhi:
        print('Rahul Gandhi is Trailing in Amethi by ','%s' %(fg(trail)),irani - gandhi,'%s' % (attr('reset'))," Votes",end="\n")
    else:
        print('Rahul Gandhi is Leading in Amethi by ','%s' %(fg(trail)),irani - gandhi,'%s' % (attr('reset'))," Votes",end="\n")
    print('Approx Votes Counting Remaining in Amethi:','%s' % (fg('magenta')),totalvotes - totalVotesDone,'%s' % (attr('reset')))