*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  minski  minski123
    Output Should Contain  Username is already in use

Register With Too Short Username And Valid Password
    Input Credentials  m  minski123
    Output Should Contain  Username is too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  .minski  minski123
    Output Should Contain  Username should contain only caracters a-z

Register With Valid Username And Too Short Password
    Input Credentials  minea  123
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  minea  minskiminea
    Output Should Contain  Password must contain non-letter characters

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  minski  minski123