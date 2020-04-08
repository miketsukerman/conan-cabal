# Conan support for Cabal build system

[![Build Status](https://travis-ci.com/miketsukerman/conan-cabal.svg?branch=master)](https://travis-ci.com/miketsukerman/conan-cabal)

[Conan.io](https://conan.io) package for Haskell [Cabal](https://github.com/haskell/cabal) package manager.

The packages generated with this conanfile can be found in [Bintray](https://dl.bintray.com/miketsukerman/fpp/fpp/cabal/3.2.0.0/).

## For Users: Use this package

### Basic setup

    conan install cabal/3.2.0.0@fpp/testing

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    cabal/3.2.0.0@fpp/testing

    [generators]
    virtualrunenv

Complete the installation of requirements for your project running:

    mkdir build && cd build && conan install ..

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git.

## For Packagers: Publish this Package

The example below shows the commands used to publish to bincrafters conan repository. To publish to your own conan respository (for example, after forking this git repository), you will need to change the commands below accordingly.

## Issues

All issues, such as feature request, bug, support or discussion are centralized on Community repository. If you are interested to open a new issue, please visit https://github.com/bincrafters/community/issues.

## Build and package

The following command both runs all the steps of the conan file, and publishes the package to the local system cache.  This includes downloading dependencies from "build_requires" and "requires" , and then running the build() method.
    
    conan create . fpp/stable

## Add Remote

    conan remote add miketsukerman-bintray "https://api.bintray.com/conan/miketsukerman/fpp"

## Upload

    conan upload cabal/3.2.0.0@fpp/testing --all -r miketsukerman-bintray

# License

conan bnfc is provided under a Apache2 license that can be found in the [License.md](License.md) file. By using, distributing, or contributing to this project, you agree to the terms and conditions of this license.
