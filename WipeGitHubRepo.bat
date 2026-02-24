@echo off
:: Ensure we are in the correct directory
cd /d "%~dp0"

echo ====================================================
echo WIPE GITHUB REPO ONLY (Prat78/Synapse)
echo ====================================================
echo.
echo This will delete ALL files from GitHub.
echo YOUR LOCAL FILES ON THIS COMPUTER WILL STAY SAFE.
echo.
pause
echo [1/3] Removing files from GitHub index...
git rm -r --cached .
echo [2/3] Creating wipe commit...
git commit -m "Wipe Remote Repository"
echo [3/3] Pushing wipe to GitHub...
git push origin main --force
echo.
echo ====================================================
echo DONE! GitHub is now EMPTY. 
echo Your local files are still here on your computer.
echo ====================================================
pause
