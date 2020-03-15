from conans.model import Generator
from conans import ConanFile

class Proglet:
    def __init__(self, proglet_info):
        self.info = proglet_info

    def exec_content(self, exec_info):
        exec_template = (
            "executable: {}\n".format(exec_info.name),
            "main-is: {}\n".format(exec_info.main_file),
            "build-depends: {}\n".format(exec_info.build_deps),
            "hs-source-dirs: {}\n".format(exec_info.source_dirs),
            "default-language: {}\n".format(exec_info.default_language)
            )
        return exec_template

    def lib_content(self, lib_info):
        lib_template = (
            "exposed-modules: {}".format(lib_info.exposed_modules),
            "other-modules: {}".format(lib_info.other_modules),
            "other-extensions: {}".format(lib_info.other_extensions),
            "build-depends: {}".format(lib_info.build_deps),
            "hs-source-dirs: {}".format(lib_info.source_dirs),
            "default-language: {}".format(lib_info.default_language)
        )
        return lib_template        

    def content(self):
        template = (
            "name: {}\n".format(self.info.name),
            "version: {}\n".format(self.info.version),
            "license: {}\n".format(self.info.license),
            "license-file: {}\n".format(self.info.license_file),
            "author: {}\n".format(self.info.author),
            "maintainer: {}\n".format(self.info.maintainer),
            "category: {}\n".format(self.info.category),
            "build-type: {}\n".format(self.info.build_type),
            "extra-source-files: {}\n".format(self.info.extra_source_files),
            "cabal-version: {}\n".format(self.info.cabal_version),
            "synopsis: {}\n".format(self.info.synopsis),
            "copyright: {}\n".format(self.info.copyright),
            "category: {}\n".format(self.info.category),
            "\n".join( "%s" % exec_content(exec) for exec in self.info.executables), 
            "\n".join( "%s" % lib_content(lib) for lib in self.info.libraries)
        )

        return template

class Setup:
    def __init__(self, setup_info):
        pass

    def content():
        return """
            import Distribution.Simple 
            main = defaultMain
            """

class Cabal(Generator):

    @property
    def content(self):
         proglet = Proglet(self.proglet_info)
         setup = Setup(self.setup_info)
         return {"{}.cabal".format(self.proglet_info.name): proglet.content(),
                 "Setup.hs": setup.content()}  # any number of files

    @property
    def filename(self):
        pass

class CabalPackage(ConanFile):
     name = "Cabal"
     version = "0.1"
     url = "https://github.com/miketsukerman/conan-cabal"
     license = "MIT"
     description = "Haskell build system"