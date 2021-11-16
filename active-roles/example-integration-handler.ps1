$file = "SecZettaProfiles.csv"
$api_key = "7b2c3db30dbf4d0e89b8df454b0657cc"
$url = "https://franchisedemo.mynonemployee.com/api"
$profile_type_id = "11116b36-a0a2-4576-989e-7fddc3c9f63e"
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
    $request_url = "$url/profiles?profile_type_id=$profile_type_id&query[limit]=$limit&query[offset]=$offset" #Alumni 40
    Write-host "$($request_url)"
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
        $person = @{
            job_title="test"

        }
        $all_profiles += $person 
        write-host "TEST"
        Write-host $all_profiles
        foreach($person in $people) {
            $person.Attributes | Add-Member -MemberType NoteProperty -Name Status -Value $person.Status
            $person.Attributes | Add-Member -MemberType NoteProperty -Name Name -Value $person.Name
            $person.Attributes | Add-Member -MemberType NoteProperty -Name UID -Value $person.uid
            $all_profiles += $person
            Write-host $person.attributes
        }
        $loop_end = (Get-Date)
        If($show_performance_metrics) { Write-Host "Loop Execution Time: $($loop_end - $loop_start)" }
        

    } catch {
        Write-Host $_


        $status_code = $_.Exception.Response.StatusCode.value__
        $error_msg = $_.ErrorDetails.Message

        write-host $status_code

        if( $status_code -eq 400 ) {
            Write-Host "Got All Profiles. Finishing up."
            $finished = $true
        }
        
        #Powershell Sucks
        #$msg = ConvertFrom-Json $error_msg
        #
        #if( $msg.error -eq "no profiles found" ){
        #    Write-Host "Got All Profiles. Finishing up."
        #    $finished = $true
        #} else {
        #    Write-Host $_
        #    Write-Error "Error: HTTP Status: $status_code  Message: $error_msg"    
        #}


        
    }

    $offset = $offset + $limit
    #$offset = 1000



}

Write-Host "Got " $all_profiles.length "Profiles"

write-host @all_profiles
$all_profiles.Attributes | Export-CSV $file

$end_ms = (Get-Date)
If($show_performance_metrics) { Write-Host "Execution Time: $($end_ms - $start_ms)" }