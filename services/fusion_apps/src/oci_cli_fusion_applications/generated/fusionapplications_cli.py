# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli.cli_root import cli
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('fusion_apps.fusion_apps_root_group.command_name', 'fusion-apps'), cls=CommandGroupWithAlias, help=cli_util.override('fusion_apps.fusion_apps_root_group.help', """Use the Fusion Applications Environment Management API to manage the environments where your Fusion Applications run. For more information, see the [Fusion Applications Environment Management documentation]."""), short_help=cli_util.override('fusion_apps.fusion_apps_root_group.short_help', """Fusion Applications Environment Management API"""))
@cli_util.help_option_group
def fusion_apps_root_group():
    pass


@click.command(cli_util.override('fusion_apps.fusion_environment_family_group.command_name', 'fusion-environment-family'), cls=CommandGroupWithAlias, help="""Details of a Fusion environment family. An environment family is a logical grouping of environments. The environment family defines a set of characteristics that are shared across the environments to allow consistent management and maintenance across your production, test, and development environments. For more information, see [Planning an Environment Family].""")
@cli_util.help_option_group
def fusion_environment_family_group():
    pass


@click.command(cli_util.override('fusion_apps.refresh_activity_group.command_name', 'refresh-activity'), cls=CommandGroupWithAlias, help="""An environment refresh copies data from a source environment to a target environment, making a copy of the source environment onto the target environment. For more information, see [Refreshing an Environment].""")
@cli_util.help_option_group
def refresh_activity_group():
    pass


@click.command(cli_util.override('fusion_apps.work_request_log_entry_group.command_name', 'work-request-log-entry'), cls=CommandGroupWithAlias, help="""A log message from the execution of a work request.""")
@cli_util.help_option_group
def work_request_log_entry_group():
    pass


@click.command(cli_util.override('fusion_apps.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""A description of workrequest status""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('fusion_apps.create_refresh_activity_details_group.command_name', 'create-refresh-activity-details'), cls=CommandGroupWithAlias, help="""The information about current refresh.""")
@cli_util.help_option_group
def create_refresh_activity_details_group():
    pass


@click.command(cli_util.override('fusion_apps.fusion_environment_group.command_name', 'fusion-environment'), cls=CommandGroupWithAlias, help="""Description of FusionEnvironment.""")
@cli_util.help_option_group
def fusion_environment_group():
    pass


@click.command(cli_util.override('fusion_apps.data_masking_activity_group.command_name', 'data-masking-activity'), cls=CommandGroupWithAlias, help="""Details of data masking activity.""")
@cli_util.help_option_group
def data_masking_activity_group():
    pass


@click.command(cli_util.override('fusion_apps.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""An error encountered while executing a work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('fusion_apps.service_attachment_group.command_name', 'service-attachment'), cls=CommandGroupWithAlias, help="""Description of ServiceAttachment.""")
@cli_util.help_option_group
def service_attachment_group():
    pass


@click.command(cli_util.override('fusion_apps.fusion_environment_status_group.command_name', 'fusion-environment-status'), cls=CommandGroupWithAlias, help="""The health status of the Fusion Applications environment. For more information, see [Environment Status].""")
@cli_util.help_option_group
def fusion_environment_status_group():
    pass


@click.command(cli_util.override('fusion_apps.time_available_for_refresh_group.command_name', 'time-available-for-refresh'), cls=CommandGroupWithAlias, help="""one available refresh time.""")
@cli_util.help_option_group
def time_available_for_refresh_group():
    pass


@click.command(cli_util.override('fusion_apps.fusion_environment_family_limits_and_usage_group.command_name', 'fusion-environment-family-limits-and-usage'), cls=CommandGroupWithAlias, help="""Details of EnvironmentLimits.""")
@cli_util.help_option_group
def fusion_environment_family_limits_and_usage_group():
    pass


@click.command(cli_util.override('fusion_apps.scheduled_activity_group.command_name', 'scheduled-activity'), cls=CommandGroupWithAlias, help="""Details of scheduled activity.""")
@cli_util.help_option_group
def scheduled_activity_group():
    pass


fusion_apps_root_group.add_command(fusion_environment_family_group)
fusion_apps_root_group.add_command(refresh_activity_group)
fusion_apps_root_group.add_command(work_request_log_entry_group)
fusion_apps_root_group.add_command(work_request_group)
fusion_apps_root_group.add_command(create_refresh_activity_details_group)
fusion_apps_root_group.add_command(fusion_environment_group)
fusion_apps_root_group.add_command(data_masking_activity_group)
fusion_apps_root_group.add_command(work_request_error_group)
fusion_apps_root_group.add_command(service_attachment_group)
fusion_apps_root_group.add_command(fusion_environment_status_group)
fusion_apps_root_group.add_command(time_available_for_refresh_group)
fusion_apps_root_group.add_command(fusion_environment_family_limits_and_usage_group)
fusion_apps_root_group.add_command(scheduled_activity_group)


@fusion_environment_group.command(name=cli_util.override('fusion_apps.change_fusion_environment_compartment.command_name', 'change-compartment'), help=u"""Moves a FusionEnvironment into a different compartment. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeFusionEnvironmentCompartment)""")
@cli_util.option('--fusion-environment-id', required=True, help=u"""unique FusionEnvironment identifier""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_fusion_environment_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, fusion_environment_id, compartment_id, if_match):

    if isinstance(fusion_environment_id, six.string_types) and len(fusion_environment_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('fusion_apps', 'fusion_applications', ctx)
    result = client.change_fusion_environment_compartment(
        fusion_environment_id=fusion_environment_id,
        change_fusion_environment_compartment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@fusion_environment_family_group.command(name=cli_util.override('fusion_apps.change_fusion_environment_family_compartment.command_name', 'change-compartment'), help=u"""Moves a FusionEnvironmentFamily into a different compartment. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeFusionEnvironmentFamilyCompartment)""")
@cli_util.option('--fusion-environment-family-id', required=True, help=u"""The unique identifier (OCID) of the FusionEnvironmentFamily.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_fusion_environment_family_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, fusion_environment_family_id, compartment_id, if_match):

    if isinstance(fusion_environment_family_id, six.string_types) and len(fusion_environment_family_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-family-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('fusion_apps', 'fusion_applications', ctx)
    result = client.change_fusion_environment_family_compartment(
        fusion_environment_family_id=fusion_environment_family_id,
        change_fusion_environment_family_compartment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@data_masking_activity_group.command(name=cli_util.override('fusion_apps.create_data_masking_activity.command_name', 'create'), help=u"""Creates a new DataMaskingActivity. \n[Command Reference](createDataMaskingActivity)""")
@cli_util.option('--fusion-environment-id', required=True, help=u"""unique FusionEnvironment identifier""")
@cli_util.option('--is-resume-data-masking', type=click.BOOL, help=u"""This allows the Data Safe service to resume the previously failed data masking activity.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def create_data_masking_activity(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, fusion_environment_id, is_resume_data_masking):

    if isinstance(fusion_environment_id, six.string_types) and len(fusion_environment_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if is_resume_data_masking is not None:
        _details['isResumeDataMasking'] = is_resume_data_masking

    client = cli_util.build_client('fusion_apps', 'fusion_applications', ctx)
    result = client.create_data_masking_activity(
        fusion_environment_id=fusion_environment_id,
        create_data_masking_activity_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@fusion_environment_group.command(name=cli_util.override('fusion_apps.create_fusion_environment.command_name', 'create'), help=u"""Creates a new FusionEnvironment. \n[Command Reference](createFusionEnvironment)""")
@cli_util.option('--display-name', required=True, help=u"""FusionEnvironment Identifier can be renamed.""")
@cli_util.option('--compartment-id', required=True, help=u"""The unique identifier (OCID) of the compartment where the Fusion Environment is located.""")
@cli_util.option('--fusion-environment-family-id', required=True, help=u"""The unique identifier (OCID) of the Fusion Environment Family that the Fusion Environment belongs to.""")
@cli_util.option('--fusion-environment-type', required=True, help=u"""The type of environment. Valid values are Production, Test, or Development.""")
@cli_util.option('--create-fusion-environment-admin-user-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--maintenance-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--kms-key-id', help=u"""byok kms keyId""")
@cli_util.option('--dns-prefix', help=u"""DNS prefix.""")
@cli_util.option('--additional-language-packs', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Language packs.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Rules.

This option is a JSON list with items of type Rule.  For documentation on Rule please see our API reference: https://docs.cloud.oracle.com/api/#/en/fusionapplications/20211201/datatypes/Rule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'maintenance-policy': {'module': 'fusion_apps', 'class': 'MaintenancePolicy'}, 'additional-language-packs': {'module': 'fusion_apps', 'class': 'list[string]'}, 'rules': {'module': 'fusion_apps', 'class': 'list[Rule]'}, 'create-fusion-environment-admin-user-details': {'module': 'fusion_apps', 'class': 'CreateFusionEnvironmentAdminUserDetails'}, 'freeform-tags': {'module': 'fusion_apps', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'fusion_apps', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'maintenance-policy': {'module': 'fusion_apps', 'class': 'MaintenancePolicy'}, 'additional-language-packs': {'module': 'fusion_apps', 'class': 'list[string]'}, 'rules': {'module': 'fusion_apps', 'class': 'list[Rule]'}, 'create-fusion-environment-admin-user-details': {'module': 'fusion_apps', 'class': 'CreateFusionEnvironmentAdminUserDetails'}, 'freeform-tags': {'module': 'fusion_apps', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'fusion_apps', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_fusion_environment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, fusion_environment_family_id, fusion_environment_type, create_fusion_environment_admin_user_details, maintenance_policy, kms_key_id, dns_prefix, additional_language_packs, rules, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id
    _details['fusionEnvironmentFamilyId'] = fusion_environment_family_id
    _details['fusionEnvironmentType'] = fusion_environment_type
    _details['createFusionEnvironmentAdminUserDetails'] = cli_util.parse_json_parameter("create_fusion_environment_admin_user_details", create_fusion_environment_admin_user_details)

    if maintenance_policy is not None:
        _details['maintenancePolicy'] = cli_util.parse_json_parameter("maintenance_policy", maintenance_policy)

    if kms_key_id is not None:
        _details['kmsKeyId'] = kms_key_id

    if dns_prefix is not None:
        _details['dnsPrefix'] = dns_prefix

    if additional_language_packs is not None:
        _details['additionalLanguagePacks'] = cli_util.parse_json_parameter("additional_language_packs", additional_language_packs)

    if rules is not None:
        _details['rules'] = cli_util.parse_json_parameter("rules", rules)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('fusion_apps', 'fusion_applications', ctx)
    result = client.create_fusion_environment(
        create_fusion_environment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@fusion_environment_group.command(name=cli_util.override('fusion_apps.create_fusion_environment_admin_user.command_name', 'create-fusion-environment-admin-user'), help=u"""Create a FusionEnvironment admin user \n[Command Reference](createFusionEnvironmentAdminUser)""")
@cli_util.option('--username', required=True, help=u"""The username for the administrator.""")
@cli_util.option('--password', required=True, help=u"""The password for the administrator.""")
@cli_util.option('--email-address', required=True, help=u"""The email address for the administrator.""")
@cli_util.option('--first-name', required=True, help=u"""The administrator's first name.""")
@cli_util.option('--last-name', required=True, help=u"""The administrator's last name.""")
@cli_util.option('--fusion-environment-id', required=True, help=u"""unique FusionEnvironment identifier""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def create_fusion_environment_admin_user(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, username, password, email_address, first_name, last_name, fusion_environment_id):

    if isinstance(fusion_environment_id, six.string_types) and len(fusion_environment_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['username'] = username
    _details['password'] = password
    _details['emailAddress'] = email_address
    _details['firstName'] = first_name
    _details['lastName'] = last_name

    client = cli_util.build_client('fusion_apps', 'fusion_applications', ctx)
    result = client.create_fusion_environment_admin_user(
        fusion_environment_id=fusion_environment_id,
        create_fusion_environment_admin_user_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@fusion_environment_family_group.command(name=cli_util.override('fusion_apps.create_fusion_environment_family.command_name', 'create'), help=u"""Creates a new FusionEnvironmentFamily. \n[Command Reference](createFusionEnvironmentFamily)""")
@cli_util.option('--display-name', required=True, help=u"""A friendly name for the environment family. The name must contain only letters, numbers, dashes, and underscores. Can be changed later.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment where the environment family is located.""")
@cli_util.option('--subscription-ids', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of the IDs of the applications subscriptions that are associated with the environment family.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--family-maintenance-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'family-maintenance-policy': {'module': 'fusion_apps', 'class': 'FamilyMaintenancePolicy'}, 'subscription-ids': {'module': 'fusion_apps', 'class': 'list[string]'}, 'freeform-tags': {'module': 'fusion_apps', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'fusion_apps', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'family-maintenance-policy': {'module': 'fusion_apps', 'class': 'FamilyMaintenancePolicy'}, 'subscription-ids': {'module': 'fusion_apps', 'class': 'list[string]'}, 'freeform-tags': {'module': 'fusion_apps', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'fusion_apps', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_fusion_environment_family(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, subscription_ids, family_maintenance_policy, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id
    _details['subscriptionIds'] = cli_util.parse_json_parameter("subscription_ids", subscription_ids)

    if family_maintenance_policy is not None:
        _details['familyMaintenancePolicy'] = cli_util.parse_json_parameter("family_maintenance_policy", family_maintenance_policy)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('fusion_apps', 'fusion_applications', ctx)
    result = client.create_fusion_environment_family(
        create_fusion_environment_family_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@create_refresh_activity_details_group.command(name=cli_util.override('fusion_apps.create_refresh_activity.command_name', 'create-refresh-activity'), help=u"""Creates a new RefreshActivity. \n[Command Reference](createRefreshActivity)""")
@cli_util.option('--fusion-environment-id', required=True, help=u"""unique FusionEnvironment identifier""")
@cli_util.option('--source-fusion-environment-id', required=True, help=u"""The [OCID] of the source environment""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def create_refresh_activity(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, fusion_environment_id, source_fusion_environment_id):

    if isinstance(fusion_environment_id, six.string_types) and len(fusion_environment_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['sourceFusionEnvironmentId'] = source_fusion_environment_id

    client = cli_util.build_client('fusion_apps', 'fusion_applications', ctx)
    result = client.create_refresh_activity(
        fusion_environment_id=fusion_environment_id,
        create_refresh_activity_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@fusion_environment_group.command(name=cli_util.override('fusion_apps.delete_fusion_environment.command_name', 'delete'), help=u"""Deletes the Fusion environment identified by it's OCID. \n[Command Reference](deleteFusionEnvironment)""")
@cli_util.option('--fusion-environment-id', required=True, help=u"""unique FusionEnvironment identifier""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_fusion_environment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, fusion_environment_id, if_match):

    if isinstance(fusion_environment_id, six.string_types) and len(fusion_environment_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('fusion_apps', 'fusion_applications', ctx)
    result = client.delete_fusion_environment(
        fusion_environment_id=fusion_environment_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@fusion_environment_group.command(name=cli_util.override('fusion_apps.delete_fusion_environment_admin_user.command_name', 'delete-fusion-environment-admin-user'), help=u"""Deletes the FusionEnvironment administrator user identified by the username. \n[Command Reference](deleteFusionEnvironmentAdminUser)""")
@cli_util.option('--admin-username', required=True, help=u"""The admin user name for the fusion environment.""")
@cli_util.option('--fusion-environment-id', required=True, help=u"""unique FusionEnvironment identifier""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_fusion_environment_admin_user(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, admin_username, fusion_environment_id, if_match):

    if isinstance(admin_username, six.string_types) and len(admin_username.strip()) == 0:
        raise click.UsageError('Parameter --admin-username cannot be whitespace or empty string')

    if isinstance(fusion_environment_id, six.string_types) and len(fusion_environment_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('fusion_apps', 'fusion_applications', ctx)
    result = client.delete_fusion_environment_admin_user(
        admin_username=admin_username,
        fusion_environment_id=fusion_environment_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@fusion_environment_family_group.command(name=cli_util.override('fusion_apps.delete_fusion_environment_family.command_name', 'delete'), help=u"""Deletes a FusionEnvironmentFamily resource by identifier \n[Command Reference](deleteFusionEnvironmentFamily)""")
@cli_util.option('--fusion-environment-family-id', required=True, help=u"""The unique identifier (OCID) of the FusionEnvironmentFamily.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_fusion_environment_family(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, fusion_environment_family_id, if_match):

    if isinstance(fusion_environment_family_id, six.string_types) and len(fusion_environment_family_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-family-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('fusion_apps', 'fusion_applications', ctx)
    result = client.delete_fusion_environment_family(
        fusion_environment_family_id=fusion_environment_family_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@data_masking_activity_group.command(name=cli_util.override('fusion_apps.get_data_masking_activity.command_name', 'get'), help=u"""Gets a DataMaskingActivity by identifier \n[Command Reference](getDataMaskingActivity)""")
@cli_util.option('--fusion-environment-id', required=True, help=u"""unique FusionEnvironment identifier""")
@cli_util.option('--data-masking-activity-id', required=True, help=u"""Unique DataMasking run identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'fusion_apps', 'class': 'DataMaskingActivity'})
@cli_util.wrap_exceptions
def get_data_masking_activity(ctx, from_json, fusion_environment_id, data_masking_activity_id):

    if isinstance(fusion_environment_id, six.string_types) and len(fusion_environment_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-id cannot be whitespace or empty string')

    if isinstance(data_masking_activity_id, six.string_types) and len(data_masking_activity_id.strip()) == 0:
        raise click.UsageError('Parameter --data-masking-activity-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('fusion_apps', 'fusion_applications', ctx)
    result = client.get_data_masking_activity(
        fusion_environment_id=fusion_environment_id,
        data_masking_activity_id=data_masking_activity_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@fusion_environment_group.command(name=cli_util.override('fusion_apps.get_fusion_environment.command_name', 'get'), help=u"""Gets a FusionEnvironment by identifier \n[Command Reference](getFusionEnvironment)""")
@cli_util.option('--fusion-environment-id', required=True, help=u"""unique FusionEnvironment identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'fusion_apps', 'class': 'FusionEnvironment'})
@cli_util.wrap_exceptions
def get_fusion_environment(ctx, from_json, fusion_environment_id):

    if isinstance(fusion_environment_id, six.string_types) and len(fusion_environment_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('fusion_apps', 'fusion_applications', ctx)
    result = client.get_fusion_environment(
        fusion_environment_id=fusion_environment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@fusion_environment_family_group.command(name=cli_util.override('fusion_apps.get_fusion_environment_family.command_name', 'get'), help=u"""Retrieves a fusion environment family identified by its OCID. \n[Command Reference](getFusionEnvironmentFamily)""")
@cli_util.option('--fusion-environment-family-id', required=True, help=u"""The unique identifier (OCID) of the FusionEnvironmentFamily.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'fusion_apps', 'class': 'FusionEnvironmentFamily'})
@cli_util.wrap_exceptions
def get_fusion_environment_family(ctx, from_json, fusion_environment_family_id):

    if isinstance(fusion_environment_family_id, six.string_types) and len(fusion_environment_family_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-family-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('fusion_apps', 'fusion_applications', ctx)
    result = client.get_fusion_environment_family(
        fusion_environment_family_id=fusion_environment_family_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@fusion_environment_family_limits_and_usage_group.command(name=cli_util.override('fusion_apps.get_fusion_environment_family_limits_and_usage.command_name', 'get'), help=u"""Gets the number of environments (usage) of each type in the fusion environment family, as well as the limit that's allowed to be created based on the group's associated subscriptions. \n[Command Reference](getFusionEnvironmentFamilyLimitsAndUsage)""")
@cli_util.option('--fusion-environment-family-id', required=True, help=u"""The unique identifier (OCID) of the FusionEnvironmentFamily.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'fusion_apps', 'class': 'FusionEnvironmentFamilyLimitsAndUsage'})
@cli_util.wrap_exceptions
def get_fusion_environment_family_limits_and_usage(ctx, from_json, fusion_environment_family_id):

    if isinstance(fusion_environment_family_id, six.string_types) and len(fusion_environment_family_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-family-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('fusion_apps', 'fusion_applications', ctx)
    result = client.get_fusion_environment_family_limits_and_usage(
        fusion_environment_family_id=fusion_environment_family_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@fusion_environment_family_group.command(name=cli_util.override('fusion_apps.get_fusion_environment_family_subscription_detail.command_name', 'get-fusion-environment-family-subscription-detail'), help=u"""Gets the subscription details of an fusion environment family. \n[Command Reference](getFusionEnvironmentFamilySubscriptionDetail)""")
@cli_util.option('--fusion-environment-family-id', required=True, help=u"""The unique identifier (OCID) of the FusionEnvironmentFamily.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'fusion_apps', 'class': 'SubscriptionDetail'})
@cli_util.wrap_exceptions
def get_fusion_environment_family_subscription_detail(ctx, from_json, fusion_environment_family_id):

    if isinstance(fusion_environment_family_id, six.string_types) and len(fusion_environment_family_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-family-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('fusion_apps', 'fusion_applications', ctx)
    result = client.get_fusion_environment_family_subscription_detail(
        fusion_environment_family_id=fusion_environment_family_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@fusion_environment_status_group.command(name=cli_util.override('fusion_apps.get_fusion_environment_status.command_name', 'get'), help=u"""Gets the status of a Fusion environment identified by its OCID. \n[Command Reference](getFusionEnvironmentStatus)""")
@cli_util.option('--fusion-environment-id', required=True, help=u"""unique FusionEnvironment identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'fusion_apps', 'class': 'FusionEnvironmentStatus'})
@cli_util.wrap_exceptions
def get_fusion_environment_status(ctx, from_json, fusion_environment_id):

    if isinstance(fusion_environment_id, six.string_types) and len(fusion_environment_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('fusion_apps', 'fusion_applications', ctx)
    result = client.get_fusion_environment_status(
        fusion_environment_id=fusion_environment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@refresh_activity_group.command(name=cli_util.override('fusion_apps.get_refresh_activity.command_name', 'get'), help=u"""Gets a RefreshActivity by identifier \n[Command Reference](getRefreshActivity)""")
@cli_util.option('--fusion-environment-id', required=True, help=u"""unique FusionEnvironment identifier""")
@cli_util.option('--refresh-activity-id', required=True, help=u"""The unique identifier (OCID) of the Refresh activity.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'fusion_apps', 'class': 'RefreshActivity'})
@cli_util.wrap_exceptions
def get_refresh_activity(ctx, from_json, fusion_environment_id, refresh_activity_id):

    if isinstance(fusion_environment_id, six.string_types) and len(fusion_environment_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-id cannot be whitespace or empty string')

    if isinstance(refresh_activity_id, six.string_types) and len(refresh_activity_id.strip()) == 0:
        raise click.UsageError('Parameter --refresh-activity-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('fusion_apps', 'fusion_applications', ctx)
    result = client.get_refresh_activity(
        fusion_environment_id=fusion_environment_id,
        refresh_activity_id=refresh_activity_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@scheduled_activity_group.command(name=cli_util.override('fusion_apps.get_scheduled_activity.command_name', 'get'), help=u"""Gets a ScheduledActivity by identifier \n[Command Reference](getScheduledActivity)""")
@cli_util.option('--fusion-environment-id', required=True, help=u"""unique FusionEnvironment identifier""")
@cli_util.option('--scheduled-activity-id', required=True, help=u"""Unique ScheduledActivity identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'fusion_apps', 'class': 'ScheduledActivity'})
@cli_util.wrap_exceptions
def get_scheduled_activity(ctx, from_json, fusion_environment_id, scheduled_activity_id):

    if isinstance(fusion_environment_id, six.string_types) and len(fusion_environment_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-id cannot be whitespace or empty string')

    if isinstance(scheduled_activity_id, six.string_types) and len(scheduled_activity_id.strip()) == 0:
        raise click.UsageError('Parameter --scheduled-activity-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('fusion_apps', 'fusion_applications', ctx)
    result = client.get_scheduled_activity(
        fusion_environment_id=fusion_environment_id,
        scheduled_activity_id=scheduled_activity_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@service_attachment_group.command(name=cli_util.override('fusion_apps.get_service_attachment.command_name', 'get'), help=u"""Gets a Service Attachment by identifier \n[Command Reference](getServiceAttachment)""")
@cli_util.option('--fusion-environment-id', required=True, help=u"""unique FusionEnvironment identifier""")
@cli_util.option('--service-attachment-id', required=True, help=u"""OCID of the Service Attachment""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'fusion_apps', 'class': 'ServiceAttachment'})
@cli_util.wrap_exceptions
def get_service_attachment(ctx, from_json, fusion_environment_id, service_attachment_id):

    if isinstance(fusion_environment_id, six.string_types) and len(fusion_environment_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-id cannot be whitespace or empty string')

    if isinstance(service_attachment_id, six.string_types) and len(service_attachment_id.strip()) == 0:
        raise click.UsageError('Parameter --service-attachment-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('fusion_apps', 'fusion_applications', ctx)
    result = client.get_service_attachment(
        fusion_environment_id=fusion_environment_id,
        service_attachment_id=service_attachment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('fusion_apps.get_work_request.command_name', 'get'), help=u"""Gets the status of the work request with the given ID. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'fusion_apps', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('fusion_apps', 'fusion_applications', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@fusion_environment_group.command(name=cli_util.override('fusion_apps.list_admin_users.command_name', 'list-admin-users'), help=u"""List all FusionEnvironment admin users \n[Command Reference](listAdminUsers)""")
@cli_util.option('--fusion-environment-id', required=True, help=u"""unique FusionEnvironment identifier""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'fusion_apps', 'class': 'AdminUserCollection'})
@cli_util.wrap_exceptions
def list_admin_users(ctx, from_json, all_pages, fusion_environment_id):

    if isinstance(fusion_environment_id, six.string_types) and len(fusion_environment_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('fusion_apps', 'fusion_applications', ctx)
    result = client.list_admin_users(
        fusion_environment_id=fusion_environment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_masking_activity_group.command(name=cli_util.override('fusion_apps.list_data_masking_activities.command_name', 'list'), help=u"""Returns a list of DataMaskingActivities. \n[Command Reference](listDataMaskingActivities)""")
@cli_util.option('--fusion-environment-id', required=True, help=u"""unique FusionEnvironment identifier""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), help=u"""A filter that returns all resources that match the specified status""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_CREATED", "DISPLAY_NAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'fusion_apps', 'class': 'DataMaskingActivityCollection'})
@cli_util.wrap_exceptions
def list_data_masking_activities(ctx, from_json, all_pages, page_size, fusion_environment_id, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(fusion_environment_id, six.string_types) and len(fusion_environment_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-id cannot be whitespace or empty string')

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('fusion_apps', 'fusion_applications', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_data_masking_activities,
            fusion_environment_id=fusion_environment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_data_masking_activities,
            limit,
            page_size,
            fusion_environment_id=fusion_environment_id,
            **kwargs
        )
    else:
        result = client.list_data_masking_activities(
            fusion_environment_id=fusion_environment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@fusion_environment_family_group.command(name=cli_util.override('fusion_apps.list_fusion_environment_families.command_name', 'list'), help=u"""Returns a list of FusionEnvironmentFamilies. \n[Command Reference](listFusionEnvironmentFamilies)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--fusion-environment-family-id', help=u"""The ID of the fusion environment family in which to list resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter that returns all resources that match the specified lifecycle state.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_CREATED", "DISPLAY_NAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'fusion_apps', 'class': 'FusionEnvironmentFamilyCollection'})
@cli_util.wrap_exceptions
def list_fusion_environment_families(ctx, from_json, all_pages, page_size, compartment_id, fusion_environment_family_id, display_name, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if fusion_environment_family_id is not None:
        kwargs['fusion_environment_family_id'] = fusion_environment_family_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('fusion_apps', 'fusion_applications', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_fusion_environment_families,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_fusion_environment_families,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_fusion_environment_families(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@fusion_environment_group.command(name=cli_util.override('fusion_apps.list_fusion_environments.command_name', 'list'), help=u"""Returns a list of FusionEnvironments. \n[Command Reference](listFusionEnvironments)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--fusion-environment-family-id', help=u"""The ID of the fusion environment family in which to list resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter that returns all resources that match the specified lifecycle state.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_CREATED", "DISPLAY_NAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'fusion_apps', 'class': 'FusionEnvironmentCollection'})
@cli_util.wrap_exceptions
def list_fusion_environments(ctx, from_json, all_pages, page_size, compartment_id, fusion_environment_family_id, display_name, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if fusion_environment_family_id is not None:
        kwargs['fusion_environment_family_id'] = fusion_environment_family_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('fusion_apps', 'fusion_applications', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_fusion_environments,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_fusion_environments,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_fusion_environments(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@refresh_activity_group.command(name=cli_util.override('fusion_apps.list_refresh_activities.command_name', 'list'), help=u"""Returns a list of RefreshActivities. \n[Command Reference](listRefreshActivities)""")
@cli_util.option('--fusion-environment-id', required=True, help=u"""unique FusionEnvironment identifier""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--time-scheduled-start-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""A filter that returns all resources that are scheduled after this date""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-expected-finish-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""A filter that returns all resources that end before this date""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), help=u"""A filter that returns all resources that match the specified status""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_CREATED", "DISPLAY_NAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'fusion_apps', 'class': 'RefreshActivityCollection'})
@cli_util.wrap_exceptions
def list_refresh_activities(ctx, from_json, all_pages, page_size, fusion_environment_id, display_name, time_scheduled_start_greater_than_or_equal_to, time_expected_finish_less_than_or_equal_to, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(fusion_environment_id, six.string_types) and len(fusion_environment_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-id cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if time_scheduled_start_greater_than_or_equal_to is not None:
        kwargs['time_scheduled_start_greater_than_or_equal_to'] = time_scheduled_start_greater_than_or_equal_to
    if time_expected_finish_less_than_or_equal_to is not None:
        kwargs['time_expected_finish_less_than_or_equal_to'] = time_expected_finish_less_than_or_equal_to
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('fusion_apps', 'fusion_applications', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_refresh_activities,
            fusion_environment_id=fusion_environment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_refresh_activities,
            limit,
            page_size,
            fusion_environment_id=fusion_environment_id,
            **kwargs
        )
    else:
        result = client.list_refresh_activities(
            fusion_environment_id=fusion_environment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@scheduled_activity_group.command(name=cli_util.override('fusion_apps.list_scheduled_activities.command_name', 'list'), help=u"""Returns a list of ScheduledActivities. \n[Command Reference](listScheduledActivities)""")
@cli_util.option('--fusion-environment-id', required=True, help=u"""unique FusionEnvironment identifier""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--time-scheduled-start-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""A filter that returns all resources that are scheduled after this date""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-expected-finish-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""A filter that returns all resources that end before this date""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--run-cycle', type=custom_types.CliCaseInsensitiveChoice(["QUARTERLY", "MONTHLY", "ONEOFF", "VERTEX"]), help=u"""A filter that returns all resources that match the specified run cycle.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), help=u"""A filter that returns all resources that match the specified status""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_CREATED", "DISPLAY_NAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'fusion_apps', 'class': 'ScheduledActivityCollection'})
@cli_util.wrap_exceptions
def list_scheduled_activities(ctx, from_json, all_pages, page_size, fusion_environment_id, display_name, time_scheduled_start_greater_than_or_equal_to, time_expected_finish_less_than_or_equal_to, run_cycle, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(fusion_environment_id, six.string_types) and len(fusion_environment_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-id cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if time_scheduled_start_greater_than_or_equal_to is not None:
        kwargs['time_scheduled_start_greater_than_or_equal_to'] = time_scheduled_start_greater_than_or_equal_to
    if time_expected_finish_less_than_or_equal_to is not None:
        kwargs['time_expected_finish_less_than_or_equal_to'] = time_expected_finish_less_than_or_equal_to
    if run_cycle is not None:
        kwargs['run_cycle'] = run_cycle
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('fusion_apps', 'fusion_applications', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_scheduled_activities,
            fusion_environment_id=fusion_environment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_scheduled_activities,
            limit,
            page_size,
            fusion_environment_id=fusion_environment_id,
            **kwargs
        )
    else:
        result = client.list_scheduled_activities(
            fusion_environment_id=fusion_environment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@service_attachment_group.command(name=cli_util.override('fusion_apps.list_service_attachments.command_name', 'list'), help=u"""Returns a list of service attachments. \n[Command Reference](listServiceAttachments)""")
@cli_util.option('--fusion-environment-id', required=True, help=u"""unique FusionEnvironment identifier""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter that returns all resources that match the specified lifecycle state.""")
@cli_util.option('--service-instance-type', type=custom_types.CliCaseInsensitiveChoice(["DIGITAL_ASSISTANT", "INTEGRATION_CLOUD", "ANALYTICS_WAREHOUSE", "VBCS", "VISUAL_BUILDER_STUDIO"]), help=u"""A filter that returns all resources that match the specified lifecycle state.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_CREATED", "DISPLAY_NAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'fusion_apps', 'class': 'ServiceAttachmentCollection'})
@cli_util.wrap_exceptions
def list_service_attachments(ctx, from_json, all_pages, page_size, fusion_environment_id, display_name, lifecycle_state, service_instance_type, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(fusion_environment_id, six.string_types) and len(fusion_environment_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-id cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if service_instance_type is not None:
        kwargs['service_instance_type'] = service_instance_type
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('fusion_apps', 'fusion_applications', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_service_attachments,
            fusion_environment_id=fusion_environment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_service_attachments,
            limit,
            page_size,
            fusion_environment_id=fusion_environment_id,
            **kwargs
        )
    else:
        result = client.list_service_attachments(
            fusion_environment_id=fusion_environment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@time_available_for_refresh_group.command(name=cli_util.override('fusion_apps.list_time_available_for_refreshes.command_name', 'list'), help=u"""Gets available refresh time for this fusion environment \n[Command Reference](listTimeAvailableForRefreshes)""")
@cli_util.option('--fusion-environment-id', required=True, help=u"""unique FusionEnvironment identifier""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_CREATED", "DISPLAY_NAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'fusion_apps', 'class': 'TimeAvailableForRefreshCollection'})
@cli_util.wrap_exceptions
def list_time_available_for_refreshes(ctx, from_json, all_pages, page_size, fusion_environment_id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(fusion_environment_id, six.string_types) and len(fusion_environment_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('fusion_apps', 'fusion_applications', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_time_available_for_refreshes,
            fusion_environment_id=fusion_environment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_time_available_for_refreshes,
            limit,
            page_size,
            fusion_environment_id=fusion_environment_id,
            **kwargs
        )
    else:
        result = client.list_time_available_for_refreshes(
            fusion_environment_id=fusion_environment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('fusion_apps.list_work_request_errors.command_name', 'list'), help=u"""Return a (paginated) list of errors for a given work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'fusion_apps', 'class': 'WorkRequestErrorCollection'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, sort_by, sort_order, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('fusion_apps', 'fusion_applications', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_errors,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_errors,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_errors(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_log_entry_group.command(name=cli_util.override('fusion_apps.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Return a (paginated) list of logs for a given work request. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'fusion_apps', 'class': 'WorkRequestLogEntryCollection'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('fusion_apps', 'fusion_applications', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_logs,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_logs,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_logs(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('fusion_apps.list_work_requests.command_name', 'list'), help=u"""Lists the work requests in a compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help=u"""A filter to return only resources their lifecycleState matches the given OperationStatus.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--resource-id', help=u"""The ID of the a resource in which to list associated resources.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'fusion_apps', 'class': 'WorkRequestSummaryCollection'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, status, sort_by, sort_order, resource_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if status is not None:
        kwargs['status'] = status
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if resource_id is not None:
        kwargs['resource_id'] = resource_id
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('fusion_apps', 'fusion_applications', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_requests,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_requests,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_work_requests(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@fusion_environment_group.command(name=cli_util.override('fusion_apps.reset_fusion_environment_password.command_name', 'reset-fusion-environment-password'), help=u"""Resets the password of the Fusion Environment Administrator. \n[Command Reference](resetFusionEnvironmentPassword)""")
@cli_util.option('--password', required=True, help=u"""Admin password""")
@cli_util.option('--fusion-environment-id', required=True, help=u"""unique FusionEnvironment identifier""")
@cli_util.option('--admin-username', required=True, help=u"""The admin user name for the fusion environment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def reset_fusion_environment_password(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, password, fusion_environment_id, admin_username, if_match):

    if isinstance(fusion_environment_id, six.string_types) and len(fusion_environment_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-id cannot be whitespace or empty string')

    if isinstance(admin_username, six.string_types) and len(admin_username.strip()) == 0:
        raise click.UsageError('Parameter --admin-username cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['password'] = password

    client = cli_util.build_client('fusion_apps', 'fusion_applications', ctx)
    result = client.reset_fusion_environment_password(
        fusion_environment_id=fusion_environment_id,
        admin_username=admin_username,
        reset_fusion_environment_password_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@fusion_environment_group.command(name=cli_util.override('fusion_apps.update_fusion_environment.command_name', 'update'), help=u"""Updates the FusionEnvironment \n[Command Reference](updateFusionEnvironment)""")
@cli_util.option('--fusion-environment-id', required=True, help=u"""unique FusionEnvironment identifier""")
@cli_util.option('--display-name', help=u"""FusionEnvironment Identifier, can be renamed""")
@cli_util.option('--kms-key-id', help=u"""byok kms keyId""")
@cli_util.option('--maintenance-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--additional-language-packs', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Language packs""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Network access control rules to limit internet traffic that can access the environment. For more information, see [AllowRule Reference].

This option is a JSON list with items of type Rule.  For documentation on Rule please see our API reference: https://docs.cloud.oracle.com/api/#/en/fusionapplications/20211201/datatypes/Rule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'maintenance-policy': {'module': 'fusion_apps', 'class': 'MaintenancePolicy'}, 'additional-language-packs': {'module': 'fusion_apps', 'class': 'list[string]'}, 'rules': {'module': 'fusion_apps', 'class': 'list[Rule]'}, 'freeform-tags': {'module': 'fusion_apps', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'fusion_apps', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'maintenance-policy': {'module': 'fusion_apps', 'class': 'MaintenancePolicy'}, 'additional-language-packs': {'module': 'fusion_apps', 'class': 'list[string]'}, 'rules': {'module': 'fusion_apps', 'class': 'list[Rule]'}, 'freeform-tags': {'module': 'fusion_apps', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'fusion_apps', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_fusion_environment(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, fusion_environment_id, display_name, kms_key_id, maintenance_policy, additional_language_packs, rules, freeform_tags, defined_tags, if_match):

    if isinstance(fusion_environment_id, six.string_types) and len(fusion_environment_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-id cannot be whitespace or empty string')
    if not force:
        if maintenance_policy or additional_language_packs or rules or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to maintenance-policy and additional-language-packs and rules and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if kms_key_id is not None:
        _details['kmsKeyId'] = kms_key_id

    if maintenance_policy is not None:
        _details['maintenancePolicy'] = cli_util.parse_json_parameter("maintenance_policy", maintenance_policy)

    if additional_language_packs is not None:
        _details['additionalLanguagePacks'] = cli_util.parse_json_parameter("additional_language_packs", additional_language_packs)

    if rules is not None:
        _details['rules'] = cli_util.parse_json_parameter("rules", rules)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('fusion_apps', 'fusion_applications', ctx)
    result = client.update_fusion_environment(
        fusion_environment_id=fusion_environment_id,
        update_fusion_environment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@fusion_environment_family_group.command(name=cli_util.override('fusion_apps.update_fusion_environment_family.command_name', 'update'), help=u"""Updates the FusionEnvironmentFamily \n[Command Reference](updateFusionEnvironmentFamily)""")
@cli_util.option('--fusion-environment-family-id', required=True, help=u"""The unique identifier (OCID) of the FusionEnvironmentFamily.""")
@cli_util.option('--display-name', help=u"""A friendly name for the environment family. The name must contain only letters, numbers, dashes, and underscores. Can be changed later.""")
@cli_util.option('--family-maintenance-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--subscription-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of the IDs of the applications subscriptions that are associated with the environment family.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'family-maintenance-policy': {'module': 'fusion_apps', 'class': 'UpdateFamilyMaintenancePolicyDetails'}, 'subscription-ids': {'module': 'fusion_apps', 'class': 'list[string]'}, 'freeform-tags': {'module': 'fusion_apps', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'fusion_apps', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'family-maintenance-policy': {'module': 'fusion_apps', 'class': 'UpdateFamilyMaintenancePolicyDetails'}, 'subscription-ids': {'module': 'fusion_apps', 'class': 'list[string]'}, 'freeform-tags': {'module': 'fusion_apps', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'fusion_apps', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_fusion_environment_family(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, fusion_environment_family_id, display_name, family_maintenance_policy, subscription_ids, freeform_tags, defined_tags, if_match):

    if isinstance(fusion_environment_family_id, six.string_types) and len(fusion_environment_family_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-family-id cannot be whitespace or empty string')
    if not force:
        if family_maintenance_policy or subscription_ids or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to family-maintenance-policy and subscription-ids and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if family_maintenance_policy is not None:
        _details['familyMaintenancePolicy'] = cli_util.parse_json_parameter("family_maintenance_policy", family_maintenance_policy)

    if subscription_ids is not None:
        _details['subscriptionIds'] = cli_util.parse_json_parameter("subscription_ids", subscription_ids)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('fusion_apps', 'fusion_applications', ctx)
    result = client.update_fusion_environment_family(
        fusion_environment_family_id=fusion_environment_family_id,
        update_fusion_environment_family_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)
