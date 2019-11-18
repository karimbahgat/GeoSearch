"""
"""

import os
import urllib, urllib.request
import zipfile
import io

def download_nga_gns(downpath):
    urlsite = "http://geonames.nga.mil/gns/html/namefiles.html"

    #desiredfields = ["LAT", "LONG", "FC", "NT", "LC", "SHORT_FORM", "GENERIC", "FULL_NAME_RO"]

    def download(link):
        print('downloading')
        rawzip = urllib.request.urlopen(link).read()
        print('ziploading')
        z = zipfile.ZipFile(io.BytesIO(rawzip))
        fname = link.split('/')[-1].split('.')[0] + '.txt'
        print('extracting')
        z.extract(fname, downpath)

    # file page
    raw = urllib.request.urlopen(urlsite).read().decode('utf8')
    elems = (e for e in raw.replace('>','<').split('<'))
    elem = next(elems, None)
    while elem is not None:
        if '.zip' in elem:
            print(elem)
            sublink = elem.split('href=')[1].split()[0].strip('"')
            print(sublink)
            if len(sublink.split('/')[-1].split('.')[0]) == 2:
                root = os.path.split(urlsite)[0]
                url = root + '/' + sublink
                print(sublink, url)
                download(url)
        elem = next(elems, None)


if __name__ == '__main__':
    download_nga_gns('testgns')

    
