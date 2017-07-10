from ssh_automated_tests.core.cmd_handler import VimCmdHandler
from ssh_automated_tests.core.file import TxtFile, RemoteHomeFile
from ssh_automated_tests.core.random_generator import RandomGenerator


def test_edit_vim(connection, sftp):
    txt_file = TxtFile('new_file')
    remote_file = RemoteHomeFile(txt_file, 'ivan')
    random_text = RandomGenerator(10).generate_string('digits')
    vim_handler = VimCmdHandler(connection)
    vim_handler.edit_file(txt_file.name(), random_text)
    remote_file = sftp.open(remote_file.name())
    file_content = ''
    for line in remote_file:
        file_content += line
    assert random_text in file_content
