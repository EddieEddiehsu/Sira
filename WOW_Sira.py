import time as wow
choose=bool(input('選擇西拉。月守的命運:'))
if(choose==0):
    print('殺掉西拉')
    Sira='西拉死了'
    wow.sleep(5);
elif(choose==1):
    print('饒過西拉')
    wow.sleep(15);
    print('被迫將她人的命運交給納薩諾斯。凋零者')
    wow.sleep(15);
    print('納薩諾斯殺了西拉')
    Sira='西拉死了'
if(Sira=='西拉死了'):
    print('西拉死前的遺言:她……在哪裡？')
wow.sleep(10);
print('結論:西拉的命運是死亡')
