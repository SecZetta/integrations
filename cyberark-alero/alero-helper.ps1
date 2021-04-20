
# Usage: alero-public-api-access-token-helper.ps1 -AleroSite <alero-site> -AccountFilePath <path-to-alero-account-secrets-file> -TenantID <tenantID>
param([string] $AleroSite = 'alero.io',
[string] $AccountFilePath = 'service-account-cyberark.json',
[string] $TenantID = '11eaab2250acefe0b97f95ccc5c5e407')

if($AleroSite -eq 'none' -OR $AccountFilePath -eq  'none' -OR $TenantID -eq 'none') {
Write-Output "Usage: alero-public-api-access-token-helper.ps1 -AleroSite <alero-site> -AccountFilePath <path-to-alero-account-secrets-file>"
exit
}
$AleroServiceAccount = Get-Content $AccountFilePath | ConvertFrom-Json
[string]$Header = '{"alg":"RS256","typ":"JWT"}'
$encodedHeader = [Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes($Header)) -replace '\+','-' -replace '/','_' -replace '='
$now = (Get-Date).ToUniversalTime()
$createDate = [Math]::Floor([decimal](Get-Date($now) -UFormat "%s"))
$expiryDate = [Math]::Floor([decimal](Get-Date($now.AddHours(72)) -UFormat "%s"))
$rawclaims = [Ordered]@{
aud = "https://auth.$($AleroSite)/auth/realms/serviceaccounts"
iss = "$($TenantID).$($AleroServiceAccount.serviceAccountId).ExternalServiceAccount"
sub = "$($TenantID).$($AleroServiceAccount.serviceAccountId).ExternalServiceAccount"
nbf = "0"
exp = $expiryDate
iat = $createDate
jti = [guid]::newguid()#"6"#(Get-WmiObject -Class Win32_ComputerSystemProduct).UUID
} | ConvertTo-Json
$rawclaims = $rawclaims -replace ' ' -replace "`r|`n"
$encodedclaim = [Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes($rawclaims)) -replace '\+','-' -replace '/','_' -replace '='
$jws = "$encodedheader.$encodedclaim"
$encodedjws = [System.Text.Encoding]::UTF8.GetBytes($jws)
# Create PEM file
$rawPrivateKey = $AleroServiceAccount.privateKey
Write-Output "***********************create private key for JWT sign: *************************************************************************"
New-Item PrivateKey.pem
Set-Content PrivateKey.pem $rawPrivateKey
# Create file containing the data to sign
Set-Content data.txt $jws -NoNewline
# Sign the data and store it to file
openssl dgst -sha256 -sign "PrivateKey.pem" -out "sig.txt" "data.txt"
# Read signiture
$rsa_signature = [System.IO.File]::ReadAllBytes("sig.txt")
$rsa_signature = [Convert]::ToBase64String($rsa_signature)
$rsa_signature = $rsa_signature -replace '\+','-' -replace '/','_' -replace '='
# Remove files
Remove-Item sig.txt
Remove-Item PrivateKey.pem
Remove-Item data.txt
$jwt = "$($jws).$($rsa_signature)"

Write-Output "*********************** JWT token: *************************************************************************"
$JWT

# $authenticate = @{
# Method="POST"
# Uri="https://auth.$($AleroSite)/auth/realms/serviceaccounts/protocol/openid-connect/token"
# ContentType = "application/x-www-form-urlencoded"
# Body = @{
# grant_type='client_credentials'
# client_assertion_type='urn:ietf:params:oauth:client-assertion-type:jwt-bearer'
# client_assertion=$JWT
# }
# }
# Write-Output "*********************** JWT token: *************************************************************************"
# $JWT
#Write-Output "*********************** Access token and Refresh token: full response **************************************"
# $response=(Invoke-WebRequest -Method Post -Uri $authenticate.Uri -ContentType "application/x-www-form-urlencoded" -Body $authenticate.Body -UseBasicParsing).Content
# $response
# $tokendata = ConvertFrom-JSON $response
# Write-Output "*********************** Access token: **********************************************************************"
# $tokendata.access_token
