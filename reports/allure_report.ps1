Remove-Item .\reports\allureReport -Recurse -Force
allure generate .\reports\testResult -o .\reports\allureReport
allure serve -h localhost .\reports\allureReport