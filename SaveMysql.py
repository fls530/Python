import uuid
import pymysql
import time

'''
uuid库生成128位全局唯一标识符
'''

# 获取当前时间,插入数据库
now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


# 生成num个验证码，每个验证码长度位length，可设置默认长度
def create_num(num, length=30):
    result = []
    while num > 0:
        uuid_id = uuid.uuid1()
        temp = str(uuid_id).replace('-', '')[:length]
        if temp not in result:
            result.append(temp)
            num -= 1
    return result


# a = create_num(1)[0]
# print(type(a))

def save_to_mysql(mycode, date, sqltime):
    conn = pymysql.connect(
        host='35.194.141.249',
        port=3306,
        user='root',
        passwd='speaknow',
        db='GRC')
    try:
        with conn.cursor() as cursor:
            # 获取操作游标
            sql = "INSERT INTO activate_code(activate_code,date,create_time)VALUES(%s,%s,%s)"
            try:
                cursor.execute(sql, (mycode, date, sqltime))
                conn.commit()
            except Exception as e:
                print(e)

        with conn.cursor() as cursor:
            sql = "SELECT id,activate_code,date,create_time FROM activate_code WHERE activate_code=%s"
            cursor.execute(sql, mycode)
            # 使用 fetchone() 方法获取一条数据库
            result = cursor.fetchone()
            print(result)
    finally:
        conn.close()


for code in create_num(1):
    save_to_mysql(code, 12, now)
