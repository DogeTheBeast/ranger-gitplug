import subprocess
from ranger.api.commands import Command

class git(Command):

    commands = 'init status clone add rm restore commit remote push'.split()


    def execute(self):
        # empty
        if not self.arg(1):
            # Write to a tmp file and open it in editor (Easy solution)
            # Shift to a terminal instance and display commands
            return self.fm.notify("For commands check \"git help\"")

        # help
        if self.arg(1) == "help":
            return self.fm.notify("Not done yet!", bad=True)

        # init
        if self.arg(1) == self.commands[0]:
            output = subprocess.run(["git", "init"], capture_output=True, text=True)
            if output.returncode != 0:
                self.fm.notify("git: " + output.stderr, bad=True)
            else:
                return self.fm.notify("git: " + output.stdout)

        # status
        # Note: This feature is limited by the Ranger API. In an ideal world, we should be able to use whichever editor and it should be a read only file, I would love to use less for this instance
        if self.arg(1) == self.commands[1]:
            output = subprocess.run(["git", "status"], capture_output=True, text=True)

            if output.returncode !=0:
                return self.fm.notify("git: " + output.stderr, bad=True)

            with open('/tmp/gitplug-status', 'w') as out:
                out.write(output.stdout)

            return self.fm.edit_file('/tmp/gitplug-status')

        # clone
        # TODO:
        # TIP!
        #       to clone private repositorues you have to store your data
        #       using: "git config --global credential.helper store" in your
        #       terminals emulator(not ranger! it will not work!) and then
        #       do one pull still from terminals emulator and then you can
        #       clone private repositories from ranger.
        if self.arg(1) == self.commands[2]:
            if not self.arg(2):
                return self.fm.notify("Missing url!", bad=True)

            if self.arg(2):
                subprocess.run(["git", "clone", self.arg(2), "--quiet"])
                return self.fm.notify("Repository successfully cloned!")

        # add
        # TODO: Improvement idea, check if the file at path exists, if not exit with error early
        if self.arg(1) == self.commands[3]:
            if not self.arg(2):
                return self.fm.notify("Missing arguments! Usage :git add <file>", bad=True)

            # Could throw an error if file is not present
            output = subprocess.run(["git", "add", self.arg(2)], capture_output=True, text=True)
            if output.returncode != 0:
                return self.fm.notify("git: " + output.stderr, bad=True)
            return self.fm.notify("git: Successfully added")

        #rm
        # TODO: TODO from add applies here
        if self.arg(1) == self.commands[4]:
            if not self.arg(2):
                return self.fm.notify("Missing arguments! Usage :git rm <file>", bad=True)

            if self.arg(2):
                subprocess.run(["git", "rm", self.arg(2)])
                return self.fm.notify("Successfully removed files from branch!")

        # restore
        if self.arg(1) == self.commands[5]:
            if not self.arg(2):
                return self.fm.notify("Missing arguments! Usage :git restore <file>", bad=True)

            if self.arg(2):
                subprocess.run(["git", "restore", "--staged", self.arg(2), "--quiet"])
                return self.fm.notify("Successfully restored files!")

        # commit
        if self.arg(1) == self.commands[6]:
            if not self.rest(2):
                return self.fm.notify("Missing commit text", bad=True)

            if self.rest(2):
                subprocess.run(["git", "commit", "-m", self.rest(2), "--quiet"])
                return self.fm.notify("Successfully commited!")
        
        # remote
        if self.arg(1) == self.commands[7]:
            if not self.arg(2):
                return self.fm.notify("Missing arguments! Use: git remote add/rm <name> <url>", bad=True)

            if self.arg(2) == "add":
                if not self.arg(3):
                    return self.fm.notify("Missing name and url!", bad=True)

                if self.arg(3):
                    if not self.arg(4):
                        return self.fm.notify("Missing url!", bad=True)

                    if self.arg(4):
                        subprocess.run(["git", "remote", "add", self.arg(3), self.arg(4)])
                        return self.fm.notify("Remote successfully added!")

            if self.arg(2) == "rm":
                if not self.arg(3):
                    return self.fm.notify("Missing name!", bad=True)

                if self.arg(3):
                    subprocess.run(["git", "remote", "rm", self.arg(3)])
                    return self.fm.notify("Remote successfully removed")

        # push
        if self.arg(1) == self.commands[8]:
            if self.arg(2) == "-u" and self.arg(3) and self.arg(4):
                subprocess.run(["git", "push", "--quiet", "-u", self.arg(3), self.arg(4)])
                return self.fm.notify("Repository successfully pushed")

            if not self.arg(2):
                subprocess.run(["git", "push", "--quiet"])
                return self.fm.notify("Repository successfully pushed")
