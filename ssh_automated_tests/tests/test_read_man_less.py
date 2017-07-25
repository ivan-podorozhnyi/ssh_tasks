def test_read_man(shell):
    stdout = shell.execute_with_output("man less\n")
    while "AUTHOR" not in stdout:
        stdout = shell.send_key("SPACE")
    stdout = shell.execute_with_output("q")
    assert ":~$ " in stdout
