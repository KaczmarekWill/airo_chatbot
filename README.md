# AIRO Chatbot Project
*The AIRO Chatbot is a project by the Artificial Intelligence Research Organization (AIRO) at the University of North Florida. The purpose of this bot is to provide easy access to information and services for the university while serving as a platform for studying techniques in Natural Language Processing*

## Contributing
In order to contribute to the project, please send Will Kaczmarek a private message on Discord with your student n-number. You will be given access to the gpu server where we will be developing the project.

### Contributors
1. Will Kaczmarek
1. Dominic Harshaw
1. Aaron Zellner 

### Making Your First Contribution
1. Fork this repository to your GitHub account by clicking the "Fork" button on the top-right corner of this page

2. Click the green "Clone or Download" button that appears in the top-right corner of your new forked repository and copy the link to your clipboard

3. RDC in to the gpu server using the credentials provided to you after you are added to the server

4. Move to whatever folder you would like to host the repository in, then enter the following commands in the terminal:
```
$ git init
$ git clone {paste the link you copied here}
```
You will then be prompted to enter your GitHub username and password. 

5. Once the repository is cloned, use whatever text editor you prefer to add your name to the list of contributors in README.md in the following format
  ```
  ### Contributors
  1. Will Kaczmarek
  1. {other names here}
  1. {your name here}
  ```

6. Back in the terminal, commit your changes and push them up to GitHub (and add the upstream repository)
```
$ git remote add upstream https://github.com/KaczmarekWill/airo_chatbot.git
$ git add .
$ git commit -m "Added {name here} to list of contributors"
$ git push origin master
```

7. Back in GitHub, go to *your* fork of the repository to view your changes, then click the pull requests tab and create a new pull request.

8. Once your changes are reviewed and approved, you can update your copy of the repo by syncing upstream changes
```
$ git fetch upstream
$ git checkout master
$ git merge upstream/master
```
You can then update these changes by pushing them to GitHub as we did previously
```
$ git add .
$ git commit -m "Synced to upstream"
$ git push origin master
```
**Congratulations! You are now a contributor on the AIRO Chatbot Project**

## Working with Rasa
Take some time to get familiar with the open-source Chatbot library, Rasa, by going through the [User Guide](https://rasa.com/docs/rasa/user-guide/installation/)

You will need to install Rasa using the following command:
```
$ pip3 install rasa-x --extra-index-url https://pypi.rasa.com/simple
```

Individual projects and assignments will be added as we solidify our project requirements over the coming week and will be announced on Discord as well as tracked via the GitHub "Projects" tab.

"I often tell my students not to be misled by the name 'artificial intelligence' - there is nothing artificial about it. AI is made by humans, intended to behave by humans, and, ultimately, to impact humans' lives and human society." -*Fei-Fei Li*

