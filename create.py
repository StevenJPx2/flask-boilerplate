import os
from argparse import ArgumentParser

from github3 import login

DEFAULT_PATH = "~/Documents/Python"
GITIGNORE = f"{os.path.dirname(os.path.realpath(__file__))}{os.path.sep}gitignore.txt"

def create_parser():
    parser = ArgumentParser()
    parser.add_argument("repository", help="Creates a repository with this name, if --folder-name is not specified, it makes a folder titlecased and replaces hyphens with spaces")
    parser.add_argument("-nr", "--no-readme", help="Does not initialize a new README", action="store_true")
    parser.add_argument("-ng", "--no-gitignore", help="Does not initialize a new .gitignore", action="store_true")
    parser.add_argument("-i", "--init", help="Uses the current folder for creating new repository. By default, README is not created", action="store_true")
    parser.add_argument("-v", "--verbose", help="Shows statements", action="count", default=0)
    parser.add_argument("-f", "--folder-name", help="If specified, creates folder name with said name")
    parser.add_argument("-p", "--path", help="This will create the folder in the specified path, rather than default")
    parser.add_argument("-c", "--commit-message", help="This will add your own commit message other than 'Initial commit'", default="Initial commit")
    
    return parser

def create(args=None):
    user = os.environ.get('GITHUB_USER')
    password = os.environ.get('GITHUB_PASS')
    
    parser = create_parser()
    
    args = parser.parse_args() if args is None else parser.parse_args(args)
    
    repo_name = args.repository
    titled_name = args.folder_name or repo_name.replace("-", " ").title()
    base_path = args.path or DEFAULT_PATH
    
    if not args.init:
        path = f"{base_path}{os.sep}{titled_name}"
            
        path = os.popen(f"echo '{path}'").read().split()[0]
        
        os.makedirs(path)
        os.chdir(path)
        
        if not args.no_readme:
            if args.verbose > 1: print(f"echo '# {titled_name}' >> README.md")
            os.system(f"echo '# {titled_name}' >> README.md")
            
    if not args.no_gitignore:
        if args.verbose > 1: print(f"cp '{GITIGNORE}' '.gitignore'")
        os.system(f"cp '{GITIGNORE}' '.gitignore'")

    if args.verbose > 1: print("git init; git add .")
    os.system("git init; git add .")
    
    if args.verbose > 1: print(f"git commit -m '{args.commit_message}'")
    os.system(f"git commit -m '{args.commit_message}'")
    
    g = login(user, password=password)
    if args.verbose > 1: print("Logged in successfully!")
    r = g.create_repository(repo_name)
    
    if args.verbose > 1: print(f"git remote add origin {r.clone_url}; git push -u origin master")
    os.system(f"git remote add origin {r.clone_url}; git push -u origin master")

    if r and args.verbose >= 1:
        print(f"Created {r.name} successfully.")
    
def _main():
    create()

if __name__ == "__main__":
    _main()
        
    
    
