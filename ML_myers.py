import nn
import chainer
from chainer import Variable
import chainer.functions as F
import numpy as np
import common


def get_triangle_name(label):
	if label == 0:
		return "It's not a triangle."
	elif label == 1:
		return "It's an equilateral triangle."
	elif label == 2:
		return "It's an isosceles triangle."
	else:
		return "It's a scalene triangle."

def is_correct_number(c):
	if not c.isalnum():
		return False
	if not c.isdecimal():
		return False
	c = int(c)
	return True if c > 0 else False

def please_input(side_name):
	while True:
		print('\nEnter the length of side ' + side_name + ' as an integer (0 < n < 100000)')
		length = input().strip()
		if len(length) > 5 :
			print('Error! String too long.')
			continue
		if not is_correct_number(length):
			print('Error! Please Enter an integer (0 < n < 100000)')
			continue
		else:
			break
	return length


print('Please enter the side length of the triangle. \nAnswer the triangle type.\n\n')
inst_common = common.common()
while True:
	a = please_input('A')
	b = please_input('B')
	c = please_input('C')
	input_list = inst_common.normalization([a, b, c])

	model = nn.NN(inst_common.MID_LAYER_NUM, inst_common.OUTPUT_NUM)
	chainer.serializers.load_hdf5(inst_common.SAVE_FILE_NAME, model)

	input_data = (np.array([input_list])).astype(np.float32)
	input_data = Variable(input_data.astype(np.float32))

	result = model(input_data)
	result = F.softmax(result)
	pred_label = np.argmax(result.data, 1)
	print(get_triangle_name(pred_label))
	print('\n\nDo you want to continue? (y/n)')
	ans = input().strip()
	ans = ans.lower()
	if ans == 'n' or ans == 'no':
		break