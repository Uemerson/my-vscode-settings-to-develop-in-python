# My Visual Studio Code settings to develop in python

Here are my settings for python development with Visual Studio Code editor, below are some instructions on what is needed to install and configure for everything to work well.

To change the code formatter, change the "python.formatting.provider" in the VSCode JSON configuration file, for example:

To use autopep8:

```
{
  "python.formatting.provider": "autopep8"
}
```

To use Black:

```
{
  "python.formatting.provider": "black"
}
```

# Extensions

It's necessary to install on [Visual Studio Code](https://code.visualstudio.com/) all these below extensions to have a better experience. Some extensions it's mandatory for all settings to work fine.

<strong>Mandatory(s)</strong>

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python): A Visual Studio Code extension with rich support for the Python language (for all actively supported versions of the language: >=3.7), including features such as IntelliSense (Pylance), linting, debugging, code navigation, code formatting, refactoring, variable explorer, test explorer, and more!

<strong>Not mandatory(s)</strong>

- [python snippets](https://marketplace.visualstudio.com/items?itemName=frhtylcn.pythonsnippets): A snippet pack to make you more productive working with python

- [Code Runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner): Run code snippet or code file for multiple languages: C, C++, Java, JavaScript, PHP, Python, Perl, Perl 6, Ruby, Go, Lua, Groovy, PowerShell, BAT/CMD, BASH/SH, F# Script, F# (.NET Core), C# Script, C# (.NET Core), VBScript, TypeScript, CoffeeScript, Scala, Swift, Julia, Crystal, OCaml Script, R, AppleScript, Elixir, Visual Basic .NET, Clojure, Haxe, Objective-C, Rust, Racket, Scheme, AutoHotkey, AutoIt, Kotlin, Dart, Free Pascal, Haskell, Nim, D, Lisp, Kit, V, SCSS, Sass, CUDA, Less, Fortran, Ring, and custom command

# Libraries settings

The configuration file [.coveragerc](.coveragerc) defines settings for Python coverage.

The configuration file [.flake8](.flake8) defines settings for Flake8.

The configuration file [.pep8](.pep8) defines settings for autopep8.

The configuration file [pytest.ini](pytest.ini) defines settings for pytest.

The configuration file [pyproject.toml](pyproject.toml) defines settings for Black. This file may contain other settings as well.

You can put the settings for Black, autopep8 and Flake8 on settings of Visual Studio Code editor, for example:

```
{
  "python.linting.flake8Args": [
      "--max-line-length=120"
  ],
  "python.formatting.blackArgs": [
    "--line-length", "120",
    "--experimental-string-processing"
  ],
  "python.formatting.autopep8Args": [
    "--max-line-length", "120",
    "--experimental"
  ],
}
```

# Tests (pytest)

To generate a coverage report as HTML output, type:

```
$ pytest --cov-report html --cov=src tests/
```

<hr>

<br />
<br />

Made with ❤, by Uemerson Pinheiro Junior
