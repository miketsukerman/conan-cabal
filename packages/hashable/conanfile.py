from conans.model import Generator
from conans import ConanFile,tools, AutoToolsBuildEnvironment
import os


class HashablePackage(ConanFile):
    name = "hashable"
    version = "1.3.0.0"
    requires = "ghc/8.10.1@haskell/testing"
    url = "https://github.com/miketsukerman/conan-cabal"
    license = "MIT"
    description = "This package defines a class, Hashable, for types that can be converted to a hash value"
    topics = ("ghc", "cabal", "haskell", "hashable")
    settings = "os", "compiler", "build_type", "arch"
    generators = "virtualrunenv"
    scm = {
         "type": "git",
         "subfolder": "hashable",
         "url": "https://github.com/tibbe/hashable.git",
         "revision": "b317a69cb8c4b97463151db4c6cc50b9d1aa4aa7"
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
