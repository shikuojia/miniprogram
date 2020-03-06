import pymysql
import json
import xlwt
import xlrd

path ='/Users/shilei/Downloads/001.xls'
conn = pymysql.connect(host='localhost',port=3900,user='root',passwd='hepshilei',db='jszg')
# print(db)
cursor = conn.cursor(pymysql.cursors.DictCursor)
# cursor = conn.cursor()
sql = 'select * from questions_pool_old_exam_written'
cursor.execute(sql)
results = cursor.fetchall()


 ##define excel file
xls = xlwt.Workbook()
xlsx = xls.add_sheet('教师资格')

xlsx.write(0,0,'编号')
xlsx.write(0,1,'题干')
xlsx.write(0,2,'解析')
xlsx.write(0,3,'答案')
xlsx.write(0,4,'试卷编号')
xlsx.write(0,5,'题型')
xlsx.write(0,6,'分值')
xlsx.write(0,7,'选项A')
xlsx.write(0,8,'选项B')
xlsx.write(0,9,'选项C')
xlsx.write(0,10,'选项D')


# print(type(results))
# print(results)
# print(type(results['choice_item']))
# data = {}
for i in results:
    
    # data = json.loads(i['choice_item'])
    id = i['id']
    print(id)
    xlsx.write(id,0,id)#编号
    question  = i['question']
    xlsx.write(id,1,question)#编号
    choices = i['choice_item']
    answer = i['answer']
    xlsx.write(id,3,answer)#编号
    jiexi = i['question_analysis']
    xlsx.write(id,2,jiexi)#编号
    tx = i['question_type']
    xlsx.write(id,5,tx)#编号
    scores = i['each_question_score']
    xlsx.write(id,6,scores)#编号
    sjbh = i['belong_examination_paper_id']
    xlsx.write(id,4,sjbh)
    if choices is not None:
        # print(i['id'])
        choices_json = eval(choices)
        a = choices_json['A']
        b = choices_json['B']
        c = choices_json['C']
        d = choices_json['D']
        xlsx.write(id,7,a)#编号
        xlsx.write(id,8,b)#编号
        xlsx.write(id,9,c)#编号
        xlsx.write(id,10,d)#编号

        # e = choices['A']
    else:
        choices = ' '
        xlsx.write(id,7,choices)#编号
        xlsx.write(id,8,choices)#编号
        xlsx.write(id,9,choices)#编号
        xlsx.write(id,10,choices)#编号
        # print(i['id'])
    
    xls.save(path)
   

   
   

    

    
