#!/bin/bash

function flask-boilerplate(){
    python ~/Documents/Python/Flask\ Boilerplate/app.py $@
}

function create(){
    python ~/Documents/Python/Flask\ Boilerplate/create.py $@
}

function create-unittests(){
    echo "\n\n===============================  1  ===============================\n\n"
    python ~/Documents/Python/Flask\ Boilerplate/create.py hello-world
    curl -v -u $GITHUB_USER:$GITHUB_PASS -X DELETE https://api.github.com/repos/$GITHUB_USER/hello-world
    rm -rf ~/Documents/Python/Hello\ World
    echo "\n\n===============================  1  ===============================\n\n"
        
    
    echo "\n\n===============================  2  ===============================\n\n"
    python ~/Documents/Python/Flask\ Boilerplate/create.py -nr hello-world
    curl -v -u $GITHUB_USER:$GITHUB_PASS -X DELETE https://api.github.com/repos/$GITHUB_USER/hello-world
    rm -rf ~/Documents/Python/Hello\ World
    echo "\n\n===============================  2  ===============================\n\n"

    
    echo "\n\n===============================  3  ===============================\n\n"
    python ~/Documents/Python/Flask\ Boilerplate/create.py -i hello-world
    curl -v -u $GITHUB_USER:$GITHUB_PASS -X DELETE https://api.github.com/repos/$GITHUB_USER/hello-world
    rm -rf ~/Documents/Python/Hello\ World
    echo "\n\n===============================  3  ===============================\n\n"

    
    echo "\n\n===============================  4  ===============================\n\n"
    python ~/Documents/Python/Flask\ Boilerplate/create.py -v hello-world
    curl -v -u $GITHUB_USER:$GITHUB_PASS -X DELETE https://api.github.com/repos/$GITHUB_USER/hello-world
    rm -rf ~/Documents/Python/Hello\ World
    echo "\n\n===============================  4  ===============================\n\n"

    
    echo "\n\n===============================  5  ===============================\n\n"
    python ~/Documents/Python/Flask\ Boilerplate/create.py -f Hey hello-world
    curl -v -u $GITHUB_USER:$GITHUB_PASS -X DELETE https://api.github.com/repos/$GITHUB_USER/hello-world
    rm -rf ~/Documents/Python/Hey
    echo "\n\n===============================  5  ===============================\n\n"

    
    echo "\n\n===============================  6  ===============================\n\n"
    python ~/Documents/Python/Flask\ Boilerplate/create.py -p ~/Documents/Python/Hello\ World hello-world
    curl -v -u $GITHUB_USER:$GITHUB_PASS -X DELETE https://api.github.com/repos/$GITHUB_USER/hello-world
    rm -rf ~/Documents/Python/Hello\ World
    echo "\n\n===============================  6  ===============================\n\n"

    
    echo "\n\n===============================  7  ===============================\n\n"
    python ~/Documents/Flask\ Boilerplate/create.py -c "I love you bruh" hello-world
    curl -v -u $GITHUB_USER:$GITHUB_PASS -X DELETE https://api.github.com/repos/$GITHUB_USER/hello-world
    rm -rf ~/Documents/Python/Hello\ World
    echo "\n\n===============================  7  ===============================\n\n"

    

}