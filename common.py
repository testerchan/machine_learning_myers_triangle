class common:
	MID_LAYER_NUM = 64
	OUTPUT_NUM = 4
	EPOCH_NUM = 2500
	TEACHER_DATA_NAME = 'teacher_data.csv'
	SAVE_FILE_NAME = 'test.hdf5'
	IS_GPU = True

	def normalization(self, edge_list):
		edge_list = list(map(int, edge_list))
		max_length = max(edge_list)
		edge_list = [
				edge_list[0] / max_length, 
				edge_list[1] / max_length,
				edge_list[2] / max_length
		]
		return edge_list
