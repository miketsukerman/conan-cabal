from conans.model import Generator
from conans import ConanFile,tools
import os


class Base64ByteStringPackage(ConanFile):
    name = "byte64-bytestring"
    version = "1.0.0.3"
    requires = "ghc/8.8.2", "cabal/3.2.0.0"
    url = "https://github.com/miketsukerman/conan-cabal"
    license = "BSD3"
    description = "This package provides a Haskell library for working with base64-encoded data quickly and efficiently, using the ByteString type."
    topics = ("ghc", "cabal", "haskell")
    settings = "os", "compiler", "build_type", "arch"
    generators = "virtualrunenv"
    scm = {
         "type": "git",
         "subfolder": "byte64-bytestring",
         "url": "https://github.com/haskell/base64-bytestring.git",
         "revision": "refs/tags/{}".format(version)
    }

    def build(self):        
        self.run("ghc -threaded --make Setup", run_environment=True,cwd=self.name)
        self.run(".{}Setup configure --user --prefix={}".format(os.sep,self.package_folder), run_environment=True,cwd=self.name)
        self.run(".{}Setup build".format(os.sep), run_environment=True,cwd=self.name)
        self.run(".{}Setup install".format(os.sep), run_environment=True,cwd=self.name)

    def package(self):
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
