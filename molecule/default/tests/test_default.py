import pytest
import testinfra.utils.ansible_runner
import re

def test_python_is_installed(host):
    python = host.package("python3")
    assert python.is_installed

def test_nginx_is_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed
    print (nginx.version)
    assert re.match('1.24*', nginx.version)

def test_etc_passwd_exists(host):
    passwd = host.file("/etc/passwd")
    assert passwd.exists
    assert passwd.user == "root"

def test_nginx_running_and_enabled(host):
     nginx = host.service("nginx")
     assert nginx.is_running
     assert nginx.is_enabled