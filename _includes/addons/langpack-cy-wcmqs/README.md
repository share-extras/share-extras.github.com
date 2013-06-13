Alfresco Web Quick Start Welsh Language Pack
============================

Author: Will Abson

This language pack provides a Welsh translation of the Alfresco Web Quick Start modules and the Alfresco Web Editor and Quick Start web applications.

A [Welsh translation of Alfresco Share](https://github.com/share-extras/langpack-cy-wcmqs) is available separarely.

The translation is complete for Alfresco Community 4.0 and should be backwards-compatible with previous versions.

Building from Source
--------------------

An Ant build script is provided to build a JAR file containing the custom files, which can then be installed into your Alfresco installation.

To build the JAR file, run the following command from the base project directory.

    ant dist-jar

The command should build a JAR file named `alfresco-langpack-wcmqs_cy-gb.jar`
in the `build/dist` directory within the project.

Installation
------------

Copy the JAR file into `<TOMCAT_HOME>/shared/lib`. If this directory does not exist then you can create it, but you should also check that the `shared.loader` property defined in `<TOMCAT_HOME>/conf/catalina.properties` includes it, e.g.

    shared.loader=${catalina.home}/shared/classes,${catalina.home}/shared/lib/*.jar

You should update the value if it is empty, or add this value to the bottom of the file if it is not already defined or is commented out.

You will need to restart the Alfresco server before you can use the language pack.

Usage
-----

Alfresco Share will auto-detect the client language based on your 
browser settings. You will need to add 'English (United Kingdom)' as the first entry in 
your preferred languages - in Firefox click _Tools > Options > Content > 
Languages > Choose_ or click _Language settings_ in Chrome's Advanced Settings.