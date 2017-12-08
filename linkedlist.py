import urllib2

counter = 0
response  = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345')
html = response.read()

end_numbers = html[len(html)-5:len(html)]

first_part = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

while counter < 400:
    new_nothing = []
    response = urllib2.urlopen(first_part+str(end_numbers))
    html = response.read()
    for item in html:
        if item.isdigit() == True:
            new_nothing.append(item)
    
    counter += 1
    end_numbers = ''.join(new_nothing)
    print end_numbers    

