import os

loginName = {'a':'QMD','b':'W6','c':'J8','d':'D2','e':'S4','f':'B5','g':'GM2','h':'QW','i':'N0','j':'HJ','k':'RC',
            'l':'DU','m':'T8L','n':'JK','o':'D7','p':'E4','q':'8D8','r':'BP','s':'UQ7','t':'ER','u':'FJ6','v':'LZ',
            'w':'DS1','x':'T7','y':'X0','z':'KJ0','1':'OP','2':'L0','3':'PQ','4':'DJ','5':'VC','6':'7B','7':'SY',
            '8':'LQ','9':'21','-':'6T','0':'ND','.':'KI',' ':'09','A':'RT','B':'ER','C':'FJ6','D':'LZ','E':'DS1',
            'F':'T7','G':'X0','H':'KJ0','I':'OP','J':'L0','K':'PQ','L':'QMD','M':'W6','N':'J8','O':'D2','P':'S4',
            'Q':'B5','R':'GM2','S':'QW','T':'N0','U':'HJ','V':'RC','W':'SY1','X':'LQ3','Y':'21','Z':'6T','!':'ND','^':'KI'}    

#dictionary for the computername encoding
pcName = {'a':'TY','b':'KJ','c':'3I','d':'DA','e':'87','f':'45','g':'ML','h':'QW','i':'4R','j':'0E','k':'F7',
             'l':'5H','m':'MT','n':'PO','o':'JH','p':'2B','q':'MQ','r':'LL','s':'00','t':'ER','u':'38','v':'M4',
             'w':'7A','x':'XZ','y':'VD','z':'K0','1':'EN','2':'GR','3':'UJ','4':'FG','5':'3N','6':'W2','7':'M0',
             '8':'83','9':'RT','-':'9X','0':'F2','.':'U4',' ':'GM','A':'M56','B':'TY','C':'KJ','D':'2B','E':'MQ',
             'F':'LL','G':'00','H':'ER','I':'38','J':'M4','K':'7A','L':'XZ','M':'VD','N':'K0','O':'EN','P':'GR',
             'Q':'3I','R':'DA','S':'87','T':'45','U':'ML','V':'QW','W':'4R','X':'0E','Y':'F7','Z':'5H','!':'MT','^':''}

key = ""

login = raw_input("login name: ")

for ch in login:
    try: 
        key = key +loginName[ch]
    except:
        pass
		
pcname = os.getenv('COMPUTERNAME')

tmp = ""
for c in pcname:
    try: 
        tmp = tmp + pcName[c]
        key = key + tmp
    except:
        pass

print key