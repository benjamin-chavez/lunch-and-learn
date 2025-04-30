# import os
# from itertools import islice
# from uuid import uuid4

# from aws_lambda_powertools.utilities.typing import LambdaContext
# from pydantic import BaseModel

# from common.aws.bedrock import bedrock_map_schema
# from common.aws.dynamodb import create_tablename_from_tenantname, get_table
# from common.data.schemas import get_schema, get_data_tape_example
# from common.get_source_type_schema import get_source_type_schema_dict
# from common.models.actions import Action
# from common.models.common import Status
# from common.models.schemas import FieldSchema
# from common.utils import get_file_make_df


# class LambdaEvent(BaseModel):
#     tenant_name: str
#     schema_id: str
#     data_tape_example_id: str


# def batch_dictionary(input_dict, batch_size):
#     """
#     Batches a dictionary into smaller dictionaries of a specified size.

#     Args:
#         input_dict (dict): The dictionary to batch.
#         batch_size (int): The maximum number of items in each batch.

#     Yields:
#         dict: A dictionary containing a batch of items from the input dictionary.
#     """
#     it = iter(input_dict.items())
#     while batch := dict(islice(it, batch_size)):
#         yield batch


# dytpe_map = {
#     "uint": "number",
#     "int": "number",
#     "float": "decimal",
#     "object": "string",
#     "boolean": "string",
#     "datetime": "date",
#     "string": "string",
# }


# def get_schema_from_dtypes(dtypes, parent_name=None):
#     schema = {}
#     for col_name, dtype in dtypes.items():
#         if "Unnamed" in col_name:
#             continue
#         for key, value in dytpe_map.items():
#             if str(dtype).startswith(key):
#                 schema_key = f"{parent_name}.{col_name}" if parent_name else col_name
#                 schema[schema_key] = FieldSchema(field_type=value)
#                 break
#     return schema


# def lambda_handler(event: LambdaEvent, context: LambdaContext) -> LambdaEvent:
#     s3_key = event["Records"][0]["s3"]["object"]["key"]
#     tenant_name = s3_key.split("/")[1]
#     schema_id = s3_key.split("/")[2]
#     data_tape_example_id = s3_key.split("/")[3].split(".")[0]

#     table = get_table(create_tablename_from_tenantname(tenant_name))

#     schema = get_schema(table, schema_id)

#     schema.schema_upload_status = Status.Processing.value
#     table.put_item(Item=schema.model_dump())

#     data_tape_example = get_data_tape_example(table, schema_id, data_tape_example_id)

#     data_tape = get_file_make_df(
#         data_tape_example.s3_key, os.environ.get("BUCKET_NAME")
#     )

#     tape_schema = {}

#     from pprint import pprint

#     # DataTape is an excel file with multiple sheets
#     if isinstance(data_tape, dict):
#         for sheet_name, df in data_tape.items():
#             tape_schema.update(get_schema_from_dtypes(df.dtypes, sheet_name))
#     # DataTape is a single sheet, json, or csv
#     else:
#         tape_schema.update(get_schema_from_dtypes(data_tape.dtypes))

#     schema.schema = tape_schema
#     table.put_item(Item=schema.model_dump())

#     data_tape_example.schema_ = tape_schema
#     table.put_item(Item=data_tape_example.model_dump())

#     source_schema = get_source_type_schema_dict(tenant_name, schema.source_type)

#     mappings = bedrock_map_schema(tape_schema, source_schema)

#     for source_field, target_field in mappings.items():
#         action_uid = str(uuid4())
#         action = Action(
#             pk=schema_id,
#             sk=f"action::{action_uid}::",
#             uid=action_uid,
#             schema_id=schema_id,
#             params={
#                 "name": "map_field",
#                 "source_fields": [source_field],
#                 "target_field": target_field,
#             },
#         )
#         table.put_item(Item=action.model_dump())

#     schema.schema_upload_status = Status.Complete.value
#     table.put_item(Item=schema.model_dump())

#     return event

from typing import Any


def get_loan_data() -> dict[str, Any]:
    loan_data = {"loan_id": 1}
    print(loan_data)
    # return loan_data
