# RoHunter

<hr>

## 1. Installation

> ### SearchBlox (chrome extension)
>
> Install the extension from the Chrome Web Store: <https://chrome.google.com/webstore/detail/searchblox/pfnpibkjgkpifagdbjkckikghnhhmacp>
>
> ### Python
>
>Ensure you have Python 3.7+ installed. Go to <https://www.python.org/downloads/> and follow the download instructions for your OS.
>
>### Clone the repository
>
>Clone the repository to your local machine by running the terminal command:
>
>```bash
>git clone https://github.com/leekycauldron/RoHunter.git
>```
>
>Go into the directory of the project by running the terminal command:
>
>```bash
>cd RoHunter
>```
>
>### Packages
>
>Install the required packages by running the following command in the root directory of the project:
>
>```bash
>pip install -r requirements.txt
>```
>
>### ChromeDriver
>
>Download the ChromeDriver for your OS from <https://chromedriver.chromium.org/downloads> and place it in the root directory of the project.
>
>To check your Chrome version, go to chrome://version in your browser.
>
>![Chrome Version](/img/chrome-version.png)

## 2. Setup
>
>### settings.json
> 
> Edit this in a text editor.
> 
>| Key | Value |
>| --- | --- |
>| user | The target user's Roblox username |
>| profile-link | The target user's Roblox profile link |
>| delay | The delay between each check (in seconds) |
>| chrome -> data-dir | The path to the Chrome user data directory  (see below if you don't know how)|
>| chrome -> profile | The name of the Chrome profile to use (with SearchBlox >installed) |
>| links | A list of game links to check for the target user |
>
>### Chrome User Data Directory
>
> 1. Open Chrome and go to chrome://version
> 2. Copy the path next to "Profile Path" (do not include the words after the last slash at the end e.g. "Default") and use that as `data-dir` in settings.json. Highlighted in red in the image below.
> 3. Use the name of the profile you want to use as `profile` in settings.json. (the final folder in the profile path e.g. "Default"). Highlighted in orange in the image below.
> ![Chrome User Data Directory](/img/chrome-profile.png)
>
> **NOTE:** When entering the path in settings.json, use **double backslashes** (\\\\) instead of single backslashes (\\). This is because backslashes are used to escape characters in JSON, so you need to escape the backslashes themselves. (e.g. C:\\\\Users\\\\User\\\\AppData\\\\Local\\\\Google\\\\Chrome\\\\User Data\\\\Default)

## 3. Usage

>To run the program simply run the following command. The program will open a chrome window, it does not have to be in focus to run. At the start it will keep checking the status of the target, and once the target is online and in game, it will check the list of games specified in settings.json. Once the target is found, the program will end and will print the game link.
>
>```bash
>python main.py
>```
