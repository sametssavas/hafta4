paragraf="""Dün 70,87 dolara kadar yükselen Brent petrolün varil fiyatı, günü 70,54 dolar seviyesinde tamamladı. Brent petrolün varil fiyatı, bugün saat 09.36 itibarıyla kapanışa göre yaklaşık yüzde 0,3 artarak 70,86 dolar oldu. Aynı saatte Batı Teksas türü (WTI) ham petrolün varili 67,29 dolardan alıcı buldu."""
kelimeler=paragraf.split(' ')

def donustur(a):
    sayac = []
    for kelime in a:
       print(kelime)
       sayici = 0
       for harf in range(len(kelime)):
        sayici+=1
       print(sayici)
       sayac.append(sayici)
    return sayac
b = donustur(kelimeler)
print(b)