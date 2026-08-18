#!/bin/bash

set -e  # Exit immediately if a command fails

echo "🚀 Starting project setup..."

# -----------------------------
# 1. Check Python installation
# -----------------------------
if ! command -v python3 &> /dev/null
then
    echo "❌ Python3 not found. Installing..."

    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        sudo apt update
        sudo apt install -y python3 python3-pip python3-venv
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        brew install python
    else
        echo "⚠️ Please install Python manually."
        exit 1
    fi
else
    echo "✅ Python3 already installed"
fi

# -----------------------------
# 2. Create virtual environment
# -----------------------------
echo "📦 Creating virtual environment..."
python3 -m venv venv

# -----------------------------
# Activate virtual environment
# -----------------------------
echo "🔄 Activating virtual environment..."

if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    # Git Bash / Windows
    source venv/Scripts/activate
else
    # Linux / macOS
    source venv/bin/activate
fi
# -----------------------------

# -----------------------------
# Set venv python path
# -----------------------------
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    VENV_PYTHON="venv/Scripts/python.exe"
else
    VENV_PYTHON="venv/bin/python"
fi

echo "🐍 Using Python: $VENV_PYTHON"
# 3. Upgrade pip
# -----------------------------
echo "⬆️ Upgrading pip..."
$VENV_PYTHON -m pip install --upgrade pip

# -----------------------------
# 4. Install dependencies
# -----------------------------
if [ -f "requirements.txt" ]; then
    echo "📥 Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
else
    echo "⚠️ requirements.txt not found, installing default dependencies..."
    pip install pytest playwright pytest-playwright
fi

# -----------------------------
# 5. Install Playwright browsers
# -----------------------------
echo "🌐 Installing Playwright browsers..."
playwright install

# Optional: install system deps (important for Linux CI)
playwright install-deps || true

# -----------------------------
# 6. Verify installation
# -----------------------------
echo "🔍 Verifying setup..."

python --version
pip --version
pytest --version
playwright --version

echo "✅ Setup completed successfully!"

# -----------------------------
# 7. Run sample test (optional)
# -----------------------------
if [ -d "tests" ]; then
    echo "🧪 Running sample tests..."
    pytest || true
else
    echo "ℹ️ No tests folder found. Skipping test run."
fi

echo "🎉 You're ready to go!"
echo "👉 Activate env anytime using: source venv/bin/activate"