from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.shortcuts import render, redirect, HttpResponse

from Public import mysqldb


class userIndex(View):
    def get(self, request):
        return render(request, 'user.html')

    def post(self, request):
        return render(request, 'user.html')


class userTea(View):
    def get(self, request):
        return redirect('/user/')

    def post(self, request):
        usertea_id = request.POST.get("usertea_id", 0)
        usertea_name = request.POST.get("usertea_name", 0)

        try:
            if usertea_name:
                sql = ('''
                                              SELECT jid,user_name , password,c_time from  oracle2utf.coschuser_info  where user_name= '{}'
                                                '''.format(usertea_name))
                res = mysqldb.MysqlDB(sql=sql)
                user_name_list = res.connectdb()
                data_list = []
                if len(user_name_list)>0:
                    for i in user_name_list:
                        sql = ('''
                                                  SELECT s.name,s.school_id ,u.state_id  from user_info u , school_info s  where u.ett_user_id = {} and u.DC_SCHOOL_ID = s.school_id 
                                                                '''.format(i['jid']))
                        res = mysqldb.MysqlDB(sql=sql, db='school')
                        row = res.connectdb()[0]
                        data = dict(i, **row)
                        data_list.append(data)
                    if user_name_list:
                        return render(request, 'user.html', {'data_list': data_list})
                else:
                    masg = '没有可查询的数据'
                    return render(request, 'user.html', {'masg': masg})

            if usertea_id:

                sql = ('''
                                SELECT jid,user_name , password,c_time from  oracle2utf.coschuser_info  where jid = {}
                                  '''.format(usertea_id))
                res = mysqldb.MysqlDB(sql=sql)
                userid_list = res.connectdb()
                if len(userid_list) > 0:
                    userid_list = res.connectdb()[0]
                    sql2 = ('''
                                                SELECT s.name,s.school_id ,u.state_id  from user_info u , school_info s  where u.ett_user_id = {} and u.DC_SCHOOL_ID = s.school_id 
        
                                                  '''.format(usertea_id))
                    res2 = mysqldb.MysqlDB(sql=sql2, db='school')
                    userid_list2 = res2.connectdb()[0]
                    if userid_list2:
                        return render(request, 'user.html', {'userid_list': userid_list, 'userid_list2': userid_list2})
                else:
                    masg = '没有可查询的数据'
                    return render(request, 'user.html', {'masg': masg})

        except:
            masg = '没有可查询的数据'
            return render(request, 'user.html', {'masg': masg})


class userStu(View):
    def get(self, request):
        return redirect('/user/')

    def post(self, request):
        userstu_id = request.POST.get("userstu_id", None)
        userstu_name = request.POST.get("userstu_name", None)

        try:
            if userstu_name:
                sql = ('''
                                              SELECT user_id as 'jid',user_name , password,c_time from  oracle2utf.user_info  where user_name= '{}'
                                                '''.format(userstu_name))
                res = mysqldb.MysqlDB(sql=sql)
                user_name_list = res.connectdb()
                data_list = []
                if len(user_name_list)>0:
                    for i in user_name_list:
                        sql = ('''
                                                  SELECT s.name,s.school_id ,u.state_id  from user_info u , school_info s  where u.ett_user_id = {} and u.DC_SCHOOL_ID = s.school_id 
                                                                '''.format(i['jid']))
                        res = mysqldb.MysqlDB(sql=sql, db='school')
                        row = res.connectdb()[0]
                        data = dict(i, **row)
                        data_list.append(data)
                    if user_name_list:
                        return render(request, 'user.html', {'data_list': data_list})
                else:
                    masg = '没有可查询的数据'
                    return render(request, 'user.html', {'masg': masg})
            if userstu_id:

                sql = ('''
                                SELECT user_id as 'jid',user_name , password,c_time from  oracle2utf.user_info  where user_id = {}
                                  '''.format(userstu_id))
                res = mysqldb.MysqlDB(sql=sql)
                userid_list = res.connectdb()

                if len(userid_list) > 0:
                    userid_list = res.connectdb()[0]
                    sql2 = ('''
                                                SELECT s.name,s.school_id ,u.state_id  from user_info u , school_info s  where u.ett_user_id = {} and u.DC_SCHOOL_ID = s.school_id 

                                                  '''.format(userstu_id))
                    res2 = mysqldb.MysqlDB(sql=sql2, db='school')
                    userid_list2 = res2.connectdb()[0]
                    if userid_list2:
                        return render(request, 'user.html', {'userid_list': userid_list, 'userid_list2': userid_list2})
                else:
                    masg = '没有可查询的数据'
                    return render(request, 'user.html', {'masg': masg})
        except:
            masg = '没有可查询的数据'
            return render(request, 'user.html', {'masg': masg})
