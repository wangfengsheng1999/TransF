import unittest

import sys
sys.path.append('./python')
# 你需要在.vscode里面添加extra地址 才能找到
import TransFTrain as train
import TransFTrain.backend_ndarray as nd
import numpy as np

class TestSaclarGe(unittest.TestCase):
    def test_case1_cpu(self):
        A = np.random.randn(5, 5)
        B = nd.array(A, device=nd.cpu)
        C = A[0, 1].item()
        np.testing.assert_allclose(A == C, (B == C).numpy(), atol=1e-5, rtol=1e-5)

    @unittest.skipIf(not nd.cuda().enabled(), "NO GPU")
    def test_case1_cuda(self):
        A = np.random.randn(5, 5)
        B = nd.array(A, device=nd.cuda())
        C = A[0, 1].item()
        np.testing.assert_allclose(A == C, (B == C).numpy(), atol=1e-5, rtol=1e-5)


if "__main__" == __name__:
    unittest.main()
