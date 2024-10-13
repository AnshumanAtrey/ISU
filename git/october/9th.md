1. How to install git in windows and mac using command line
   - **Windows**: 
     1. Open Command Prompt.
     2. Use the command: `winget install --id Git.Git -e --source winget` or download from [git-scm.com](https://git-scm.com/download/win).
   - **macOS**: 
     1. Open Terminal.
     2. Use the command: `brew install git` (if Homebrew is installed) or download from [git-scm.com](https://git-scm.com/download/mac).

2. What to do if git is not recognized after installation
   - Ensure that the Git installation path is added to your system's PATH environment variable. You can check this by running `git --version` in the command line. If it returns an error, you may need to reinstall Git or manually add the path.

3. What are common errors in macOS with git installation [pwd related]
   - Common errors include:
     - **Permission Denied**: This can occur if you do not have the necessary permissions to access certain directories. Use `sudo` to run commands with elevated privileges.
     - **Command Not Found**: This indicates that Git is not installed or not in your PATH. Ensure Git is installed and the path is correctly set.

4. What is purpose of the .gitconfig file
   - The `.gitconfig` file is used to store configuration settings for Git. This includes user information (like name and email), editor preferences, and other settings that customize Git's behavior. It can be found in your home directory and can be edited directly or through Git commands like `git config --global`.
