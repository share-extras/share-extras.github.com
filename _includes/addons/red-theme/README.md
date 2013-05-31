Red Theme for Alfresco Share
============================

Author: Will Abson

This project provides a custom theme for Alfresco Share using a red colour scheme.

![Red Theme](screenshots/screenshot.png)

Installation
------------

In Share 3.4.b and greater the theme can be easily installed as a JAR file. To install the theme, simply drop the `red-theme-<version>.jar` file into the `tomcat/shared/lib` folder within your Alfresco installation, and restart the application server. You might need to create this folder if it does not already exist.

For all other versions, the custom theme is packaged as an [AMP file](http://wiki.alfresco.com/wiki/AMP_Files) that can be installed on top of Alfresco Share using the [Module Management Tool](http://wiki.alfresco.com/wiki/Module_Management_Tool). This tool is available as a separate download if your installation does not include it.

To install the theme, drop the AMP file into the root of your Alfresco installation and use the MMT executable JAR to install the files into the `share` web application.

    java -jar bin/alfresco-mmt.jar install red-theme-<version>.amp tomcat/webapps/share.war
    rm -rf tomcat/webapps/share

If you are using a Windows-based installation package or Tomcat bundle then you can also use the `apply_amps.bat` script to install the AMP file for you. You will need to create a folder named `amps-share` if this does not already exist in your installation directory, and place the AMP file in there before running the script.

The script will also take care of removing the old exploded web application files.

Building from Source
--------------------


An Ant build script is provided to build a package containing the custom files, which can then be installed into the `share` web application, as documented in the _[Installation](#installation)_ section above.

In Share 3.4.b and greater, you can build the JAR file directly

    ant dist-jar

The command should build a JAR file named `red-theme-<version>.jar` in the `build/dist` directory within your project.

Or, to build the AMP file, run the following command from the base project directory.

    ant dist-amp

The command should build a JAR file named `red-theme-<version>.amp` in the `build/dist` directory within your project.

Usage
-----

### Setting the site theme

  1. Log into Alfresco Share as a site administrator
  2. Click the _Customize Site_ button in the site navigation bar
  3. Select _Red Theme_ from the list of themes and click OK to save
  4. The theme will now be used for all users using that site

### Setting the default theme for users

  1. Log in to Alfresco Share as a repository administrator
  2. Navigate the *Application* section of the Share *Administration Console*
  3. Select _Red Theme_ from the drop-down list and click OK to save your changes
  4. The new theme will now be used for all Alfresco Share users