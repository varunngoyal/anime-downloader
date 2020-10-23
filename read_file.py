class read_file():

    def read_urls_from_file(self):
        f = open("urls.txt", "r")

        url_list = []
        url1 = f.readline().rstrip("\n")
        while url1 != '':
            url_list.append(url1) 
            url1 = f.readline().rstrip("\n")
        return url_list

if  __name__ == '__main__':
    r = read_file()
    print(r.read_urls_from_file())

