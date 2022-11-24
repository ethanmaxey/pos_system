# Git Workflow
## One Time Setup
1. git clone https://github.com/kundanpaudel/pos_11-21
2. cd pos_11-21
3. git checkout "<YOUR_NAME>"

## Merge Lifecycle
1. Make your changes and test along the way
2. git add -A
3. git commit -m "..." # The commit messages should be verbose describing the purpose of the changes you made
4. git pull origin master
5. TEST and fix anything that is broken - Only push working changes!
6. git push origin "<YOUR_NAME>" # Never push to master directly!
7. Let Ethan know you have changes that are ready to be merged
8. Ethan will test your changes locally.
9. Ethan will merge your branch into `master`.
