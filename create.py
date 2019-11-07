import os
from argparse import ArgumentParser

from github3 import login

DEFAULT_PATH = "~/Documents/Python"

def create_parser():
    parser = ArgumentParser()
    parser.add_argument("repository", help="Creates a repository with this name, if --folder-name is not specified, it makes a folder titlecased and replaces hyphens with spaces")
    parser.add_argument("-nr", "--no-readme", help="Does not initialize a new README", action="store_true")
    parser.add_argument("-i", "--init", help="Uses the current folder for creating new repository", action="store_true")
    parser.add_argument("-v", "--verbose", help="Shows statements", action="store_true")
    parser.add_argument("-f", "--folder-name", help="If specified, creates folder name with said name")
    parser.add_argument("-p", "--path", help="This will create the folder in the specified path, rather than default")
    parser.add_argument("-c", "--commit-message", help="This will add your own commit message other than 'Initial commit'", default="Initial commit")
    
    return parser

def main():
    user = os.environ.get('GITHUB_USER')
    password = os.environ.get('GITHUB_PASS')
    
    parser = create_parser()
    
    args = parser.parse_args()
    
    repo_name = args.repository
    titled_name = repo_name.replace("-", r"\ ").title()
    
    if not args.init:
        if args.path and args.folder_name:
            path = f"{args.path}{os.path.sep}{args.folder_name}"
        elif args.path:
            path = f"{args.path}{os.path.sep}{titled_name}"
        elif args.folder_name:
            path = f"{DEFAULT_PATH}{os.path.sep}{args.folder_name}"
        else:
            path = f"{DEFAULT_PATH}{os.path.sep}{titled_name}"
        
        
        os.system(f"mkdir -p {path}")
        os.chdir(path.replace(r"\ ", " ").replace("~", os.popen("echo ~").read().split()[0]))
            
        os.system("git init")
        
        if not args.no_readme:
            if args.verbose > 1: print("echo '# "+titled_name.replace(r'\ ', ' ')+"' >> README.md; git add README.md")
            os.system("echo '# "+titled_name.replace(r'\ ', ' ')+"' >> README.md; git add README.md")
            
    else:
        os.system("git init; git add .")
        
    os.system(f"git commit -m '{args.commit_message}'")
    
    g = login(user, password=password)
    if args.verbose > 1: print("Logged in successfully!")
    r = g.create_repository(repo_name)
    
    os.system(f"git remote add origin {r.clone_url}; git push -u origin master")

    if r and args.verbose >= 1:
        print(f"Created {r.name} successfully.")
    

if __name__ == "__main__":
    main()
        
    
    
