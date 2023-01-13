import json
import csv
#分离出用户的话语
path = "D:/A 学习/zyd/北京.json"#原始数据路径
log_path = 'D:/A 学习/zyd/beijing_data/beijing.csv'#分离出用户话语的结果文档路径
# 读取文件数据
with open(path, "r",encoding="utf-8") as f:
    row_data = json.load(f)
dict_log=[]
dict_user=[]
for i in row_data:
    # print(i)
    # dict_log=[]
    # dict_user=[]
    dict_log=i["log"]
    # print(i["log"])
    for j in dict_log:
        if j["speaker"]=="用户":
            dict_user.append(j["text"])
            # print(j["text"])
        # print(j["speaker"])
        # print(j["text"])
# print(dict_user)
rows=zip(dict_user)

with open(log_path, "w", newline='') as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row) 

#得到用户问题
q = open('D:/A 学习/zyd/beijing_data/question.csv','a+',encoding='utf-8')#得到用户问题话语的结果文档路径
line1 = ['？','?']
for l in line1:
    p = open('D:/A 学习/zyd/beijing_data/beijing.csv', 'r', encoding='utf-8')#分离出用户话语的结果文档路径
    line2 = p.readlines()
    for ll in line2:
        # print(ll)
        if l.strip() in ll:
            # print(ll)
           # print(l)
            #print(l.strip())
            q.writelines(ll)
    p.close()
# f.close()
q.close()
print("finished")