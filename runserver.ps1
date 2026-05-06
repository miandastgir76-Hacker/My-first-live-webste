# Quick start script for Porsche Dealer Backend (Windows PowerShell)

Write-Host "🚀 Porsche Dealer - Starting Setup..." -ForegroundColor Cyan
Write-Host ""

# Check if virtual environment exists
if (-not (Test-Path ".venv")) {
    Write-Host "📦 Creating virtual environment..." -ForegroundColor Yellow
    python -m venv .venv
    Write-Host "✓ Virtual environment created" -ForegroundColor Green
}

# Activate virtual environment
Write-Host "📌 Activating virtual environment..." -ForegroundColor Yellow
& ".\.venv\Scripts\Activate.ps1"

# Install dependencies
Write-Host "📥 Installing dependencies..." -ForegroundColor Yellow
pip install -q -r requirements.txt
Write-Host "✓ Dependencies installed" -ForegroundColor Green

# Run migrations
Write-Host "🗄️  Running database migrations..." -ForegroundColor Yellow
python manage.py migrate -q
Write-Host "✓ Migrations complete" -ForegroundColor Green

# Create test data
Write-Host "👤 Creating test dealer accounts..." -ForegroundColor Yellow
python setup.py
Write-Host ""

Write-Host "✅ Setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "🌐 Starting Django development server..." -ForegroundColor Cyan
Write-Host ""
python manage.py runserver
