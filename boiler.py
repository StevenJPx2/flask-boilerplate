import os
import shutil
from tempfile import TemporaryDirectory
from argparse import ArgumentParser

from create import create

DEFAULT_PATH = "~/Documents/Python"
THUMBPRINT = "20JOEQOIFQI04NVII2HWIE92"
JQUERY_LINK = '''<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>'''



def create_parser():
    parser = ArgumentParser()
    parser.add_argument("boiler-type", help="Decides what boilerplate to use", choices=["flask"])
    parser.add_argument("repository", help="Creates a repository with this name, if --folder-name is not specified, it makes a folder titlecased and replaces hyphens with spaces")    
    parser.add_argument("-v", "--verbose", help="Shows statements", action="count", default=0)
    parser.add_argument("-c", "--commit-message", help="This will add your own commit message other than 'Initial commit'", default="Initial commit")

    parser.add_argument("-t", "--flask-type", choices="zmnfc", default="n", help="Chooses how complex or simple the flask app must be initialized: z -zero, m -minimal, n -normal (default), f -fully-fledged, c -complete")
    
    # LOCAL GROUP
    
    local_group = parser.add_argument_group('Local options', 'Options for local directory')
    local_group.add_argument("-f", "--folder-name", help="If specified, creates folder name with said name")
    local_group.add_argument("-p", "--path", help="This will create the folder in the specified path, rather than default")

    # INIT GROUP
    
    init_group = parser.add_argument_group('Components', 'Initializes separate components in the app')
    init_group.add_argument("-js", "--javascript", help="Initialize a new js file", action="store_true")
    init_group.add_argument("-jq", "--jquery", help="Initialize a new js file with jquery plugged in", action="store_true")
    init_group.add_argument("-cs", "--css", help="Initialize a new css file", action="store_true")
    
    # DB GROUP
    
    db_group = parser.add_mutually_exclusive_group()
    db_group.add_argument("-md", "--mongo-db", help="Initializes MongoDB instance", action="store_true")
    db_group.add_argument("-me", "--mongoengine", help="Initializes MongoEngine (MongoDB ORM) instance [recommended]", action="store_true")
    db_group.add_argument("-sd", "--sqlalchemy-db", help="Initializes SQLAlchemy instance", action="store_true")
    db_group.add_argument("-jd", "--json-db", help="Initializes simple JSON database", action="store_true")
    
    # FRONT-END GROUP
    
    front_group = parser.add_mutually_exclusive_group()
    front_group.add_argument("-b", "--bootstrap", help="Loads in Bootstrap v4.3 web framework", action="store_true")
    front_group.add_argument("-fb", "--flask-bootstrap", help="Loads in Flask Bootstrap (Bootstrap v3, with flask_wtf support)", action="store_true")
    
    return parser

def copy_file(source_path, destination_path, here=True, single_file=False):
    if here:
        source_path = f"{os.path.dirname(os.path.realpath(__file__))}{os.sep}{source_path}"
    if single_file:
        shutil.copy(source_path, destination_path)
    else:
        shutil.copytree(source_path, destination_path)

    
def main():
    parser = create_parser()
    
    args = parser.parse_args()
    verbose_string = f"-{'v'*args.verbose}"
    folder_name = args.folder_name or args.repository.replace("-", " ").title()
    
    if args.verbose > 2: print(parser)
    
    tmp_path = TemporaryDirectory()
    tmp_dir = f"{tmp_path}{os.sep}{folder_name}"
    
    flask_type = args.type
    if flask_type == 'z':
        copy_file("Boilerplates/zero", tmp_dir)
    elif flask_type == 'm':
        copy_file("Boilerplates/minimal", tmp_dir)
    elif flask_type == 'n':
        copy_file("Boilerplates/normal", tmp_dir)
    elif flask_type == 'f':
        copy_file("Boilerplates/fully-fledged", tmp_dir)
    elif flask_type == 'c':
        copy_file("Boilerplates/complete", tmp_dir)
        
    if args.jquery:
        pass
    if args.css:
        pass
    if args.javascript:
        pass
    
    if args.mongo_db:
        pass
    elif args.mongoengine:
        pass
    elif args.sqlalchemy_db:
        pass
    elif args.json_db:
        pass
    
    if args.bootstrap:
        pass
    elif args.flask_bootstrap:
        pass
    
    copy_file(tmp_dir, DEFAULT_PATH, here=False)
        
    

if __name__ == "__main__":
    main()
