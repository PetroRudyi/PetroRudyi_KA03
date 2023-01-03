import unittest
import common.config as cfg
from common.dropbox_tester import DropBoxTester

tester= DropBoxTester(cfg.ACCESS_TOKEN, cfg.FILE_TO_UPLOAD, f'common/resources/{cfg.FILE_TO_UPLOAD}')


def test_file_upload():
    assert tester.file_upload().ok


def test_file_getmetadata():
    response = tester.file_getmetadata()
    assert response.json()['name'] == cfg.FILE_TO_UPLOAD
    assert response.ok


def test_file_delete():
    assert tester.file_delete().ok


if __name__ == '__main__':
    unittest.main()