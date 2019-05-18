import chainer
from chainer import optimizers, Variable
import chainer.functions as F
import numpy as np
from sklearn import datasets, model_selection
import nn
import common


#CSV読み込み
def read_csv(file_name):
    line_list = []
    ans_list = []
    with open(file_name, 'r') as file:
        line = file.readline()
        while line:
            line = line.strip()
            edges = line.split(',')
            #正規化して学習させる
            line_list.append(inst_common.normalization(edges[:3]))
            ans_list.append(edges[-1])
            line = file.readline()
    line_list = (np.array(line_list)).astype(np.float32)       
    ans_list = (np.array(ans_list)).astype(np.int32)
    return line_list, ans_list

#精度計測
def calc_acc(test_data, test_label):
    test_data_variable = Variable(test_data.astype(np.float32))
    y = model(test_data_variable)
    y = F.softmax(y)
    pred_label = np.argmax(y.data, 1)
    return np.sum(pred_label == test_label) / np.sum(test_label)

#GPU関連
def change_gpu(model, train_data_variable, train_label_variable):
    model.to_gpu()
    train_data_variable.to_gpu()
    train_label_variable.to_gpu()
    return model, train_data_variable, train_label_variable

def change_cpu(model, train_data_variable, train_label_variable):
    model.to_cpu()
    train_data_variable.to_cpu()
    train_label_variable.to_cpu()
    return model, train_data_variable, train_label_variable


inst_common = common.common()
x, y = read_csv(inst_common.TEACHER_DATA_NAME)
#教師データとテストデータに別ける
train_data, test_data, train_label, test_label = model_selection.train_test_split(x, y, shuffle = True)

model = nn.NN(inst_common.MID_LAYER_NUM, inst_common.OUTPUT_NUM)
optimizer = optimizers.Adam()
optimizer.setup(model)

train_data_variable = Variable(train_data.astype(np.float32))
train_label_variable = Variable(train_label.astype(np.int32))

if inst_common.IS_GPU:
    model, train_data_variable, train_label_variable = change_gpu(model, train_data_variable, train_label_variable)

loss_log = []
for epoch in range(inst_common.EPOCH_NUM):
    model.cleargrads()
    prod_label = model(train_data_variable)
    loss = F.softmax_cross_entropy(prod_label, train_label_variable)
    loss.backward()
    optimizer.update()
    loss_log.append(loss.data)
    print(epoch)

if inst_common.IS_GPU:
    model, train_data_variable, train_label_variable = change_cpu(model, train_data_variable, train_label_variable)

acc = calc_acc(test_data, test_label)
print(acc)

#ファイル保存
chainer.serializers.save_hdf5(inst_common.SAVE_FILE_NAME, model)



