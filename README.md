## Python Brushup

#### The repository contains sample python codes for various usage.

## Find out pip2 version & Update
`which pip2` </br>
`sudo -H pip2 install --upgrade pip`

## Find out pip3 version & Update
`which pip3` </br>
`sudo -H pip3 install --upgrade pip`

## pip Uninstall
`sudo -H pip uninstall pip`

### Install OpenCV
`pip3 install opencv-python`

### Issue with QT

```text
Qt is a free and open-source widget toolkit for creating graphical user interfaces 
It is as cross-platform applications that run on various software and hardware platforms
E.g as Linux, Windows, macOS, Android or embedded systems
with little or no change in the underlying codebase while still being a native application with native capabilities and speed. 
Qt is currently being developed by The Qt Company.
A publicly listed company, and the Qt Project under open-source governance, involving individual developers and organizations working to advance Qt.
Qt is available under both commercial licenses and open source GPL 2.0, GPL 3.0, and LGPL 3.0 licenses.
```

```java
qt.qpa.plugin: Could not find the Qt platform plugin "cocoa" in ""
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.
```

Fix : Downgrade OpenCV version </br>
`pip install opencv-python==4.1.2.30`