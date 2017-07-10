from ssh_automated_tests.core.cmd_handler import VimCmdHandler
from ssh_automated_tests.core.file_handler import RemoteHomeFileHandler, TxtFileHandler
from ssh_automated_tests.core.random_generator import RandomGenerator


def test_edit_vim(connection, sftp):
    txt_file = TxtFileHandler('new_file')
    remote_file = RemoteHomeFileHandler(txt_file, 'ivan')
    random_text = RandomGenerator(10).generate_string('digits')
    vim_handler = VimCmdHandler(connection)
    vim_handler.edit_file(txt_file.get_name(), random_text)
    remote_file = sftp.open(remote_file.get_name())
    file_content = ''
    for line in remote_file:
        file_content += line
    assert random_text in file_content
