from conans import ConanFile, tools
import os


class CabalInstallPackage(ConanFile):
    name = "cabal-install"
    version = "3.2.0.0"
    requires = "ghc/8.8.2", "cabal/3.2.0.0", "byte64-bytestring/1.0.0.3", "http/4000.3.14-r1"
    url = "https://github.com/miketsukerman/conan-cabal"
    license = "MPL-2.0"
    description = "Haskell build system"
    topics = ("ghc", "cabal", "haskell")
    settings = "os", "compiler", "build_type", "arch"
    generators = "virtualrunenv"

    def source(self):
        if self.settings.os == "Linux":
            url = "https://hackage.haskell.org/package/cabal-install-{}/cabal-install-{}.tar.gz".format(
                self.version, self.version)
        else:
            raise Exception(
                "Cabal install {} does not exist for these settings".format(self.version))
        tools.get(url, md5='cc807bc0114eae46ccc90a4ad3bea877')

    def build(self):
        os.chdir("cabal-install-{}".format(self.version))
        self.run("EXTRA_CONFIGURE_OPTS='' PREFIX={} .{}bootstrap.sh --no-doc".format(
            self.package_folder, os.sep), run_environment=True)

    def package(self):
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
