from conans.model import Generator
from conans import ConanFile,tools, AutoToolsBuildEnvironment
import os


class ResolvePackage(ConanFile):
    name = "resolve"
    version = "0.2.0.1"
    requires = "ghc/8.10.1"
    url = "https://github.com/miketsukerman/conan-cabal"
    license = "GPL3"
    description = "Reading, writing and manipulating resolve archive files"
    topics = ("ghc", "cabal", "haskell", "resolve")
    settings = "os", "compiler", "build_type", "arch"
    generators = "virtualrunenv"
    scm = {
         "type": "git",
         "subfolder": "resolve",
         "url": "https://github.com/riaqn/resolve.git",
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
