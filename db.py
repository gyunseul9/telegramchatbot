import pymysql

class DBConnection:
    def __init__(self,host,user,password,database,charset,port):
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=database,
            charset=charset,
            port=port,
            cursorclass=pymysql.cursors.DictCursor)

    def exec_select(self,kind):
        with self.connection.cursor() as cursor:
            query = Query().get_select(kind)
            cursor.execute(query)
            data = cursor.fetchall()

        return data

    def close(self):
        self.connection.close()

    def commit(self):
        self.connection.commit()

class Query:

    def get_select(self,kind):
            
        if kind == 1:
            table = 'sendrnd'
            condition = ''
            sort = 'order by num desc limit 1'
        elif kind == 2:
            table = 'news'
            condition = ''
            sort = 'order by num desc limit 1'
        else:
            table = 'sendrnd'
            condition = ''
            sort = 'order by num desc limit 1'         

        query = 'select * from {} {} {}'.format(table,condition,sort)

        return query
