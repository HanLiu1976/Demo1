import sys
from decimal import Decimal
import matplotlib.pyplot as plt
import numpy as np
from pyral import Rally, rallyWorkset

#options = [arg for arg in sys.argv[1:] if arg.startswith('--')]
#args = [arg for arg in sys.argv[1:] if arg not in options]
#server, user, password, apikey, workspace, project = rallyWorkset(options)
# rally = Rally(server, user, password, apikey=apikey, workspace=workspace, project=project)
rally = Rally('rally1.rallydev.com', 'han.liu@sas.com', 'A@sas.com', server_ping=True)

# rally.enableLogging('mypyral.log')
rally.enableLogging(dest=sys.stdout, attrget=False, append=False)
response = rally.get('Release', fetch="Project,Name,ReleaseStartDate,ReleaseDate",
                     order="ReleaseDate")

proj1 = rally.getProjects(workspace='HLS: RnD Health and Life Sciences')
# print ("project = ", proj1.Name)


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x(), 1.03 * height, '%s' % int(height))

def autolabelfloat(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x(), 1.03*height, '%.2f' % Decimal(height))

plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False
Defect_sum=0
valid_defect_sum=0
workspaces = rally.getWorkspaces()
for wksp in workspaces:
    # print("workspace =", wksp.oid, wksp.Name )
    projects = rally.getProjects(workspace=wksp.Name)
    for proj in projects:
        # print ('project name =',proj.oid, proj.Name)
        if proj.Name.__eq__('LSAF 5.x'):
            print("We are into LSAF 5.x project")
            print("-------------------------------------------------------")
            tester_name_list = ["shuang.fu", "junru.liu", "ping.lu", "yeqian.gu", "di.chen"]
            query_time = "2020-01-01"
            i = 0
            TC_touched_list = []
            TC_duration_total_list = []
            Total_defects_list = []
            High_defects_list = []
            Valid_defects_list = []
            Valid_rate_list = []
            Duration_larger_list =[]
            while i < len(tester_name_list):
                query_criteria1 = 'Date >= "2020-01-01"' + ' and Tester contains ' + tester_name_list[i] + '@sas.com'

                response1 = rally.get('TestCaseResult', fetch=True, query=query_criteria1)

                sum = 0.0
                duration_larger =0
                # print("--------------------- " + tester_name_list[i] + "-------------------")
                for temp in response1:
                    if temp.Duration is None:
                        sum = sum

                    else:
                        sum += float(temp.Duration)
                        if float(temp.Duration) >=8:
                            duration_larger = duration_larger+1


                # print("TC touched =", response1.resultCount)
                # print("duration total =", sum)
                TC_touched_list.append(response1.resultCount)
                TC_duration_total_list.append(sum)
                Duration_larger_list.append(duration_larger)


                query_criteria2 = 'CreationDate >= "2020-01-01"' + ' and SubmittedBy contains ' + tester_name_list[
                    i] + '@sas.com'
                response2 = rally.get('Defect', fetch=True, query=query_criteria2)
                High_sum = 0
                Valid_sum = 0
                for temp1 in response2:
                    if temp1.Severity in "High,Alert":
                        High_sum = High_sum + 1
                    if temp1.Resolution in "Fixed,No Fix,Converted,N/A,None,No Bug":
                        Valid_sum = Valid_sum + 1

                Total_defects_list.append(response2.resultCount)
                Defect_sum=Defect_sum+response2.resultCount

                High_defects_list.append(High_sum)

                Valid_defects_list.append(Valid_sum)
                # print("Valid rate =", Valid_sum / response2.resultCount)
                Valid_rate_list.append(Valid_sum / response2.resultCount)
                valid_defect_sum=valid_defect_sum+Valid_sum

                i = i + 1


plt.figure()
bar_width = 0.2  # 条形宽度

plt.subplot(2, 2, 1)
index_duration_larger = np.arange(len(tester_name_list))+bar_width
plt.title('Cases number ', y=1, fontdict={'weight': 'normal', 'size': 20})
a = plt.bar(range(len(tester_name_list)), TC_touched_list, width=bar_width, color='b', label='TOTAL')
b = plt.bar(index_duration_larger, height=Duration_larger_list, width=bar_width, color='g', label='>= 8 housrs')
autolabel(a)
autolabel(b)
plt.legend()
plt.xticks(np.arange(len(tester_name_list)) + bar_width / 3,
               tester_name_list)


plt.subplot(2, 2, 2)
plt.title('Total duration time  ', y=1, fontdict={'weight': 'normal', 'size': 20})
a=plt.bar(range(len(tester_name_list)), TC_duration_total_list, tick_label=tester_name_list)
autolabel(a)

plt.subplot(2, 2, 3)
index_TotalDefects = np.arange(len(tester_name_list))  # Total 条形图的横坐标
index_ValidDefects = index_TotalDefects + bar_width  # Valid 条形图的横坐标
index_HighDefects = index_ValidDefects + bar_width  # Hig 条形图的横坐标

a = plt.bar(index_TotalDefects, height=Total_defects_list, width=bar_width, color='b', label='TOTAL')
b = plt.bar(index_ValidDefects, height=Valid_defects_list, width=bar_width, color='g', label='VALID')
c = plt.bar(index_HighDefects, height=High_defects_list, width=bar_width, color='r', label='HIGH')

autolabel(a)
autolabel(b)
autolabel(c)
plt.legend()
plt.xticks(index_TotalDefects + bar_width / 3,
               tester_name_list)
plt.ylabel('Defect number')
plt.title('2020 total defects:'+str(Defect_sum)+" and valid: "+str(valid_defect_sum))  # 图形标题

plt.subplot(2, 2, 4)
plt.title('Valid Rate ', y=1, fontdict={'weight': 'normal', 'size': 20})
a=plt.bar(range(len(tester_name_list)), Valid_rate_list, tick_label=tester_name_list)
autolabelfloat(a)

plt.show()

'''
N = 5
x = np.arange(N)
p1 = plt.bar(x, height=Total_defects_list, width=0.5, label="total", tick_label=tester_name_list)
# 添加数据标签
for a, b in zip(x, Total_defects_list):
    plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=10)

# 添加图例
plt.legend()

# 展示图形
plt.show()
'''