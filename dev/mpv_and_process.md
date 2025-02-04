1. [X] Open a file using a FileDialog (explorer window):

    1. [ ] Open project file
    2. [ ] Open source file
2. [X] Open a Filter Dialoge

    1. [X] Original file is copied from and untouched
    2. [X] New project data is stored in memory (original text, translated text) in arry form called "project_data"
    3. [ ] Inherit current_project_path from the the project file we opened. If it's new, there is no path.
    4. [ ] ?// Maybe ask the user if they want to move the source text file to a dedicated folder? - I think yes if I were to implement cloud saving option
3. [ ] FIlter texts using regex, but still retain the original whitespaces and new lines

    1. [ ] Check Decision pending in `main_window.py`
    2. [ ] Account for dialogue strings that span multiple lines. Maybe look into making filter check for `"^` start and `"` end to account for all of the string.
4. [X] Once filtering is finished, populate them on to the table
5. [X] Give user option to save it as project file

    1. [X] Create new project file
    2. [X] Overwrite the project file it was opened from
6. [ ] Give user an option to export

    1. [ ] Create new exported file (txt, JSON; depending on the original source file format)
    2. [ ] Create .csv file of table comparison between original text v. translated text.
7. [ ] BIG STRETCH: Give user option to save their work on cloud

    1. [ ] Learn how to set up dockers  start here: https://www.reddit.com/r/webdev/comments/9oaq0l/im_a_complete_newbie_and_trying_to_set_up_a/
    2. [ ] Set up: db to store the project files
    3. [ ] Set up: O Auth for user specific encryption
    4. [ ] Set up: REST API (front and back)
