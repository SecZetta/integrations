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

'"employee_number", "first_name", "last_name", "email", "job_title", "role", "phone", "mobile_phone","manager","franchise","created_by","status"' | Out-File $file

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

        
        foreach($person in $people) {
            $sz_profile = [PSCustomObject]@{}
            $sz_profile | Add-Member -MemberType NoteProperty -Name 'employee_number' -Value $person.attributes.employee_number
            $sz_profile | Add-Member -MemberType NoteProperty -Name 'first_name' -Value $person.attributes.first_name
            $sz_profile | Add-Member -MemberType NoteProperty -Name 'last_name' -Value $person.attributes.last_name
            $sz_profile | Add-Member -MemberType NoteProperty -Name 'email' -Value $person.attributes.email

            $job_titles = $person.attributes.job_title
            if( $null -eq $job_titles ) {
                $sz_profile | Add-Member -MemberType NoteProperty -Name 'job_title' -Value ""
            
            } else {
                $job_titles_fixed = $job_titles.replace(" – "," ")
                $sz_profile | Add-Member -MemberType NoteProperty -Name 'job_title' -Value $job_titles_fixed
            
            }
           
            
            $sz_profile | Add-Member -MemberType NoteProperty -Name 'role' -Value $person.attributes.role
            $sz_profile | Add-Member -MemberType NoteProperty -Name 'phone' -Value $person.attributes.phone
            $sz_profile | Add-Member -MemberType NoteProperty -Name 'mobile_phone' -Value $person.attributes.mobile_phone
            $sz_profile | Add-Member -MemberType NoteProperty -Name 'manager' -Value $person.attributes.manager
            
            $franchise = $person.attributes.person_franchise
            if( $null -eq $franchise ){
                $sz_profile | Add-Member -MemberType NoteProperty -Name 'franchise' -Value ""
            
            } else {
                $franchise_number = $franchise.substring(0,5)
                $sz_profile | Add-Member -MemberType NoteProperty -Name 'franchise' -Value $franchise_number
            }

            $sz_profile | Add-Member -MemberType NoteProperty -Name 'created_by' -Value $person.attributes.created_by
            $sz_profile | Add-Member -MemberType NoteProperty -Name 'status' -Value $person.status
            

            $all_profiles += $sz_profile

            # write-host $person.id
            # $csv_row = ""
            # $csv_row += '"' + $person.attributes.employee_number + '";'
            # $csv_row += '"' + $person.attributes.first_name + '";'
            # $csv_row += '"' + $person.attributes.last_name + '";'
            # $csv_row += '"' + $person.attributes.email + '";'
            # $csv_row += '"' + $person.attributes.job_title + '";'
            # $csv_row += '"' + $person.attributes.role + '";'
            # $csv_row += '"' + $person.attributes.phone + '";'
            # $csv_row += '"' + $person.attributes.mobile_phone + '";'
            # $csv_row += '"' + $person.attributes.manager + '";'
            
            # $franchise = $person.attributes.person_franchise
            # if( $null -eq $franchise ){
            #     $csv_row += '";"'
            # } else {
            #     $franchise_number = $franchise.substring(0,5)
            #     $csv_row += '"' + $franchise_number + '";'
            # }
            # $csv_row += '"' + $person.attributes.created_by + '";'
            # $csv_row += '"' + $person.status + '"'
            


           #Add-Content $file $csv_row
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

Write-Host "profiles"
$all_profiles | Export-Csv -path $file -Encoding UTF8


$end_ms = (Get-Date)
If($show_performance_metrics) { Write-Host "Execution Time: $($end_ms - $start_ms)" }