import aws_cdk
from aws_cdk import Stack
from config import Config
import os
from stacks.stack import StackTemplate

Config.init()

environment = aws_cdk.Environment(
    account=Config.account(), region=Config.region()
)

StackTemplateApp = aws_cdk.App()

stack = StackTemplate(
    StackTemplateApp,
    stack_name=f"vinay-{Config.region()}-{Config.env()}",
    description=f"vinay testing for aws cdk {Config.env()}",
    env=environment,
    id=f"{Config.shortName()}-{Config.region()}-{Config.env()}"
)

StackTemplateApp.synth()


def apply_permissions_boundary(self, stack: StackTemplate) -> None:
    permission_boundary_policy = aws_cdk.aws_iam.ManagedPolicy.from_managed_policy_arn(
        stack,
        id="",
        managed_policy_arn=f"arn:aws:iam::{stack.account}:policy/app-role-boundary"
    )

    aws_cdk.aws_iam.PermissionsBoundary.of(
        stack).apply(permission_boundary_policy)
