from conans.model import Generator
from conans import ConanFile,tools
import os


class CryptohashSha256StringPackage(ConanFile):
    name = "cryptohash-sha256"
    version = "1.12"
    requires = "ghc/8.10.1@haskell/testing"
    url = "https://github.com/miketsukerman/conan-cabal"
    license = "MIT"
    description = "Fast, pure and practical SHA-256 implementation"
    topics = ("ghc", "cabal", "haskell")
    settings = "os", "compiler", "build_type", "arch"
    generators = "virtualrunenv"
    scm = {
         "type": "git",
         "subfolder": "cryptohash-sha256",
         "url": "https://github.com/haskell-hvr/cryptohash-sha256.git",
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
