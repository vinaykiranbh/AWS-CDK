import aws_cdk
from aws_cdk import Stack
from config import Config
from stacks.services.apigateway import APIGService
from stacks.services.iamservice import IAMService
from constructs import Construct


class StackTemplate(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        StackTemplate.Create(self)

    @staticmethod
    def Create(stack: Construct):

        role = IAMService.create_role(scope=stack)

        apigateway = APIGService.create_apig(scope=stack)
       