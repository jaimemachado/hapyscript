{ pkgs ? import (fetchTarball "https://github.com/NixOS/nixpkgs/archive/nixos-unstable.tar.gz") {} }:

let
  python = pkgs.python312;
  pythonPackages = python.pkgs;
  lib-path = with pkgs; lib.makeLibraryPath [
    libffi
    openssl
    stdenv.cc.cc
  ];

in

pkgs.mkShell {

  packages = [
    pythonPackages.pip
    pythonPackages.setuptools
    pythonPackages.wheel
    pythonPackages.virtualenv
    pythonPackages.cython
    pythonPackages.pygithub
    pythonPackages.ipython
  ];

  buildInputs = [
    # C++ development tools
    pkgs.gcc       # GNU Compiler Collection
    pkgs.nodejs
    python
  ];


  hardeningDisable = [ "fortify" ];

  shellHook = ''
    echo "Development environment loaded."
    echo "Python $(python --version) installed"

    # Set LD_LIBRARY_PATH to prioritize Nix libraries
    export LD_LIBRARY_PATH="${lib-path}:$LD_LIBRARY_PATH"
    
    # Set PKG_CONFIG_PATH to help find the right OpenSSL
    export PKG_CONFIG_PATH="${pkgs.openssl.dev}/lib/pkgconfig:$PKG_CONFIG_PATH"
    
    # Set OPENSSL_DIR to explicitly point to Nix OpenSSL
    export OPENSSL_DIR="${pkgs.openssl.dev}"
    export OPENSSL_LIB_DIR="${pkgs.openssl.out}/lib"
    export OPENSSL_INCLUDE_DIR="${pkgs.openssl.dev}/include"
    
    echo "Set code-insiders alias"
    alias codeinsiders="/mnt/c/Users/machajai/AppData/Local/Programs/Microsoft\ VS\ Code\ Insiders/bin/code-insiders"
    
    # Create and activate Python virtual environment if it doesn't exist
    VENV_DIR=".venv"
    if [ ! -d "$VENV_DIR" ]; then
      echo "Creating Python virtual environment in $VENV_DIR..."
      python -m venv "$VENV_DIR" --copies
    fi

    # Activate the virtual environment
    source "$VENV_DIR/bin/activate"
    echo "Python virtual environment activated: $(which python)"

    # Install package in development mode using setup.py if it exists
    if [ -f setup.py ]; then
      echo "Installing package in development mode using setup.py..."
      pip install -e .
    elif [ -f requirements.txt ]; then
      echo "No setup.py found. Installing dependencies from requirements.txt instead..."
      pip install -r requirements.txt --no-binary aiohttp
    else
      echo "Neither setup.py nor requirements.txt found. Skipping dependencies installation."
    fi
  '';

  postShellHook = ''
    ln -sf ${python.sitePackages}/* ./.venv/lib/python3.12/site-packages
  '';
}
