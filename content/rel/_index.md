---
title: "Download"
---

WinFsp is released in the form of an MSI installer that includes a signed driver and all files necessary to run and develop user mode file systems on Windows. The installer supports Windows native, FUSE, .NET and Cygwin file systems out of the box. Download the latest version here.

<center class="my-5">
<a class="btn btn-primary" style="width:240px;" href="{{< github-latest-asset `billziss-gh/winfsp` `.msi` >}}" role="button">Download WinFsp Installer</a><br/>
<a class="text-small" href="https://github.com/billziss-gh/winfsp">Repository</a> &middot; <a class="text-small" href="{{< github-latest-blob `billziss-gh/winfsp` `/Changelog.asciidoc` >}}">Changelog</a><br/>
<br/>
<br/>
<b>Additional Downloads</b><br/>
<span class="text-small">WinFsp installation required</span><br/>
<br/>
<a class="btn btn-outline mb-1" style="width:240px;" href="{{< github-latest-asset `billziss-gh/sshfs-win` `-x64.msi` >}}" role="button">SSHFS-Win (x64)</a><br/>
<a class="btn btn-outline" style="width:240px;" href="{{< github-latest-asset `billziss-gh/sshfs-win` `-x86.msi` >}}" role="button">SSHFS-Win (x86)</a><br/>
<a class="text-small" href="https://github.com/billziss-gh/sshfs-win">Repository</a><br/>
<br/>
<a class="btn btn-outline" style="width:240px;" href="{{< github-latest-asset `billziss-gh/nfs-win` `.msi` >}}" role="button">NFS-Win (x86)</a><br/>
<a class="text-small" href="https://github.com/billziss-gh/nfs-win">Repository</a>
</center>

## Quick Start Guide

{{% media-object src="install.png" float="left" col=5 %}}

- Download and run the WinFsp installer.
- In the installer select the option to install the developer files. These include the MEMFS sample file system, but also header and library files that let you develop your own user-mode file system.
- You should not need to reboot, unless WinFsp was already running on your system.

{{% /media-object %}}

## Launch WinFsp from the Windows Explorer

{{% media-object src="explorer.png" float="right" col=5 %}}

- Open Windows Explorer
- Select "This PC". Right-click and select "Map network drive..."
- Map a drive to `\\memfs64\share`. (Assuming a 64-bit machine. Try `\\memfs32\share` if you have a 32-bit machine.)
- After a few seconds a new Explorer window will open up for your new drive.
- The file system behind this drive is a case-insensitive in-memory file system (MEMFS).
- When you are done, you can simply right click on the drive from Windows Explorer and select “Disconnect”.

{{% /media-object %}}

## Launch WinFsp from the Command Prompt

{{% media-object src="command.png" float="left" col=5 %}}

- Start a non-admin Command Prompt.
- Navigate to the folder where you installed WinFsp: `cd C:\Program Files (x86)\WinFsp\bin`
- Execute the command: `memfs-x64 -u \memfs64\share2 -m *`. (Assuming a 64-bit machine. Try `memfs-x86 -u \memfs32\share2 -m *` if you have a 32-bit machine.)
- Open a second non-admin Command Prompt and navigate to the new drive.
- When you are done, you can just press Ctrl-C to kill the MEMFS process from the first command prompt.

{{% /media-object %}}

## For Cygwin users

{{% media-object src="cygwin.png" float="right" col=5 %}}

The installer includes a FUSE package that can be installed on 32-bit or 64-bit Cygwin. This allows software such as SSHFS and FUSEPY to be built and run on Cygwin with minimal changes.

To install the FUSE package to Cygwin perform the following steps:

```
$ cd opt/cygfuse/       <1>
$ sh ./install.sh       <2>
```

1. From a Cygwin command prompt change to the subdirectory `opt/cygfuse` under the WinFsp installation directory.
2. Execute the command `sh ./install.sh` which will install the necessary FUSE files. This includes FUSE runtime and development files.

To uninstall the FUSE package to Cygwin perform the following steps:

```
$ cd opt/cygfuse/       <1>
$ sh ./uninstall.sh     <2>
```

1. From a Cygwin command prompt change to the subdirectory `opt/cygfuse` under the WinFsp installation directory.
2. Execute the command `sh ./uninstall.sh` which will uninstall all previously installed FUSE files.

{{% /media-object %}}
