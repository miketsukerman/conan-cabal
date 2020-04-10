from conans.model import Generator
from conans import ConanFile,tools
import os


class IntegerLogarithmsPackage(ConanFile):
    name = "integer-logarithms"
    version = "1.0.3"
    requires = "ghc/8.10.1@haskell/testing"
    url = "integer-logarithmss://github.com/miketsukerman/conan-cabal"
    license = "MIT"
    description = "Integer logarithms, originally split from arithmoi package"
    topics = ("ghc", "cabal", "haskell", "integer-logarithms")
    settings = "os", "compiler", "build_type", "arch"
    generators = "virtualrunenv"
    scm = {
         "type": "git",
         "subfolder": "integer-logarithms",
         "url": "https://github.com/Bodigrim/integer-logarithms.git",
         "revision": "refs/tags/v{}".format(version)
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
