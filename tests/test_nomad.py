import os
from unittest import mock

from nomade.nomad import Nomad


class TestNomad:
    @mock.patch('os.makedirs')
    @mock.patch('shutil.copyfile')
    def test_init(self, copyfile, makedirs):
        Nomad.init()
        makedirs.assert_called_once_with(os.path.join('nomade', 'migrations'))
        assert copyfile.call_count == 2

    def test_steps_to_int_with_max_steps(self):
        assert Nomad._steps_to_int('head', 'head', 5) == 5

    def test_steps_to_int_with_valid_steps(self):
        assert Nomad._steps_to_int('10', 'head', 20) == 10

    def test_steps_to_int_with_invalid_steps(self):
        assert Nomad._steps_to_int('tail', 'head', 5) == 0
