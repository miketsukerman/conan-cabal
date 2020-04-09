from conans.model import Generator
from conans import ConanFile,tools, AutoToolsBuildEnvironment
import os


class NetworkURIPackage(ConanFile):
    name = "network-uri"
    version = "2.6.3.0"
    requires = "ghc/8.8.2", "cabal/3.2.0.0"
    url = "https://github.com/miketsukerman/conan-cabal"
    license = "MIT"
    description = "This package provides facilities for parsing and unparsing URIs, and creating and resolving relative URI references, closely following the URI spec, IETF RFC 3986"
    topics = ("ghc", "cabal", "haskell", "network", "network-uri")
    settings = "os", "compiler", "build_type", "arch"
    generators = "virtualrunenv"
    scm = {
         "type": "git",
         "subfolder": "network-uri",
         "url": "https://github.com/haskell/network-uri.git",
         "revision": "master"
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
