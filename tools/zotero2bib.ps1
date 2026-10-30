# Export all Zotero items (local API, Zotero must be running) to the proposal's refs.bib.
# Usage (PowerShell): powershell -ExecutionPolicy Bypass -File tools\zotero2bib.ps1
# Uses Windows' curl.exe with --noproxy, because a system proxy blocks Invoke-WebRequest to localhost.
$root = Split-Path -Parent $PSScriptRoot
$out = Join-Path $root "Thesis Proposal\proposal\ref\refs.bib"
$tmp = [System.IO.Path]::GetTempFileName()
$all = New-Object System.Text.StringBuilder
$start = 0
while ($true) {
    & curl.exe -s -f --noproxy "*" -o $tmp "http://localhost:23119/api/users/0/items/top?format=bibtex&limit=100&start=$start"
    if ($LASTEXITCODE -ne 0) { Write-Host "Zotero not reachable - is Zotero open?"; exit 1 }
    $text = [System.IO.File]::ReadAllText($tmp, [System.Text.Encoding]::UTF8)
    if ([string]::IsNullOrWhiteSpace($text)) { break }
    [void]$all.Append($text).Append("`n`n")
    $start += 100
}
Remove-Item $tmp
# Drop url/urldate lines: otherwise GB/T 7714 prints every article as [J/OL] with an access date (DOI is kept).
$lines = $all.ToString() -split "`r?`n" | Where-Object { $_ -notmatch '^\s*(url|urldate)\s*=' }
$clean = ($lines -join "`n")
[System.IO.File]::WriteAllText($out, $clean, (New-Object System.Text.UTF8Encoding($false)))
$n = ([regex]::Matches($clean, '(?m)^@')).Count
Write-Host "$n entries -> $out"
