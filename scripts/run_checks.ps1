Write-Host "Running Agent Lab checks..." -ForegroundColor Cyan

Write-Host ""
Write-Host "Step 1: Python version"
python --version

Write-Host ""
Write-Host "Step 2: Install dependencies"
pip install -r requirements.txt

Write-Host ""
Write-Host "Step 3: Run tests"
pytest -v

Write-Host ""
Write-Host "Checks completed."