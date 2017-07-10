def test_create_file(shell, sftp):
    file_name = "new_test1235252"
    shell.send_command("touch {}\n".format(file_name))
    sftp.stat(file_name)
