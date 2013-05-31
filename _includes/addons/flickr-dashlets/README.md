Flickr Photos dashlet for Alfresco Share
========================================

Author: Will Abson

This project defines three custom dashlets to display a slideshow display of photostreams sourced from Flickr's public API. The dashlets are able to display public photos from three types of feed.

  * User photos
  * User contacts photos
  * User favourite photos

![Flicks Slideshow Dashlet](screenshots/flickr-slideshow-dashlet.png)

Installation
------------

The dashlets are packaged in a single JAR file for easy installation into Alfresco Share.

To install the dashlets, simply drop the `flickr-dashlets-<version>.jar` file into the `tomcat/shared/lib` folder within your Alfresco installation, and restart the application server. You might need to create this folder if it does not already exist.

Building from Source
--------------------

An Ant build script is provided to build a JAR file containing the custom files, which can then be installed into the `tomcat/shared/lib` folder of your Alfresco installation.

To build the JAR file, run Ant from the base project directory.

    ant dist-jar

The command should build a JAR file named `flickr-dashlets-<version.jar` in the `build/dist` directory within your project, which you can then copy into the `tomcat/shared/lib` folder of your Alfresco installation.

Alternatively, you can use the build script to _hot deploy_ the JAR file directly into a local Tomcat instance for testing. You will need to use the `hotcopy-tomcat-jar task` and set the `tomcat.home`
property in Ant.

    ant -Dtomcat.home=C:/Alfresco/tomcat hotcopy-tomcat-jar
    
After you have deployed the JAR file you will need to restart Tomcat to ensure it picks up the changes.

Usage
-----

  1. Log in to Alfresco Share and navigate to a site where you are a Site Manager OR to your user dashboard
  2. On the dashboard and click the *Customize Dashboard* button to edit the contents of the dashboard. Drag a Flickr dashlet into one of the columns from the list of dashlets to add it.
  3. Click *OK* to save the configuration.
  4. The chosen dashlet should now be shown on your dashboard.