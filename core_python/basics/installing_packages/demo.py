import subprocess
import sys


def install(package):
    # subprocess.run([sys.executable,"-m","pip","install","--upgrade pip"])
    # subprocess.check_call([sys.executable, "-m", "ensurepip"])
    result = subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    print(result)
    # uninstall_dependency = subprocess.Popen([ "pip", "uninstall", package],
    #                                        stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    # print(uninstall_dependency.stdout)


def main():
    install("codegen")  # Demo Package
    # result = subprocess.run([sys.executable, "-c", "print('ocean')"],capture_output=True,text=True)

    # print(f"stdout: {result.stdout}")
    # print(f"stderr: {result.stderr}")


if __name__ == "__main__":
    main()
