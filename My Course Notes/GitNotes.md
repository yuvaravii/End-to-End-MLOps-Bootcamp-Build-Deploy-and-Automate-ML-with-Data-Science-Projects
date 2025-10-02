### Git requirement

- Download git cli
- Installation of GIT

### Method 1 : Creating Repo & working from CLI

- Step 1 : download the git from website
- Step 2 : configure your account of git : [Git - Git Configuration](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration)
    - User name
    - user email id
    
    ```markdown
    $ git config --global user.name "John Doe"
    $ git config --global user.email johndoe@example.com
    
    ```
    This authenticates via browser 
    ```
    ```
    
- Step 3 : then initialize git (this creates .git hidden file)
    
    ```markdown
    git init
    ```
    
- Step 4 : check the git status
    
    ```markdown
    git status 
    
    _This command informs the status of files present within it, this gives the status of untracked files too_
    - if the files are untracked : this needs to staged (meaning the files has to be added to the meta data, then should be commited for finalizing then to be pushed to the remote)
    
    ```
    
- Step 5 : add the untracked files
    
    ```markdown
    git add "your file name"
    git add .      # this commands lets you to add all the changes we made.
    
    git restore "your file name"   # if we dont want changes to happen.
    
    git reset "your file name"   # this completely restored without any trace in meta data
    ```
    
- Step 6 : Check the branch before committing
    
    ```markdown
    git branch     # let's you know on which branch you are in.
    git branch -M main     # Renaming the master branch if so into main, for easiness.
    
    git branch "your name"   # create new branch
    
    git checkout "your new branch name"  # switching to new branch
    git branch                           # git branch name check
    
    ## Need to merge the changes of your new branch with your main branch
    git checkout main            #1. Shift to your main branch firstly
    git branch                   #2. check for your branch name 
    git merge your_new_branch    #3. Since you are in main branch, now merge it with the new branch
    git push origin main         #4. We have merged the changes, but still this has to be pushed to the main branch
    
    ```
    
- Step 7 : how to check whether it is going to push in specific repository we need.
    
    ```markdown
    git remote add origin "your repository url"
    
    git remote -v   # to check the status of branch we are located in.
    ```
    
- Step 8 : Committing the changed files
    
    ```markdown
    git commit -m "your comments"
    ```
    
- Step 9 : Pushing the files to remote
    
    ```markdown
    git push origin main  # this main can be replaced with any branches you are working in.
    
    git log     # to view all the pushes done earlier
    git log -3  # last 3 commits happened
    ```
    

### Handling Git branch conflicts (Resolving)

- When more than one developer is working on a project then there may be changes made by different users, thus there are larger difference, the conflict would arise.
    - The git branch conflicts occurs when the users try to modify the same file in the repo. So, the overcome the conflict we need to essentially remove the errors manually.
