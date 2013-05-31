OAuth Support for Alfresco Share
================================

Author: Will Abson

This add-on provides custom Spring Surf connectors and client-side helper class, allowing easy OAuth-based access to external resources. It is a prerequisite for the Twitter, Yammer and LinkedIn dashlets provided by Share Extras.

Installation
------------

The extension is packaged as a single JAR file for easy installation into Alfresco Share.

To install the component, drop the `share-oauth-<version>.jar` file into the following two directories within your Alfresco installation, and restart the application server.

  * `tomcat/webapps/alfresco/WEB-INF/lib`
  * `tomcat/webapps/share/WEB-INF/lib`
  
Building from Source
--------------------

An Maven POM is provided to build a JAR file containing the custom files, which can then be installed into your Alfresco installation.

To build the JAR file, run Maven from the base project directory.

    mvn clean package

The command should build a JAR file named `share-oauth-<version>.jar` in the `target` directory within your project, which you install by copying it into the `WEB-INF/lib` folder of the `alfresco` and `share` webapps.

Once you have run this you will need to restart Tomcat so that the resources in the JAR file are picked up.
