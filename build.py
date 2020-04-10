import os
import subprocess
from os import path

def run(cmd):
    ret = os.system(cmd)
    if ret != 0:
        raise Exception("Failed command: %s" % cmd)

packages = ["semigroups"
            , "network"
            , "network-uri"
            , "random"
            , "base16-bytestring"
            , "base64-bytestring"
            , "hashable"
            , "cryptohash-sha256"
            ]

def main(conan_path):
    for package in packages:
        run("conan create packages/{} {} --build missing".format(package, conan_path))
    
if __name__ == '__main__':
    main("haskell/testing") 
