$exclude = @("venv", "rpa.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "rpa.zip" -Force