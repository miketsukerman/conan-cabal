from conans.model import Generator
from conans import ConanFile,tools
import os


class SemigroupsPackage(ConanFile):
    name = "semigroups"
    version = "0.19.1"
    build_requires = "ghc/8.10.1@haskell/testing"
    url = "https://github.com/miketsukerman/conan-cabal"
    license = "BSD3"
    description = "Semigroup is an algebraic structure consisting of a set together with an associative binary operation"
    topics = ("ghc", "cabal", "haskell", "semigroups")
    settings = "os", "compiler", "build_type", "arch"
    build_requires = "ghc/8.10.1@haskell/testing"
    generators = "virtualrunenv"
    scm = {
         "type": "git",
         "subfolder": "semigroups",
         "url": "https://github.com/ekmett/semigroups.git",
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
