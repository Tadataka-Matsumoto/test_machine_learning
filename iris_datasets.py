from sklearn import datasets, svm

#データを読み出す
iris = datasets.load_iris()
print("target=", iris.target) #ラベルデータ
print("data=", iris.data) #観測データ