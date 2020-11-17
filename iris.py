import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


# import urllib.request as req

# url = "https://github.com/pandas-dev/pandas/blob/master/pandas/tests/io/data/csv/iris.csv"

# savefile = "iris.csv"
# req.urlretrieve(url, savefile)
# print("保存しました")
# print(savefile)

# ダウンロードしたファイルの内容を表示
# csv = pd.read_csv(savefile, encoding="utf-8")
# csv
# csv = pd.read_csv(savefile, encoding="utf-8")

# csv = pd.read_csv(savefile, encoding="utf-8", error_bad_lines=False)
# csv = pd.read_csv("https://github.com/pandas-dev/pandas/blob/master/pandas/tests/io/data/csv/iris.csv", encoding="utf-8", error_bad_lines=False)
# print(csv)


# アヤメデータの読み込み

iris_data=pd.read_csv("../../iris.csv", encoding="utf-8", error_bad_lines=False)
print(iris_data)
# アヤメデータをラベルと入力データに分離する
y = iris_data.loc[:,"Name"]
x = iris_data.loc[:,["SepalLength","SepalWidth","PetalLength","PetalWidth"]]

# 学習用とテスト用に分離する
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2,
train_size = 0.8, shuffle = True)

# 学習する
clf = SVC()
clf.fit(x_train, y_train)

# 評価する
y_pred = clf.predict(x_test)
print("正解率 = ", accuracy_score(y_test, y_pred))




