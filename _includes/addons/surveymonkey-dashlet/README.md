SurveyMonkey dashlet for Alfresco Share
=======================================

Author: Will Abson

This project defines a custom dashlet to display a [SurveyMonkey](http://www.surveymonkey.com/) Survey on a site dashboard.

![](screenshots/surveymonkey-dashlet.png)

The add-on should work with Alfresco version 3.3 or greater.

Installation
------------

The dashlet is packaged as a single JAR file for easy installation into Alfresco Share.

To install the dashlet, simply drop the `surveymonkey-dashlet-<version>}.jar` file into the `tomcat/shared/lib` folder within your Alfresco installation, and restart the application server. You might need to create this folder if it does not already exist.

Building from Source
--------------------

An Ant build script is provided to build a JAR file containing the custom files, which can then be installed into the `tomcat/shared/lib` folder of your Alfresco installation.

To build the JAR file, run Ant from the base project directory.

    ant dist-jar

The command should build a JAR file named `surveymonkey-dashlet-<version>.jar` in the `build/dist` directory within your project, which you can then copy into the `tomcat/shared/lib` folder of your Alfresco installation.

Alternatively, you can use the build script to _hot deploy_ the JAR file directly into a local Tomcat instance for testing. You will need to use the `hotcopy-tomcat-jar task` and set the `tomcat.home`
property in Ant.

    ant -Dtomcat.home=C:/Alfresco/tomcat hotcopy-tomcat-jar
    
After you have deployed the JAR file you will need to restart Tomcat to ensure it picks up the changes.

Usage
-----

  1. Log in to Alfresco Share and navigate to a site where you are a Site Manager
  2. On the dashboard and click the *Customize Dashboard* button to edit the contents of the dashboard. Drag the _SurveyMonkey_ dashlet into one of the columns from the list of dashlets to add it.
  3. Click *OK* to save the configuration.
  4. The dashlet should now be shown in your dashboard.
  5. Click *Configure* in the dashlet toolbar to enter the URL of the SurveyMonkey survey you want to be displayed, e.g. `http://www.surveymonkey.com/s/D579FNY`