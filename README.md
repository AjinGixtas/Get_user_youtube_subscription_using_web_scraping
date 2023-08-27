# User_subscriber_using_web_scraping
 A simple python program to get an user on Youtube their list of channel and it's link
 How to use the program:
  *Step 1: Download the repository.
  *Step 2: Go to the user's youtube's page.
  *Step 3: Navigate to the user's subscribed channel page. The link should look like this: https://www.youtube.com/{USER_DISPLAY_NAME}/channels.
  *Step 4: Right clicking on an empty place on the page and click on inspect.
  *Step 5: The developer console of your browser should appear now. In the "Inspector", look for a the string "<body>".
   (NOTE: Due to Youtube's website constantly changing, the string might have some stuff in between "y" and ">" such as dir="ltr", rounded-container="", modern-dialog="", etc...).
  *Step 6: Right click on that line, select "Copy" and then select "Inner HTML".
   (NOTE: This is only work on Firefox, if you are on a different browser, this step might be different).
  *Step 7: Now that you have the "Inner HTML", paste it in the "input.txt" file in the repository.
  *Step 8: Run the python script with "python main.py".
  *Step 9: A text file called "result.txt" should appear in the same folder "main.py" is, inside is the channel name and link to said channel of the user.
  *Step 10: You did it :D
  NOTE: Due to Youtube's website everchanging design, the code WILL NOT work after a while without me keep the repository up to date. If you want to help update/optimized the code for me, feel free to do a pull requests!
