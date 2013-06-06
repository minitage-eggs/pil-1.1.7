#add minitage libraries to search pathes
import os
import re
import platform
HAS_WINDOWS = (('windows' in platform.system().lower()
                or ('cygwin' in platform.system().lower())))

ref = re.M|re.I|re.U
def pil(options,buildout):
    cwd = os.getcwd()
    os.chdir(
        options['compile-directory']
    )
    ccwd = os.getcwd()
    # make a .libs folder containing symlink to dyn libs
    # to link  with
    libs = os.path.join(ccwd, 'libs')
    libdir = '/usr'
    locations = {
        'freetype': buildout.get('freetype', {}).get(
            'location', libdir
        ),
        'jpeg': buildout.get('libjpeg', {}).get (
            'location', libdir
        ),
        'tiff': buildout.get('libtiff', {}).get(
            'location', libdir
        ),
        'zlib': buildout.get('zlib', {}).get(
            'location', libdir
        ),
        'lcms': buildout.get('lcms', {}).get(
            'location', libdir
        ),
    }
    st = open('setup.py').read()
    for i in locations.keys():
        locations['%s-include' % i ]= locations[i] + "/include"
        locations['%s-lib' % i ]= locations[i] + "/lib"
    pregex = [
        ("^(FREETYPE_ROOT.*)$",
         "FREETYPE_ROOT='%(freetype-lib)s' , '%(freetype-include)s'" % (
             locations
         )
        ),
        ("^(TIFF_ROOT.*)$",
         "TIFF_ROOT='%(tiff-lib)s', '%(jpeg-include)s'" % locations),
        ("^(JPEG_ROOT.*)$",
         "JPEG_ROOT='%(jpeg-lib)s', '%(tiff-include)s'" % locations),
        ("^(ZLIB_ROOT.*)$",
         "ZLIB_ROOT='%(zlib-lib)s', '%(zlib-include)s'" % locations),
        ("^(LCMS_ROOT.*)$",
         "LCMS_ROOT='%(lcms-lib)s', '%(lcms-include)s'" % locations),
    ]
    for p, rep in pregex:
        r= re.compile(p, ref)
        st = r.sub(rep, st)
    open('setup.py', 'w').write(st)
    os.chdir(cwd)
