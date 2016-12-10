git add .
if ! git diff-index --quiet HEAD --; then
    printf "Please write the git commit message.\n"
    sleep 2
    printf "#Git Files Being Committed:\n" > gitmsg
    for i in $(git diff --name-only); do
        printf "#\t%s\n" "$i"
    done
    nano gitmsg
    git commit -m gitmsg
    git pull && git push
    printf "Finished commiting and merging of repo.\n"
else
    printf "There's nothing to commit, so make some changes to commitable files or make sure they're not being ignored!\n"
    printf "." && sleep 0.5 && printf "." && sleep 0.5 && printf ".\n" && sleep 0.5 
    printf "But, even if there's nothing to commit, we're going to still attempt a merge!\n"
    if git merge; then
        printf "Finished merging of repo.\n"
    else
        printf "Merge errored.\n"
    fi
fi
