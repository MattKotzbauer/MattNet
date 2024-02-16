import urllib2
response = urllib2.urlopen('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Python_logo_and_wordmark.svg/260px-Python_logo_and_wordmark.svg.png')
data = response.read()
filename = "image.png"
file_ = open(filename, 'w')
file_.write(data)
file_.close()