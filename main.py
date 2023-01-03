from common.dropbox_tester import DropBoxTester
import common.config as cfg

if __name__ == '__main__':
    tester = DropBoxTester(cfg.ACCESS_TOKEN, cfg.FILE_TO_UPLOAD, f'common/resources/{cfg.FILE_TO_UPLOAD}')
    print(tester.file_upload())
    print(tester.file_getmetadata())
    print(tester.file_delete())