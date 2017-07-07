from ssh_automated_tests.core.user import SshUser


def test_user_data():
    assert SshUser("anton", 3022, "id_rsa", "127.0.0.1")\
        .make_connection_data()["username"] == "anton"
