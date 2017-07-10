from ssh_automated_tests.core.file_handler import NoExtensionFileHandler


def test_find_string(sftp):
    new_file = NoExtensionFileHandler('/etc/hosts')
    remote_file = sftp.open(new_file.get_name())
    searchable_string = '127.0.0.1\tlocalhost'
    file_content = ''
    for line in remote_file:
        file_content += line
    assert searchable_string in file_content
