# Starting the server on another thread
import threading

import diff
import revert
import server

server_thread = threading.Thread(target=server.run_server)
server_thread.start()

# Running the diff program
diff.start()

# Running the revert program
revert.start()

# Stopping the server and thread
server_thread._stop()