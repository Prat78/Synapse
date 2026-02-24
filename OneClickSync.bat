@echo off
:: Ensure we are in the correct directory
cd /d "%~dp0"

echo ========================================
echo SYNAPSE AI - ONE CLICK GITHUB SYNC
echo ========================================
echo.
echo [1/3] Staging all local changes...
git add -A
echo [2/3] Committing changes...
git commit -m "One-Click Sync: Consolidated articles and updated ad stack"
echo [3/3] Wiping GitHub and uploading new files...
git push origin main --force
echo.
echo ========================================
echo DONE! GitHub is now a mirror of your local folder.
echo ========================================
pause
