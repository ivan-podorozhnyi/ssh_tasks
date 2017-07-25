from ssh_automated_tests.core.file import RawFile


def test_create_file(shell, sftp):
    file = RawFile("new_test")
    shell.execute_with_output("touch {}\n".format(file.name()))
    sftp.get_file_stat(file.name())
