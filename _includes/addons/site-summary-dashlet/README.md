Doucment List dashlet for Alfresco Share
======================================

Author: Will Abson

This project provides a custom dashlet that lists the contents of a chosen folder on a dashboard.

Installation
------------

The dashlet is packaged as a single JAR file for easy installation into Alfresco Share.

To install the dashlet, simply drop the `document-list-dashlet-<version>.jar` file into the `tomcat/shared/lib` folder within your Alfresco installation, and restart the application server. You might need to create this folder if it does not already exist.

Building from Source
--------------------

An Ant build script is provided to build a JAR file containing the custom files, which can then be installed into the `tomcat/shared/lib` folder of your Alfresco installation.

To build the JAR file, run Ant from the base project directory.

    ant dist-jar

The command should build a JAR file named `document-list-dashlet-<version>.jar` in the `build/dist` directory within your project.

To deploy the dashlet files into a local Tomcat instance for testing, you can use the `hotcopy-tomcat-jar` task. You will need to set the `tomcat.home` property in Ant.

    ant -Dtomcat.home=C:/Alfresco/tomcat hotcopy-tomcat-jar
    
Once you have deployed the JAR file you will need to restart Tomcat so that the resources are picked up.

Usage
-----

1. Log in to Alfresco Share and navigate to a site or user dashboard.
2. Click the _Customize Dashboard_ button to edit the contents of the dashboard and drag the dashlet into one of the columns from the list of dashlets.