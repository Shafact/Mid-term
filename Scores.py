"""
要求：

读取 report.txt 文件中的成绩；
统计每名学生总成绩、计算平均并从高到低重新排名；
汇总每一科目的平均分和总平均分（见下表第一行）；
添加名次，替换60分以下的成绩为“不及格”；
将处理后的成绩另存为一个新文件（result.txt）。
"""
"""
结果文件内容展示：

名次 姓名 语文 数学 英语 物理 化学 生物 政治 历史 地理 总分 平均分
0 平均 72 67 76 47 63 73 77 73 82 630 70.0
1 小S 94 90 96 89 92 84 83 80 82 790 87.8
2 小D 90 88 87 89 82 79 79 83 85 762 84.7
3 小A 89 94 90 96 89 92 不及格 73 80 757 84.1
...
21 小K 82 不及格 83 63 66 67 72 83 86 638 70.9
"""

""" Plans:
1. store reports each line as an element of a huge list, split each element in the huge list by " "
2. calculate and append each line's average and sum
3. sort sum -- looking for sorted() or list.sort()
4. add a new list calculation each line, insert the new list in the first place in the original huge list
5. for each element of the huge list, join them by " "
6. write each lines to the "result.txt"
"""

# define the function can readlines, split each list by " ", and convert the string to int
def read_file(path):
    with open(path) as f:
        l = [i.split() for i in f.readlines()]
        for i in range(1, len(l)):
            for j in range(1, len(l[0])):
                l[i][j] = int(l[i][j])
        return l

# define the function that can add sum and avg
def addsumavg(ls):
    total = sum(ls[1:])
    avg_score = round(total/(len(ls)-1),2)
    ls.append(total)
    ls.append(avg_score)
    return ls

# define a function that be able to sort by sum
def sortSum(ls):
    return ls[-1]

# define a function that will replace scores to "不及格"
def replace_scores(ls):
    for i in range(1, (len(ls)-2)):
        if ls[i] < 60:
            ls[i] = '不及格'
    return ls

# define a function to turn each int or float to string and combine the all list into one string
def covStr(ls):
    for i in range(len(ls)):
        ls[i] = str(ls[i])
    ls = ' '.join(ls)
    return ls


# read the file and create the scores list
scores = read_file('report.txt')

# adding sum and average scores to each elements of scores
scores[0].append('总分')
scores[0].append('平均分')
for i in range(1,len(scores)):
    addsumavg(scores[i])
print(scores)

# sort scores
sorted_scores = scores[1:]
sorted_scores.sort(key = sortSum, reverse=True)
print(sorted_scores)

# calculate summary list
summary = ['平均']
for i in range(1,(len(sorted_scores[0]))):
    total = 0
    for j in range(len(sorted_scores)):
        total += sorted_scores[j][i]
    summary.append(round(total/(len(sorted_scores)),2))
print(summary)


# replace with '不及格'
for i in range(len(sorted_scores)):
    sorted_scores[i] = replace_scores(sorted_scores[i])
print("=========== 不及格 ===========\n", sorted_scores)

# add back title and summary
sorted_scores.insert(0, summary)
sorted_scores.insert(0, scores[0])
print(sorted_scores)


# add rank
sorted_scores[0].insert(0,"名次")
for i in range(1, len(sorted_scores)):
    sorted_scores[i].insert(0,i-1)
print(sorted_scores)

# join each element of sorted_scores as one string
for i in range(len(sorted_scores)):
    sorted_scores[i] = covStr(sorted_scores[i])
print(sorted_scores)

# write into result.txt
with open('result.txt', 'w') as f:
    f.writelines([i + '\n' for i in sorted_scores])





