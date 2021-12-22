import platform
import subprocess

import sh; from sh import which
import typer; from typer import colors

SYSTEM = platform.system().upper()

from bullet import Check, keyhandler, styles
from bullet.charDef import NEWLINE_KEY

# Checkmark Menu Class
class MinMaxCheck(Check):
    def __init__(self, min_selections=0, max_selections=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.min_selections = min_selections
        self.max_selections = max_selections if max_selections else len(self.choices)

    @keyhandler.register(NEWLINE_KEY)
    def accept(self):
        if self.valid():
            return super().accept()

    def valid(self):
        return self.min_selections <= sum(1 for c in self.checked if c) <= self.max_selections


def check_mark_list(choices, return_index=True):
    client = MinMaxCheck(
        prompt         = "Use Space Bar to select an option...\n",
        min_selections = 1,
        max_selections = 1,
        return_index   = return_index,
        choices        = choices,
        **styles.Exam
    )
    result = client.launch()
    #print("Choice tuple: " + str(result))
    return result

def check_if_using_stack_yml():
    return False

def chmod_everything():
	subprocess.call(['chmod','-R','+x','./install_scripts/'])

# Installer Shell Scripts
def install_docker():
    """install docker, log in, add user to docker group via shell script"""
    subprocess.call([
        "chmod", "+x", "./install_scripts/install_docker.sh"
    ])
    subprocess.call([
        "./install_scripts/install_docker.sh"
    ])

def login_to_docker():
    """Run docker login"""
    subprocess.call([
        "chmod", "+x", "./install_scripts/login_to_docker.sh"
    ])
    subprocess.call([
        "./install_scripts/login_to_docker.sh"
    ])

def start_docker_on_boot(platform): #platform = systemd or init.d
    """Use SystemD to start docker and start on boot"""
    subprocess.call([
        "chmod", "+x", "./install_scripts/start_docker_on_boot.sh"
    ])
    subprocess.call([
        "./install_scripts/start_docker_on_boot.sh", platform
    ])


def install_faasd():
    """clone faasd -> install faasd"""
    subprocess.call([
        "chmod", "+x", "./install_scripts/install_faasd.sh"
    ])
    subprocess.call([
        "./install_scripts/install_faasd.sh"
    ])


def login_to_faasd():
    """log into faas-cli"""

    print("Piping the password from the pw file to faas-cli using\n" +
          "cat /var/lib/faasd/secrets/basic-auth-password | faas-cli login -s")
    cmd = "cat /var/lib/faasd/secrets/basic-auth-password | faas-cli login -s"

    ps = subprocess.Popen(cmd, shell=True,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT)
    output = ps.communicate()[0]
    print(output)

def test_faasd_python3_auto_deploy():
    # Auto generate and deploy a python faas function to test FaaSD
    subprocess.call([
        "chmod", "+x", "./install_scripts/test_faasd.sh"
    ])
    subprocess.call([
       "./install_scripts/test_faasd.sh"
    ])

# Finish me plz
def auto_deploy_all_faas_funcs_in_folder(folder='/monorepo/src/faas_functions', monorepo_path = "~/monorepo"):
    #test folder exists
    subprocess.call([
        "chmod", "+x", "./install_scripts/auto_deploy_all_faas_functions_folder.sh"
    ])
    subprocess.call([
        "./install_scripts/auto_deploy_all_faas_functions_folder.sh",
        folder
    ])


# Option Text as Arrays
top_level_choices = [
    ' Install Docker, Login, Start on Boot',
    ' Install FaaSD Server, faas-cli, test faasd) ',
    ' Express Install: Do all of the above',
    #' Util: Auto-Deploy OpenFaaS function(s) from a folder'
    ]

docker_choices = [
    ' Install Docker',
    ' Start Docker on Ubuntu using systemd',
    #' Start Docker with init.d (eg. WSL2 Ubuntu)',
    ' Login to Docker', 
    ' Express Setup: Do all of the above ']

openfaas_choices = [
    ' Install `faasd` server locally for testing functions',
    ' Test local faasd deployment using the python3 template ',
    ' Do all of the above']

auto_deploy_choices = [
    ' Auto-Deploy OpenFaaS function(s) from monorepo/src/faas_functions ',
    ' Manually input path containing the function(s) to deploy...']



def run_installer_terminal_ui():#password: str):
    if SYSTEM == "Windows":
        print("Automatic Docker & FaaSD installation is unavailable for Windows")
        return
    chmod_everything()
    # #with sh.contrib.sudo(password=password, _with=True):
    # updates = sh.Command("apt")('update', '-y', _iter=True)
    # for line in updates:
    #     print(line)

    # ## HOW TO GET A LIST OF THIS FOR FAASD??          
    # dependencies = sh.Command("apt")(
    #     'install',
    #     '-y',
    #     'make',
    #     'build-essential',
    #     'wget',
    #     'curl',
    #     'python3-openssl', 
    #     'libssl-dev', 
    #     'cmake', 
    #     'git',
    #     'runc'
    # )
    # with typer.progressbar(
    #     dependencies, label="Installing Dependencies"
    # ) as progress:
    #     for line in progress:
    #         pass #print(line)
    #########################################################
    users_choice = check_mark_list(choices=top_level_choices)
    print("\n")
    users_choice = users_choice[1][0]
    if users_choice == 0:
        users_choice = check_mark_list(choices=docker_choices)
        # (['Install Docker, Login, Start on Boot'], [0])
        users_choice = users_choice[1][0]
        if users_choice == 0:
            install_docker()
        elif users_choice == 1:
            start_docker_on_boot('systemd')
        #elif users_choice == 2: # For WSL
        #    start_docker_on_boot('init.d')
        elif users_choice == 2:
            login_to_docker()
        elif users_choice == 3:
            install_docker()
            #print("\nWhich boot manager does your system use?")
            #platform = check_mark_list(['SystemD (Ubuntu)','Init.d (WSL2 Ubuntu)', 'Exit installer'])
            #if platform == 2: return
            #else:
            #    if platform == 0:
            #        start_docker_on_boot('systemd')
            #     elif platform == 1:
            #         start_docker_on_boot('init.d')
            start_docker_on_boot('systemd')
            login_to_docker()
    elif users_choice == 1:
        users_choice = check_mark_list(choices=openfaas_choices)
        users_choice = users_choice[1][0]
        if users_choice == 0:
            #delete_default_faas_credentials()
            install_faasd()
            login_to_faasd()
        elif users_choice == 1:
            test_faasd_python3_auto_deploy()
        elif users_choice == 2:
            #delete_default_faas_credentials()
            install_faasd()
            login_to_faasd()
            test_faasd_python3_auto_deploy()
    elif users_choice == 2: # do all
        install_docker()
#        print("\nWhich boot manager does your system use?")
#        platform = check_mark_list(['SystemD (Ubuntu)','Init.d (WSL2 Ubuntu)', 'Exit installer'])
#        if platform == 2: return 'exit'
#        else:
#            if platform == 0:
#                start_docker_on_boot('systemd')
#            elif platform == 1:
#                start_docker_on_boot('init.d')
        start_docker_on_boot('systemd')
        login_to_docker()
        #delete_default_faas_credentials()
        install_faasd()
        login_to_faasd()
        test_faasd_python3_auto_deploy()
    elif users_choice == 3:
        users_choice = check_mark_list(choices=auto_deploy_choices)
        users_choice = users_choice[1][0]
        if users_choice == 0:
            auto_deploy_all_faas_funcs_in_folder()
        elif users_choice == 1:
            auto_deploy_all_faas_funcs_in_folder(folder=input('Manually input path containing the function(s) to deploy:'))
if __name__ == "__main__":
    while True:
        result = run_installer_terminal_ui()
        if result == 'exit':
            break

