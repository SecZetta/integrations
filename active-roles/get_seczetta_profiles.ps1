$file = "SecZettaProfiles.csv"
$api_key = "c6bda210f92142188032f5a7b59ed0f6"
$url = "https://idproofdemo.nonemployee.com/api"
$limit = 100
$offset = 0
$show_performance_metrics = $false
$start_ms = (Get-Date)
$finished = $false
$all_profiles = @()

$header = @{
    "Content-Type" = "application/json"
    "Authorization" = "Token token=$api_key"
    "Accept"=  "application/json"
}


while( $finished -ne $true ) {

    Write-host "Limit: " $limit " Offset: " $offset
    #$request_url = "$url/profiles?profile_type_id=5666f53e-cdd8-4420-8431-ca6e62e81451&query[limit]=$limit&query[offset]=$offset" #People 5
    $request_url = "$url/profiles?profile_type_id=efa0e8e1-a193-4596-9081-ccf4ea9d0c07&query[limit]=$limit&query[offset]=$offset" #Alumni 40
    #$request_url = "$url/profile_types"
    $params = @{
        Uri         = $request_url
        Headers      = $header
        Method      = 'GET'
        Body        = $null
    }

    

    try {
        
        $api_start = (Get-Date)
        $request = Invoke-RestMethod @params
        $api_end = (Get-Date)

        If($show_performance_metrics) { Write-Host "API Execution Time: $($api_end - $api_start)" }
        $people = $request.profiles
        
        $loop_start = (Get-Date)
        foreach($person in $people) {
            $person.Attributes | Add-Member -MemberType NoteProperty -Name Status -Value $person.Status
            $person.Attributes | Add-Member -MemberType NoteProperty -Name UID -Value $person.uid
            $all_profiles += $person
        }
        $loop_end = (Get-Date)
        If($show_performance_metrics) { Write-Host "Loop Execution Time: $($loop_end - $loop_start)" }
        

    } catch {
        Write-Host $_


        $status_code = $_.Exception.Response.StatusCode.value__
        $error_msg = $_.ErrorDetails.Message
        
        $msg = ConvertFrom-Json $error_msg
        
        if( $msg.error -eq "no profiles found" ){
            Write-Host "Got All Profiles. Finishing up."
            $finished = $true
        } else {
            Write-Host $_
            Write-Error "Error: HTTP Status: $status_code  Message: $error_msg"    
        }


        
    }

    $offset = $offset + $limit
    #$offset = 1000



}

Write-Host "Got " $all_profiles.length "Profiles"

$all_profiles.Attributes | Export-CSV $file -NoTypeInformation

$end_ms = (Get-Date)
If($show_performance_metrics) { Write-Host "Execution Time: $($end_ms - $start_ms)" }