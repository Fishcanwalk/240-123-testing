from program.grid_challenge import gridChallenge

import unittest


class test_grid_challenge(unittest.TestCase):
    def test_give_abc_ade_efg_is_YES(self):
        grid = ["abc", "ade", "efg"]
        self.assertEqual(gridChallenge(grid), "YES")

    def test_give_ebacd_fghij_olmkn_trpqs_xywuv_is_YES(self):
        grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]
        self.assertEqual(gridChallenge(grid), "YES")

    def test_give_mpxz_abcd_wlmf_is_NO(self):
        grid = ["mpxz", "abcd", "wlmf"]
        self.assertEqual(gridChallenge(grid), "NO")

    def test_give_a_is_YES(self):
        grid = ["a"]
        self.assertEqual(gridChallenge(grid), "YES")

    def test_give_zyx_wvu_tsr_is_NO(self):
        grid = ["zyx", "wvu", "tsr"]
        self.assertEqual(gridChallenge(grid), "NO")

    def test_give_abc_hjk_mpq_rtv_is_YES(self):
        grid = ["abc", "hjk", "mpq", "rtv"]
        self.assertEqual(gridChallenge(grid), "YES")
