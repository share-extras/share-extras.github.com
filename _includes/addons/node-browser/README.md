Node Browser Admin Console component for Alfresco Share
=======================================================

Author: Will Abson

This project defines a Share administration console component to navigate and view information on nodes stored in the repository stores, similar to the Node Browser component in Alfresco Explorer.

![Node Browser Console](screenshots/node-browser-search.png)

The Node Browser is included in core Alfresco Share 4.0 and greater, but this add-on my be used with previous versions.

Installation
------------

The component is packaged as a single JAR file for easy installation into Alfresco Share. However as it includes a custom Java class, it must be installed directly into the webapp directory structure, rather than into `tomcat/shared/lib`.

To install the component, drop the `node-browser-<version>.jar` file into the following two directories within your Alfresco installation, and restart the application server.

  * `tomcat/webapps/alfresco/WEB-INF/lib`
  * `tomcat/webapps/share/WEB-INF/lib`

Building from Source
--------------------

An Ant build script is provided to build a JAR file containing the custom files, which can then be installed into the `tomcat/shared/lib` folder of your Alfresco installation.

To build the JAR file, run the following command from the base project directory.


    ant dist-jar

The command should build a JAR file named `node-browser-<version>.jar` in the `build/dist` directory within your project, which you can then copy into the webapp folders in your Alfresco installation, as in _[Installation](#installation)_, above.

After you have deployed the JAR file you will need to restart Tomcat to ensure it picks up the changes.

Usage
-----

  1. Log in to Alfresco Share and navigate to an Administration page such as Users or Groups
  2. In the left-hand-side navigation, click *Node Browser*
  3. Enter a [search](http://wiki.alfresco.com/wiki/Full_Text_Search_Query_Syntax) to return some results, e.g. `name:test`
  4. Click on a result to start browsing the nodes

Known Issues
------------

  * In version 3.4 The Node Browser does not appear automatically in the _More..._ drop-down menu in the Share header component, however you can [add it there](http://wiki.alfresco.com/wiki/Share_Header) with some basic configuration.