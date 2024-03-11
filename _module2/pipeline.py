import subprocess


def run_script(script_name):
    subprocess.run(['python', script_name], check=True)


if __name__ == "__main__":
    run_script('module2/analyse.py')
    run_script('module2/rapport.py')
