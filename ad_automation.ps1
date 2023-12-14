

# Active Directory Information
$domainController = "\\WIN-P0359LTU6HB.corp.globex.com"
$domainName = "corp.globexpower.com" 
$ouPath = "OU=Users,OU=TPS,OU=Departments,DC=$domainName,DC=com"

# User Information
$firstName = "Franz"
$lastName = "Ferdinand"
$username = "ferdinand"
$jobTitle = "TPS Reporting Lead"
$company = "GlobeX USA"
$office = "Springfield, OR"
$email = "ferdi@GlobeXpower.com"
$department = "TPS"

# Password for the new user (you may want to set a secure password)
$password = "P@ssw0rd123"

# Create a SecureString for the password
$securePassword = ConvertTo-SecureString -String $password -AsPlainText -Force

# Create the new user
New-ADUser -SamAccountName $username -UserPrincipalName "$username@$domainName.com" -Name "$firstName $lastName" -GivenName $firstName -Surname $lastName -DisplayName "$firstName $lastName" -Title $jobTitle -Company $company -Office $office -Email $email -Department $department -Enabled $true -Path $ouPath -AccountPassword $securePassword -ChangePasswordAtLogon $false -PasswordNeverExpires $true -Server $domainController
