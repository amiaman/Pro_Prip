import urllib

X = urllib.urlopen("http://www.thehindu.com/")
Read = X.read()

Creat_file = open("The Hindu.txt", "w")
Creat_file.write(Read)
Creat_file.close()
X.close()
