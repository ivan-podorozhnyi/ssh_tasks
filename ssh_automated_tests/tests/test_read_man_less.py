def test_read_man(shell):
    stdout = shell.send_command("man less\n")
    while "AUTHOR" not in stdout:
        stdout = shell.send_key("SPACE")
    stdout = shell.send_command("q")
    assert ":~$ " in stdout
