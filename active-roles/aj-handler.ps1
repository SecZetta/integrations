$Script:Env = @{
    File = "SecZetta.csv"#"\\dc\share\SecZetta.csv"
    URL = "https://franchisedemo.mynonemployee.com/api"
    APIKey = "7b2c3db30dbf4d0e89b8df454b0657cc"
    Limit = 100
    ProfileTypes = @(
        "People"
    )
    Profiles = New-Object System.Collections.ArrayList
}

$Script:Env["Headers"] = @{
    Accept = "application/json"
    ContentType = "applicaton/json"
    Authorization = "Token token=$($Script:Env.APIKey)"
}

$ProfileTypes = (Invoke-RestMethod -URI "$($Script:Env.URL)/profile_types".ToLower() -Headers $Script:Env.Headers -Method GET -UseBasicParsing).profile_types | Where-Object name -in $Script:Env.ProfileTypes

ForEach ($ProfileType in $ProfileTypes) {
    
    $offset = 0
    $finished = $false

    while ($finished -ne $true) {

        $URI = "$($Script:Env.URL)/profiles?profile_type_id=$($ProfileType.ID)&limit=$($Script:Env.Limit)&offset=$offset"

        Try {

            $Request = Invoke-RestMethod -URI $URI -Headers $Script:Env.Headers -Method Get

            ForEach ($Person in $Request.Profiles) {

                ForEach ($Attribute in @("Status","Name","UID")) {
                    $Person.Attributes | Add-Member -MemberType NoteProperty -Name $Attribute -Value $Person.$Attribute
                }

                $Script:Env.Profiles.Add($Person) | Out-Null

            }

        } Catch {

            $StatusCode = $_.Exception.Response.StatusCode.value__

            write-host $StatusCode
            If ($StatusCode -eq 400) {
                 $finished = $true
            }
        }
            $offset += $Script:Env.Limit

    }

}

$Script:Env.Profiles.Attributes | Export-CSV $Script:Env.File -NoTypeInformation
