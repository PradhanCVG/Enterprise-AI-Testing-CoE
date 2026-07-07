import subprocess


def run_ragas():
    subprocess.run(['python', '-m', 'ragas', 'run'], check=True)


if __name__ == '__main__':
    run_ragas()
