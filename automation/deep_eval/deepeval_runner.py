import subprocess


def run_deepeval():
    subprocess.run(['python', '-m', 'deepeval', 'run'], check=True)


if __name__ == '__main__':
    run_deepeval()
