#ref: https://stackoverflow.com/a/2283754 - Thanks https://stackoverflow.com/users/37786/bigjoe714

$filename = Read-Host "Enter full path to file"

$text = [string]::join([environment]::newline, (get-content -path $filename))

$sbNew = new-object system.text.stringBuilder

$pattern = "[a-fA-F0-9]{8}-([a-fA-F0-9]{4}-){3}[a-fA-F0-9]{12}"

$lastStart = 0
$null = ([regex]::matches($text, $pattern) | %{
    $sbNew.Append($text.Substring($lastStart, $_.Index - $lastStart))
    $guid = [system.guid]::newguid()
    $sbNew.Append($guid)
    $lastStart = $_.Index + $_.Length
})
$null = $sbNew.Append($text.Substring($lastStart))

$sbNew.ToString() | out-file -encoding ASCII $filename

Write-Output "Done"