# IAM Integration

## Supported Features

Use Case | Supported (Y/N)| Details
---------|----------------|------------------
IAM initiated profile aggregation | Y | via OOTB Connector
SecZetta initiated identity create  | N | via REST API
SecZetta initiated identity update  | N | via REST API
SecZetta initiated identity delete  | N | via REST API
SecZetta initiated identity enable  | N | via REST API
SecZetta initiated identity disable  | N | via REST API
Sync SecZetta risk score to IAM | N |  

### Profile Types Supported

Profile Type | Managed in IAM (Y/N) | IAM Object Type
-------------|----------------------|-------------
People       | Y                    | Identity
Organizations| N                    | N/A
Assignments  | Y                    | Account Links / Roles?
Populations  | Y                    | Job Function



