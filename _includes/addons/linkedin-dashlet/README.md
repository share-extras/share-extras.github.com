LinkedIn dashlet for Alfresco Share
===================================

Author: Will Abson

This project defines a custom dashlet that displays recent LinkedIn messages associated with the current user's account.

**The dashlet requires Alfresco 4.0 or greater, plus the [Share OAuth add-on](https://github.com/share-extras/share-oauth), version 2.2 or greater.**

![LinkedIn Dashlet](screenshots/linkedin-dashlet.png)

Installation
------------

The dashlet is packaged as a single JAR file for easy installation into Alfresco Share.

To install the dashlet, simply drop the `linkedin-dashlet-<version>.jar` file into the `tomcat/shared/lib` folder within your Alfresco installation, and restart the application server. You might need to create this folder if it does not already exist.

**The dashlet also requires the [Share OAuth extension](https://github.com/share-extras/share-oauth), version 2.2 or greater -  see _[Installation](https://github.com/share-extras/share-oauth/blob/master/README.md#installation)_ for installation instructions.**

Building from Source
--------------------

An Ant build script is provided to build a JAR file containing the custom files, which can then be installed into the `tomcat/shared/lib` folder of your Alfresco installation.

To build the JAR file, run Ant from the base project directory.

    ant dist-jar

The command should build a JAR file named `linkedin-dashlet-<version>.jar` in the `build/dist`' directory within your project.

To deploy the dashlet files into a local Tomcat instance for testing, you can use the `hotcopy-tomcat-jar` task. You will need to set the `tomcat.home` property in Ant.

    ant -Dtomcat.home=C:/Alfresco/tomcat hotcopy-tomcat-jar
    
Once you have deployed the JAR file you will need to restart Tomcat so that the additional resources are picked up.

Usage
-----

  1. Log in to Alfresco Share and navigate to your user dashboard.
  2. Click the _Customize Dashboard_ button to edit the contents of the dashboard and drag the dashlet into one of the columns from the list of dashlets.