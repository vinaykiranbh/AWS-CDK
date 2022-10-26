import aws_cdk
from aws_cdk import aws_iam
from constructs import Construct
from config import Config
import json


class IAMService():

    def create_role(scope: Construct) -> aws_iam.Role:
        lambda_principal = aws_iam.ServicePrincipal('lambda.amazonaws.com')
        s3_principal = aws_iam.ServicePrincipal('s3.amazonaws.com')
        sqs_principal = aws_iam.ServicePrincipal('sqs.amazonaws.com')
        apigateway_principal = aws_iam.ServicePrincipal('apigateway.amazonaws.com')
        
        role = aws_iam.Role(
            scope=scope,
            id=f"{Config.shortName()}Role{Config.region()}-{Config.env()}",
            role_name=f"{Config.shortName()}-role-{Config.region()}-{Config.env()}",
            assumed_by=aws_iam.CompositePrincipal(
                lambda_principal, s3_principal, sqs_principal,apigateway_principal),
            description=f"This Iam Role is used across this {Config.shortName()} Stack",
            max_session_duration=None
        )
        return role
