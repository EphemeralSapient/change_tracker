# Why?

The interviewer asked me where if there's HTML page and client want to track all changes
on it; also store the change efficiently along with what data structure can be used.

Naturally, as a fresher I said it would involve storing lines that have been modified and
periodically or when partial snapshot changes exceeds entire snapshot, convert it to 
full snapshot.

Then I made a mistake where I visualized the version storing part on "Double linked list"
and it seems interviewer wasn't happy about it. Well, here I am, somewhat regretful and
doing PoC to learn so that I don't do the same mistake.

# So, what is this?

I used python along with unix commands [`diff`,`patch`] by using `subprocess.call(... , shell = True)`

Flask is used to run local server on port 1040 where on endpoint `/random_names`, it changes
the list and returns the new version of it.

Of course, this does not replication one-to-one of actual HTML page or some website.
This is an PoC and I achieved what I wanted in simpler means either way.

# Now, what?

Run the `main.py` and observe the changes, learn stuff I guess?

Either way, I have to dig deeper into how `diff` actually works and internal stuff; So yeah,
this repo is literally simple script and not much technically in-depth.

I hope whomever reading this may learn something useful and on the time of interview could
solve if similar question is asked.

Have a nice day.# change_tracker
