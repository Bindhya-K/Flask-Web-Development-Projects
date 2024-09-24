from sqlalchemy import create_engine
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']
engine = create_engine(db_connection_string)

# #print(result_all)
# print(type(result_all))
# first_result_dict = result_all[0]._mapping
# print(type(first_result_dict))
# print(first_result_dict)
