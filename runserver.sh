#!/bin/bash
# Quick start script for Porsche Dealer Backend

echo "🚀 Porsche Dealer - Starting Setup..."
echo ""

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv .venv
    echo "✓ Virtual environment created"
fi

# Activate virtual environment
echo "📌 Activating virtual environment..."
source .venv/Scripts/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -q -r requirements.txt
echo "✓ Dependencies installed"

# Run migrations
echo "🗄️  Running database migrations..."
python manage.py migrate -q
echo "✓ Migrations complete"

# Create test data
echo "👤 Creating test dealer accounts..."
python setup.py
echo ""

echo "✅ Setup complete!"
echo ""
echo "🌐 Starting Django development server..."
echo ""
python manage.py runserver
