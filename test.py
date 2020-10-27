import sys

from subprocess import call


def install_decore():
    exit_code = call(['python', 'setup.py', 'install'])
    
    if exit_code != 0:
        sys.exit(exit_code)


def run_tests():
    exit_code = call(['python', 'manage.py', 'test', 'tests'], cwd='./tests')

    if exit_code != 0:
        sys.exit(exit_code)


if __name__ == '__main__':
    install_decore()
    run_tests()