import urllib2
response = urllib2.urlopen('https://wordpress.org/plugins/about/readme.txt')
data = response.read()
filename = "readme.txt"
file_ = open(filename, 'w')
file_.write(data)
file_.close()