from chainer import Chain
import chainer.functions as F
import chainer.links as L


class NN(Chain):
    def __init__(self, n_hid, n_out):
        super().__init__()
        with self.init_scope():
            self.l1 = L.Linear(None, n_hid)
            self.l2 = L.Linear(n_hid, n_hid)
            self.l3 = L.Linear(n_hid, n_out)
 
    def __call__(self, x):
        h1 = F.relu(self.l1(x))
        h2 = F.relu(self.l2(h1))
        return self.l3(h2)