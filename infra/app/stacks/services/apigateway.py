import aws_cdk
from aws_cdk import aws_iam,aws_lambda
from aws_cdk import aws_s3
from aws_cdk import aws_certificatemanager
from aws_cdk import aws_apigateway
from constructs import Construct
from config import Config
import json

class APIGService():

    def main():
        return
    def create_apig(scope: Construct):
        
        api = aws_apigateway.RestApi(scope, "test-api")
        api.root.add_method("ANY")
        api.add_domain_name(
            id='standupfounder.com',
            domain_name="standupfounder.com",
            certificate=aws_certificatemanager.Certificate.from_certificate_arn(scope, "cert", "arn:aws:acm:us-east-1:202471327519:certificate/152b0e1d-286f-428a-b8d6-349c627500b5"),
            endpoint_type=aws_apigateway.EndpointType.REGIONAL,  # default is REGIONAL
            security_policy=aws_apigateway.SecurityPolicy.TLS_1_2,
            mtls=aws_apigateway.MTLSConfig(
                bucket=aws_s3.Bucket.from_bucket_name(scope,id='existingbucket',bucket_name="vinay-us-east-1-dev-bucket43879c71-qc7c245hfmft"),
                key="truststore.pem"
            ) 
        )
        

    