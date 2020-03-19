import uuid


# def create_num(num, length=30):
#     result = []
#     while num > 0:
#         uuid_id = uuid.uuid1()
#         temp = str(uuid_id).replace('-', '')[:length]
#         if temp not in result:
#             result.append(temp)
#             num -= 1
#     print(result)
#
#
# create_num(2)


print(uuid.uuid1())