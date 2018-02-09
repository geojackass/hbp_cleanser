import pandas as pd
df = pd.read_csv('hbp3.tsv', delimiter='\t')
#unixtimestampがTableNameというカラムに文字列として入力されてくるので、.json以降を削除して利用する
unixt = df["Table Name"].str.extract('([0-9]+)')
dat = df.loc[:,["DATETIME(JST)","DATENAME(JST)","HOURS(JST)","sensorId","stall","status"]]
dat = pd.concat([dat, unixt], axis=1)
#カラムネームの変更を行う
columns={
"Table Name":"unixtimestamp"
}
#再度読み込みを行う
dat.rename(columns=columns, inplace=True)
dat.head()

dat1 = dat[dat.stall==1]
dat2 = dat[dat.stall==2]
dat3 = dat[dat.stall==3]

for i in range(len(dat(sti))):
    try:
        if dat(sti).iloc[i]["status"] == "open" and dat(sti).iloc[i+1]["status"] == "close":
        #print(str(i))
            cls = dat[sti].iloc[[i]]
            opn = dat[sti].iloc[[i+1]]
            d = pd.concat([cls, opn])
            #TODO stiを変数として入力する
            d.to_csv("preset/"+str(i)+".csv", index=False)
    except:
        print('indexer is out-of-bounds')

import glob
path = "preset"+str(sti)+"/" # use your path
all_files = glob.glob(path + "*.csv")
frame = pd.DataFrame()
list_ = []
for file_ in all_files:
    df = pd.read_csv(file_,index_col=None, header=0)
    list_.append(df)
frame = pd.concat(list_)
stall1 = frame.sort_values(by=['unixtimestamp'])
stall1.to_csv('stall1.csv', index=None)

cls1 = stall1[stall1.status == "close"].reset_index(drop=True).drop("status", axis=1)
#cls1 = del cls1['status']
op1 = stall1[stall1.status == "open"].reset_index(drop=True)

def rename_func(sti)
    #sti番号で指定したstallの番号に関して、fileのリネームを行い結合する準備を行う
    #カラムネームの変更を行う
    columns={
        "DATETIME(JST)":"close_time",
        "DATENAME(JST)":"DATENAME",
        "HOURS(JST)":"hour_jst"
    }
    #再度読み込みを行う
    cls[sti].rename(columns=columns, inplace=True)

    #カラムネームの変更を行う
    columns={
        "DATETIME(JST)":"open_time",
        "DATENAME(JST)":"DATENAME",
        "HOURS(JST)":"hour_jst"
    }
    #再度読み込みを行う
    op[sti].rename(columns=columns, inplace=True)

def file_out(sti)
    #そのstall番号に関して、openした時間(Series)とcloseした時間のDataFrame時間結合を行う
    f(sti) = pd.concat([op(sti)["open_time"], cls(sti), axis=1)
    f(sti).to_csv('.csv',index=False)