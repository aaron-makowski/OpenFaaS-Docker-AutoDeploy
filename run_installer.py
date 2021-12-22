import subprocess

subprocess.call(["chmod", "+x", "./install_scripts/install_pip_requirements.sh"])
subprocess.call(["./install_scripts/install_pip_requirements.sh"])

# Run main installer that needs ^^^ requirements
subprocess.call(["python3","./install_scripts/docker_faasd_installer.py"])
