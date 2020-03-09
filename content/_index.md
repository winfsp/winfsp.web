---
title: WinFsp · Windows File System Proxy
---

WinFsp is system software that provides runtime and development support for custom file systems on Windows computers. In this sense it is similar to FUSE (Filesystem in Userspace), which provides the same functionality on UNIX-like computers.

A file system is the method that a computer uses to organize, store and retrieve files. On Windows the default file system is NTFS and files are typically stored on a "drive". WinFsp allows the creation of custom file systems that go beyond the standard file systems that ship with a Windows computer.

Typically any information or storage may be organized and presented as a file system via WinFsp, with the benefit being that the information can be accessed via the standand Windows file API's by any Windows application.

## Benefits

<!-- Icon attribution:
  - ©2015 - 2020 IcoFont (https://icofont.com) - CC BY 4.0
    - correctness.svg
    - easeofuse.svg
    - licensing.svg
    - maturity.svg
    - opensource.svg (modified)
    - performance.svg
    - stability.svg
  - Unknown but possibly Silvano Cirasa, CH (https://thenounproject.com/cirasa.silvano/) - CC BY 3.0
    - trust.svg
-->

<br/>
{{% media-object src="trust.svg" float="left" col=2 imgcls="no-filter" %}}
**Trust**

Trusted by some of the largest software companies, cloud services companies and major financial institutions in the world.
{{% /media-object %}}
<br/>
{{% media-object src="maturity.svg" float="right" col=2 imgcls="no-filter" %}}
**Maturity**

WinFsp is mature software that is in use in millions of installations. WinFsp has been deployed at all scales from government to enterprise to individual.
{{% /media-object %}}
<br/>
{{% media-object src="stability.svg" float="left" col=2 imgcls="no-filter" %}}
**Stability**

WinFsp is stable software. There are no known crashes and it does not suffer from resource leaks or similar problems.
{{% /media-object %}}
<br/>
{{% media-object src="correctness.svg" float="right" col=2 imgcls="no-filter" %}}
**Correctness**

WinFsp strives for correct file system semantics and compatibility with the NTFS file system.
{{% /media-object %}}
<br/>
{{% media-object src="performance.svg" float="left" col=2 imgcls="no-filter" %}}
**Performance**

WinFsp outperforms its competition often by an order of magnitude. In many scenarios it performs as well as NTFS.
{{% /media-object %}}
<br/>
{{% media-object src="easeofuse.svg" float="right" col=2 imgcls="no-filter" %}}
**Ease of use**

WinFsp has an easy to use but comprehensive API. It provides native Windows, FUSE and Cygwin API's for C, C++ and .NET out of the box.
{{% /media-object %}}
<br/>
{{% media-object src="opensource.svg" float="left" col=2 imgcls="no-filter" %}}
**Open Source**

WinFsp is open source with all community and transparency benefits that this entails.
{{% /media-object %}}
<br/>
{{% media-object src="licensing.svg" float="right" col=2 imgcls="no-filter" %}}
**Flexible licensing**

WinFsp is available under the GPLv3 license with a special exception for Free/Libre and Open Source Software. A commercial license is also available.
{{% /media-object %}}
