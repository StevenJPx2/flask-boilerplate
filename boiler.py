import os
from argparse import ArgumentParser

from create import create


def create_parser():
    parser = ArgumentParser()
    parser.add_argument("boiler-type", help="Decides what boilerplate to use")
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
    init_group.add_argument("-js", "--javascript", help="Initialize new js file")
    init_group.add_argument("-cs", "--css", help="Initialize new css file")
    
    # DB GROUP
    
    db_group = parser.add_argument_group('Database Group', 'Initializes databases')
    db_group.add_argument("-md", "--mongo-db", help="Initializes MongoDB instance", action="store_true")
    db_group.add_argument("-sd", "--sqlalchemy-db", help="Initializes SQLAlchemy instance", action="store_true")
    db_group.add_argument("-jd", "--json-db", help="Initializes simple JSON database", action="store_true")
    
    # FRONT-END GROUP
    
    front_group = parser.add_argument_group('Front-End Frameworks', 'Initializes front-end frameworks')
    front_group.add_argument("-b", "--bootstrap", help="Loads in Bootstrap v4.3 web framework", action="store_true")
    front_group.add_argument("-fb", "--flask-bootstrap", help="Loads in Flask Bootstrap (Bootstrap v3, with flask_wtf support)", action="store_true")
    
    
    return parser
    
    
    
def main():
    pass

if __name__ == "__main__":
    main()
