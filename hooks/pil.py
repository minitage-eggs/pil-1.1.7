#add minitage libraries to search pathes
import os
import re

ref = re.M|re.I|re.U
def pil(options,buildout):
    cwd = os.getcwd()
    os.chdir(options['compile-directory'])
    locations = {'freetype':buildout['freetype']['location'],
                 'jpeg':buildout['libjpeg']['location'],
                 'tiff':buildout['libtiff']['location'],
                 'zlib':buildout['zlib']['location'],
                } 
    st = open('setup.py').read()
    pregex = [("^(FREETYPE_ROOT.*)$", "FREETYPE_ROOT=libinclude('%(freetype)s')"%locations),
          ("^(TIFF_ROOT.*)$",  "TIFF_ROOT=libinclude('%(tiff)s')"%locations),
          ("^(JPEG_ROOT.*)$", "JPEG_ROOT=libinclude('%(jpeg)s')"%locations),
          ("^(ZLIB_ROOT.*)$",  "ZLIB_ROOT=libinclude('%(zlib)s')"%locations),
    ] 

    for p, rep in pregex:
        r= re.compile(p, ref)
        st = r.sub(rep, st)
    open('setup.py', 'w').write(st)
    os.chdir(cwd)

