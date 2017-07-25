from ssh_automated_tests.core.file import TxtFile, RemoteHomeFile
from ssh_automated_tests.core.random_generator import RandomGenerator


def test_edit_vim(shell, sftp):
    txt_file = TxtFile('new_file')
    remote_file = RemoteHomeFile(txt_file, 'anton')
    random_text = RandomGenerator(10).generate_string('digits')
    shell.append_file_with_vim(txt_file.name(), random_text)
    remote_file = sftp.open_file(remote_file.name())
    file_content = ''
    for line in remote_file:
        file_content += line
    assert random_text in file_content
