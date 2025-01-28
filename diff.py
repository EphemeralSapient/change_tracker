# So this python program stores the diff 

# Decided to use unix command [diff]
import subprocess

# We are running server on localhost:1040 for rapid change 
import requests

# Initial version
base = requests.get('http://localhost:1040/random_words')

# Create a directory to store the history
subprocess.call("rm history -rf", shell=True)
subprocess.call("mkdir history", shell=True)
subprocess.call("touch history/old && touch history/new", shell=True)

# Save the initial file
with open("history/0", "w") as f:
    f.write(base.text)

# List of versions [full snapshots]
versions = [base.text]

def start():
    while len(versions)<10:
        new = requests.get('http://localhost:1040/random_words').text
        
        # No changes occurred?
        if(new == versions[-1]):
            continue
        
        # Saving the new and old version
        with open("history/old", "w") as f:
            f.write(versions[-1])
        with open("history/new", "w") as f:
            f.write(new)

        # Comparing the new version with the previous one and save the diff
        subprocess.call("diff history/old history/new > history/patch_"+ str(len(versions)) + ".txt" , shell=True)

        # Update the versions list
        versions.append(new)
        print("Diff file saved for version ", len(versions)-1)
        print(new,"\n")
    print("Diff files saved in history directory")

if __name__ == "__main__":
    start()