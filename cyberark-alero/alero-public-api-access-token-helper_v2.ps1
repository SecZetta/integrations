
# Usage: alero-public-api-access-token-helper.ps1 -AleroSite <alero-site> -AccountFilePath <path-to-alero-account-secrets-file> -TenantID <tenantID>
# here is our URL: https://portal.alero.io/tenants/11eaab2250acefe0b97f95ccc5c5e407/settings/general

function getAuthorizationToken {

      param(
            [string] $AleroSite = 'alero.io',
            [string] $AccountFilePath = 'service-account-cyberark.json',
            [string] $TenantID = '11eaab2250acefe0b97f95ccc5c5e407'
      )

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
      Write-Host '==Private Key Start =='
      Write-Host  $rawPrivateKey
      Write-Host '==Private Key End =='
      Write-Host "$($TenantID).$($AleroServiceAccount.serviceAccountId).ExternalServiceAccount"
      #Write-Output "***********************create private key for JWT sign: *************************************************************************"
      $output = New-Item PrivateKey.pem
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

      #Write-Host JWS: $($jws)
      #Write-Host "==="
      Write-Host RSA Sig:
      Write-Host $($rsa_signature)
      Write-Host "=========="
      #Write-Host JWT: $($jwt)

      $authenticate = @{
            Method="POST"
            Uri="https://auth.$($AleroSite)/auth/realms/serviceaccounts/protocol/openid-connect/token"
            ContentType = "application/x-www-form-urlencoded"
            Body = @{
                  grant_type='client_credentials'
                  client_assertion_type='urn:ietf:params:oauth:client-assertion-type:jwt-bearer'
                  client_assertion=$JWT
            }
      }
      Write-Output "*********************** JWT token: *************************************************************************"
      #Write-Output $JWT
      #Write-Output "*********************** Access token and Refresh token: full response **************************************"
      $response=(Invoke-WebRequest -Method Post -Uri $authenticate.Uri -ContentType "application/x-www-form-urlencoded" -Body $authenticate.Body -UseBasicParsing).Content
      #Write-Output $response
      $tokendata = ConvertFrom-JSON $response
      #Write-Output "*********************** Access token: **********************************************************************"
      $tokendata.access_token

}

function getInvitations {
      Param($token)
      $authHeader = @{
            Authorization="Bearer " + $token
       }
       $URI = "https://api.alero.io/v1-edge/invitations/vendor-invitations/?limit=100&offset=0&searchIn=ALL"
       $BODY = ${

       }
      $response2=(Invoke-WebRequest -Method Get -Headers $authHeader -Uri $URI -ContentType "application/x-www-form-urlencoded" -Body $BODY -UseBasicParsing).Content
      return $response2
}

function getVendorInvitationsById {
      Param($id, $token)
      $authHeader = @{
            Authorization="Bearer " + $token
       }
      $URI = "https://api.alero.io/v1-edge/invitations/vendor-invitations/" + $id
      $BODY = ${

      }
      $response2=(Invoke-WebRequest -Method Get -Headers $authHeader -Uri $URI -ContentType "application/x-www-form-urlencoded" -Body $BODY -UseBasicParsing).Content
      return $response2
}

function getUsers {
      Param($token)
      $authHeader = @{
            Authorization="Bearer " + $token
       }
       $URI = "https://api.alero.io/v1-edge/users/"
       $BODY = ${

       }
      $response2=(Invoke-WebRequest -Method Get -Headers $authHeader -Uri $URI -ContentType "application/x-www-form-urlencoded" -Body $BODY -UseBasicParsing).Content
      return $response2
}

#got token
$token = getAuthorizationToken


#$token
$invitations = getInvitations -token $token
$users = getUsers -token $token
#$invite = getVendorInvitationsById -token $token -id "11eb267aedbffd8caba5a7d4e55fa566"
$authHeader = @{
      Authorization="Bearer " + $token
 }
 $id = "11eb267aedbffd8caba5a7d4e55fa566"
$URI = "https://api.alero.io/v1-edge/invitations/vendor-invitations/" + $id
$BODY = ${

}
Write-Output $URI
#$response2=(Invoke-WebRequest -Method Get -Headers $authHeader -Uri $URI -ContentType "application/x-www-form-urlencoded" -Body $BODY -UseBasicParsing).Content
return $response2
