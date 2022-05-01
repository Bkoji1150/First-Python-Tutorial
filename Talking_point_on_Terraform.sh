#!/bin/bash 

provider_blocks:
resources block:
terraform blocks:
datasource block:
local block:
module block:

 >>>>>: talking about  = module ("public and private module")
        why using module??
        source of your module....

>>>>>>>: variables to avoid hard coding...

>>>>>>: using local to avoid reduncies 

>>>>>>: making using data sources...


>>>>>> making using of meta arquments like count, for_each and dynamic block

>>>>>>: setting up aws backend to managed terraformd state bucket an using Dynamodb table 
for looking and data consistency 

>>>>>>> making use of lifecycle policy to ensure infrastructure consistency 
like ["create_before_destroy", "ignore_changes", "prevent_destroy"]

>>>>>>: manages infrastructure drift, using terraform state commands like
     terraform import.....
     terraform taint.....
     terraform state mv ""
     terraformstate list

>>>>>>>: making using of terraform workspaces to use one terraform manifest file to desploy to enterprise environment 

>>>>>>: build a pipline to run all terraform codes to ensure accountability amongs team

>>>>>>: terraform remote state to share re
