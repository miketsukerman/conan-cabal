from conans.model import Generator
from conans import ConanFile,tools, AutoToolsBuildEnvironment
import os


class AlexPackage(ConanFile):
    name = "alex"
    version = "3.2.5"
    build_requires = "ghc/8.10.1@haskell/testing"
    url = "https://github.com/miketsukerman/conan-cabal"
    license = "BSD3"
    description = "A lexical analyser generator for Haskell "
    topics = ("ghc", "cabal", "haskell", "alex")
    settings = "os", "compiler", "build_type", "arch"
    generators = "virtualrunenv"
    scm = {
         "type": "git",
         "subfolder": "alex",
         "url": "https://github.com/simonmar/alex.git",
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
