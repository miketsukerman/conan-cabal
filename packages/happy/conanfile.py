from conans.model import Generator
from conans import ConanFile,tools, AutoToolsBuildEnvironment
import os


class HappyPackage(ConanFile):
    name = "happy"
    version = "1.19.12"
    build_requires = "ghc/8.10.1@haskell/testing"
    url = "https://github.com/miketsukerman/conan-cabal"
    license = "BSD3"
    description = "A lexical analyser generator for Haskell "
    topics = ("ghc", "cabal", "haskell", "happy")
    settings = "os", "compiler", "build_type", "arch"
    generators = "virtualrunenv"
    scm = {
         "type": "git",
         "subfolder": "happy",
         "url": "https://github.com/simonmar/happy.git",
         "revision": "642156c3b67e4eab7b837aaad43df461c8fa76a5"
    }

    def build(self):        
        self.run("ghc -threaded --make Setup", run_environment=True,cwd=self.name)
        self.run(".{}Setup configure --user --prefix={}".format(os.sep,self.package_folder), run_environment=True,cwd=self.name)
        self.run(".{}Setup sdist".format(os.sep), run_environment=True,cwd=self.name)
        self.run(".{}Setup build".format(os.sep), run_environment=True,cwd=self.name)
        self.run(".{}Setup install".format(os.sep), run_environment=True,cwd=self.name)

    def package(self):
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
