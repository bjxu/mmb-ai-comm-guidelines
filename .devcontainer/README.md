# Dev container

Start Docker, install the VS Code Dev Containers extension, then run
**Dev Containers: Reopen in Container**. Sign in to GitHub Copilot if prompted.

## SSH keys

The container mounts your host's `~/.ssh` folder read-only at `/tmp/host-ssh`.
On each start, it copies the folder into `~/.ssh` and sets `600` permissions on
private keys. The copy lives inside the container, so private keys are present
there. Do not commit keys to the repository.

On Windows, `${localEnv:HOME}` may be unset. In that case, change the mount
source in [devcontainer.json](./devcontainer.json) to `${localEnv:USERPROFILE}/.ssh`
(for example, in a local copy). Rebuild the container after changing it.

The container mounts the repository's `.devcontainer/zscaler.pem` read-only and
installs it into the system CA store on each start. Node.js, Python Requests,
and pip are also configured to trust this certificate. Rebuild the container
after changing the dev container configuration. Only use a CA certificate you
trust, as it can authenticate HTTPS connections.

The container requests **Allow all** as the default approval level for new
Copilot sessions. Check the permissions picker in a new Copilot session and
select **Allow all** if the setting is not applied. Organization policies can
restrict this option; existing sessions retain their own permission level.

Allow all skips ordinary tool confirmations, including for destructive actions.
The repository is mounted read-write from your host, so changes made in the
container affect your local files. The container is not a security boundary
for mounted files, forwarded credentials, or accessible network services.
