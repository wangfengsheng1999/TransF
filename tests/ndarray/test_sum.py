import unittest

import sys
sys.path.append('./python')
# 你需要在.vscode里面添加extra地址 才能找到
import TransFTrain as train
import TransFTrain.backend_ndarray as nd
import numpy as np
class TestSum(unittest.TestCase):
    def test_case1(self):
        shape = (4, 4)
        _A = np.random.randint(low=0, high=10, size=shape)
        A = nd.array(_A, device=nd.cpu())
        lhs = A.permute((1,0)).compact()
        assert lhs.is_compact(), "array is not compact"
        rhs = _A.transpose()
        np.testing.assert_allclose(lhs.numpy(), rhs, atol=1e-5)

    def test_case2(self):
        shape = (4, 4)
        _A = np.random.randint(low=0, high=10, size=shape)
        A = nd.array(_A, device=train.cuda())
        lhs = A.permute((1,0)).compact()
        assert lhs.is_compact(), "array is not compact"
        rhs = _A.transpose()
        np.testing.assert_allclose(lhs.numpy(), rhs, atol=1e-5)

if __name__ == '__main__':
    unittest.main()