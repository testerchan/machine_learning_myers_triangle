import chainer
from chainer import optimizers, Variable
import chainer.functions as F
import numpy as np
from sklearn import datasets, model_selection
import nn
import config


#CSV読み込み
def read_csv(file_name):
    line_list = []
    ans_list = []
    with open(file_name, 'r') as file:
        line = file.readline()
        while line:
            line = line.strip()
            edges = line.split(',')
            line_list.append(edges[:3])
            ans_list.append(edges[-1])
            line = file.readline()
    #numpyに整形
    line_list = (np.array(line_list)).astype(np.float32)
    ans_list = (np.array(ans_list)).astype(np.float32)
    return line_list, ans_list

#精度計測
def calc_acc(test_data, test_label):
    test_data_variable = Variable(test_data.astype(np.float32))
    y = model(test_data_variable)
    y = F.softmax(y)
    pred_label = np.argmax(y.data, 1)
    return np.sum(pred_label == test_label) / np.sum(test_label)


x, y = read_csv(config.TEACHER_DATA_NAME)
#教師データとテストデータに別ける
train_data, test_data, train_label, test_label = model_selection.train_test_split(x, y, shuffle = True)

model = nn.NN(config.MID_LAYER_NUM, config.OUTPUT_NUM)
optimizer = optimizers.Adam()
optimizer.setup(model)

train_data_variable = Variable(train_data.astype(np.float32))
train_label_variable = Variable(train_label.astype(np.int32))

loss_log = []
for epoch in range(config.EPOCH_NUM):
    model.cleargrads()
    prod_label = model(train_data_variable)
    loss = F.softmax_cross_entropy(prod_label, train_label_variable)
    loss.backward()
    optimizer.update()
    loss_log.append(loss.data)
    print(epoch)

acc = calc_acc(test_data, test_label)
print(acc)

#ファイル保存
chainer.serializers.save_hdf5(config.SAVE_FILE_NAME, model)



