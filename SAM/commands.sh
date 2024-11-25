# create an s3 bucket
aws s3 mb s3://wg-schoolmgmt-v1

# upload code to s3 bucket
aws cloudformation package --s3-bucket wg-schoolmgmt-v1 --template-file sam_template.yaml --output-template-file gen/template-generated.yaml

# deploy the template
aws cloudformation deploy --template-file gen\template-generated.yaml --stack-name hello-world-sam --capabilities CAPABILITY_IAM
