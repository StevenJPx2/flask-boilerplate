#!/bin/bash

function flask-boilerplate(){
    python ~/Documents/Python/Flask\ Boilerplate/app.py $@
}

function create(){
    python ~/Documents/Python/Flask\ Boilerplate/create.py $@
}

function create-unittests(){
    echo "\n\n===============================  1  ===============================\n\n"
    create hello-world
    curl -v -u $GITHUB_USER:$GITHUB_PASS -X DELETE https://api.github.com/repos/$GITHUB_USER/hello-world
    rm -rf ~/Documents/Python/Hello\ World
    echo "\n\n===================================================================\n\n"
        
    
    echo "\n\n===============================  2  ===============================\n\n"
    create -nr hello-world
    curl -v -u $GITHUB_USER:$GITHUB_PASS -X DELETE https://api.github.com/repos/$GITHUB_USER/hello-world
    rm -rf ~/Documents/Python/Hello\ World
    echo "\n\n===================================================================\n\n"

    
    echo "\n\n===============================  3  ===============================\n\n"
    create -i hello-world
    curl -v -u $GITHUB_USER:$GITHUB_PASS -X DELETE https://api.github.com/repos/$GITHUB_USER/hello-world
    rm -rf ~/Documents/Python/Hello\ World
    echo "\n\n===================================================================\n\n"

    
    echo "\n\n===============================  4  ===============================\n\n"
    create -v hello-world
    curl -v -u $GITHUB_USER:$GITHUB_PASS -X DELETE https://api.github.com/repos/$GITHUB_USER/hello-world
    rm -rf ~/Documents/Python/Hello\ World
    echo "\n\n===================================================================\n\n"

    
    echo "\n\n===============================  5  ===============================\n\n"
    create -f Hey hello-world
    curl -v -u $GITHUB_USER:$GITHUB_PASS -X DELETE https://api.github.com/repos/$GITHUB_USER/hello-world
    rm -rf ~/Documents/Python/Hey
    echo "\n\n===================================================================\n\n"

    
    echo "\n\n===============================  6  ===============================\n\n"
    create -p ~/Documents/Python/Hello\ World hello-world
    curl -v -u $GITHUB_USER:$GITHUB_PASS -X DELETE https://api.github.com/repos/$GITHUB_USER/hello-world
    rm -rf ~/Documents/Python/Hello\ World
    echo "\n\n===================================================================\n\n"

    
    echo "\n\n===============================  7  ===============================\n\n"
    create -c "I love you bruh" hello-world
    curl -v -u $GITHUB_USER:$GITHUB_PASS -X DELETE https://api.github.com/repos/$GITHUB_USER/hello-world
    rm -rf ~/Documents/Python/Hello\ World
    echo "\n\n===================================================================\n\n"

    

}