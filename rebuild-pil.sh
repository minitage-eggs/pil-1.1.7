#!/usr/bin/env bash
cd $(dirname $0)
W=$PWD
cd PIL-x
for i in 1.1.6 1.1.6-ZMinitagePatched-Becomepil 1.1.7-ZMinitagePatched-Becomepil 1.1.7;do
    sed -i "s/PIL_VERSION = .*/PIL_VERSION = '$i'/" setup.py
    python setup.py sdist --formats=zip>/dev/null
done
cp dist/*zip ..
# vim:set et sts=4 ts=4 tw=80:
