Execute Script Document Library Action for Alfresco Share
=========================================================

Author: Will Abson

This add-on project for Alfresco Share defines a [custom Document Library action](http://wiki.alfresco.com/wiki/Custom_Document_Library_Action) allowing users to select a 
[JavaScript](http://wiki.alfresco.com/wiki/JavaScript_API) file from the Data Dictionary to run against a file, which can be configured into the Document Library component of Alfresco Share.

![Execute Script Action](screenshots/execute-script-action.png)

The custom action has been developed to install on top of an existing Alfresco 3.3 or greater installation.

Installation
------------

The dashlet is packaged as a JAR file for easy installation into Alfresco Share, although some additional steps are required after installing the JAR file to configure the action into the Document Library.

To install the action, drop the `execute-script-action-<version>.jar` file into the `tomcat/shared/lib` folder within your Alfresco installation. You might need to create this folder if it does not already exist.

Once the JAR file has been deployed into your application server you will need to configure the Share application to display the action.

### Share 4.x

You can enable the actions on the details and list pages for documents and folders by adding the following configuration to your `share-config-custom.xml`.

    <!-- Custom Execute Script Action -->
    <config evaluator="string-compare" condition="DocLibActions">
       <actionGroups>
          <actionGroup id="folder-browse">
             <action index="980" id="org_sharextras_execute-script" />
          </actionGroup>
          <actionGroup id="folder-details">
             <action index="980" id="org_sharextras_execute-script" />
          </actionGroup>
          <actionGroup id="document-browse">
             <action index="980" id="org_sharextras_execute-script" />
          </actionGroup>
          <actionGroup id="document-details">
             <action index="980" id="org_sharextras_execute-script" />
          </actionGroup>
       </actionGroups>
    </config>

If you only wish to show the action on some of the pages, then you can simply remove the other items.

### Share 3.3/3.4

Firstly, copy the web script configuration file 
`WEB-INF/classes/alfresco/site-webscripts/org/alfresco/components/documentlibrary/documentlist.get.config.xml` 
from the Share webapp into the directory 
`alfresco/web-extension/site-webscripts/org/alfresco/components/documentlibrary` in Tomcat’s `shared/classes` to override it. You should see a section 
`<actionSet id="document">` which defines all the actions shown for a normal document in the document list view.

To add the action to this list, add the following line just before the `</actionset>` element for that block.

    <action type="action-link" id="onActionExecuteScript" permission="edit" label="actions.document.execute-script" />

If you also want the action to show up in the document details view, you need to copy the file `WEB-INF/classes/alfresco/site-webscripts/org/alfresco/components/document-details/document-actions.get.config.xml`
into `alfresco/web-extension/site-webscripts/org/alfresco/components/document-details` in `shared/classes`, and add the extra `<action>` definition in the same way.

Lastly, you need to ensure that the client-side JS and CSS assets get pulled into the UI as unfortunately the config files do not allow us to specify these dependencies.

To do this, you must override the file 
`WEB-INF/classes/alfresco/site-webscripts/org/alfresco/components/documentlibrary/actions-common.get.head.ftl`. Copy this into the directory `alfresco/web-extension/site-webscripts/org/alfresco/components/documentlibrary` in `shared/classes` and add the following lines at the bottom of the file.

    <#-- Custom Execute Script Action -->
    <@link rel="stylesheet" type="text/css" href="${page.url.context}/res/extras/components/documentlibrary/execute-script-action.css" />
    <@script type="text/javascript" src="${page.url.context}/res/extras/components/documentlibrary/execute-script-action.js"></@script>

Once you have made these changes you will need to restart Tomcat so that the configuration and your classpath resources in the JAR file are picked up.

Note: If you want the action to appear in the repository browsing pages or in Web Quick Start or Records Management sites, you will also need to update the corresponding `.config.xml` and `.head.ftl` files for those page components.

Building from Source
--------------------

An Ant build script is provided to build a JAR file containing the custom files, which can then be installed into the `tomcat/shared/lib` folder of your Alfresco installation.

To build the JAR file, run Ant from the base project directory.

    ant dist-jar

The command should build a JAR file named `execute-script-action-<version>.jar` in the `build/dist` directory within your project, which you can then copy into the `tomcat/shared/lib` folder of your Alfresco installation.

Alternatively, you can use the build script to _hot deploy_ the JAR file directly into a local Tomcat instance for testing. You will need to use the `hotcopy-tomcat-jar task` and set the `tomcat.home` property in Ant.

    ant -Dtomcat.home=C:/Alfresco/tomcat hotcopy-tomcat-jar

After you have deployed the JAR file you will need to restart Tomcat to ensure it picks up the changes.

See _[Installation](#installation)_, above for the additional steps, which are required after installing the JAR file to configure the action into the Document Library.

Usage
-----

  1. Log in to Alfresco Share and navigate to any Document Library where you are a Site Collaborator or a Site Manager.
  2. Locate a document in the document list view and hover over the actions list on the right hand-side of the row. You should see your action labelled _Execute Script_ in the _More..._ section when you expand this.
  3. If you have configured the action in the document details screen above, then click on the document in the list view to navigate to the Document Details screen. You should see the _Execute Script_ action in the Actions list on the right hand side of the screen.
  4. A dialog will appear with a list of scripts installed in the Data Dictionary. Select one to run, then click OK to execute it.
  5. You can add more scripts by placing them in the *Data Dictionary/Scripts* folder in the repository.