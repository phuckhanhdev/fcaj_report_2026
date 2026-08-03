#!/bin/bash
# =======================================================
# Auto Setup Script for macOS - LifeSync Report Project
# =======================================================

echo "=== [1/4] Checking Homebrew ==="
if ! command -v brew &> /dev/null; then
    echo "Homebrew not found. Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "Homebrew is already installed."
fi

echo "=== [2/4] Installing Hugo, Pandoc, Python3, and MacTeX ==="
brew install hugo pandoc python3
brew install --cask mactex-no-gui || brew install --cask mactex

echo "=== [3/4] Installing LaTeX packages via tlmgr ==="
if command -v tlmgr &> /dev/null; then
    sudo tlmgr update --self || true
    sudo tlmgr install latexmk vntex mdframed fancyhdr pdfpages float listings || true
fi

echo "=== [4/4] Installing Python dependencies ==="
python3 -m pip install --upgrade pip
python3 -m pip install pyyaml

echo ""
echo "======================================================="
echo "  SUCCESS: All requirements for macOS have been installed!"
echo "======================================================="
