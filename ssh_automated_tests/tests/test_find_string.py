from ssh_automated_tests.core.file import RawFile


def test_find_string(sftp):
    new_file = RawFile('/etc/hosts')
    remote_file = sftp.open(new_file.name())
    searchable_string = '127.0.0.1\tlocalhost'
    file_content = ''
    for line in remote_file:
        file_content += line
    assert searchable_string in file_content
