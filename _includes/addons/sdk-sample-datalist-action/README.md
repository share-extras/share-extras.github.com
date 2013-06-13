Sample Data List Action for Alfresco Share
=========================================

Author: Will Abson

This project defines a custom action which can be configured into the Data List component of Alfresco Share, for use by site members.

The dashlet has been developed for compatibility with Alfresco 3.3 or greater.

Installation
------------

The dashlet is packaged as a single JAR file for easy installation into Alfresco Share.

To install the dashlet, simply drop the `sample-datalist-action-<version>.jar` file into the `tomcat/shared/lib` folder within your Alfresco installation, and restart the application server. You might need to create this folder if it does not already exist.

Configuration
-------------

Once the JAR file has been deployed into your application server you will need to configure the Share application to display the action.

Firstly, copy the web script configuration file `WEB-INF/classes/alfresco/site-webscripts/org/alfresco/components/data-lists/datagrid.get.config.xml` from the Share webapp into the directory `alfresco/web-extension/site-webscripts/org/alfresco/components/data-lists` in Tomcat's `shared/classes` to override it. You should see a section  `<actionSet>` which defines all the actions shown for a data list item in the list view.

To add the backup action to this list, add the following line just before the 
`</actionset>` element for that block.

    <action type="action-link" id="onActionSample" permission="" label="actions.datalist.sample" />

Then, you need to ensure that the client-side JS and CSS assets get pulled 
into the UI as unfortunately the config files do not allow us to specify these 
dependencies.

To do this, you must override the file `WEB-INF/classes/alfresco/site-webscripts/org/alfresco/components/data-lists/actions-common.get.head.ftl`. Copy this into the directory `alfresco/web-extension/site-webscripts/org/alfresco/components/data-lists` in  `shared/classes` and add the following lines at the bottom of the file.

    <#-- Custom Backup Action -->
    <@link rel="stylesheet" type="text/css" href="${page.url.context}/res/extras/components/data-lists/sample-action.css" />
    <@script type="text/javascript" src="${page.url.context}/res/extras/components/data-lists/sample-action.js"></@script>

Finally, you need to increase the width of the Actions column, which before Alfresco 4.2.b, is hard-coded in the client-side file `components/data-lists/datagrid.js`.

Look for a line beginning with the following comment

    // Add actions as last column

The following statement should look something like the following

    columnDefinitions.push(
        { key: "actions", label: this.msg("label.column.actions"), sortable: false, formatter: this.fnRenderCellActions(), width: 105 }
    );
         
At the end of the object literal assignment, change the `width` value to `105`, or add 25 for each additional action you want to add to the row.

_In Alfresco 4.2.b and greater the width value is now defined as a new property `actionsColumnWidth` in the class `options` object and can be more easily overridden there, or (even better) using an extensibility module._

Then, go back to the top of the file and look for a property `splitActionsAt`, which you should
find within the component's `options`. You can set this to whatever value you need to, so long as it is
larger than the number of actions that you will have in each row (otherwise they will not display!).

Once you have made these changes you will need to restart Tomcat so that the configuration and your classpath resources in the JAR file are picked up.

Building from Source
--------------------

An Ant build script is provided to build a JAR file containing the custom files, which can then be installed into the `tomcat/shared/lib` folder of your Alfresco installation.

To build the JAR file, run Ant from the base project directory.

    ant dist-jar

The command should build a JAR file named `sample-datalist-action-<version>.jar` in the `build/dist` directory within your project.

To deploy the JAR file into a local Tomcat instance for testing, you can use the `hotcopy-tomcat-jar` task. You will need to set the `tomcat.home` property in Ant.

    ant -Dtomcat.home=C:/Alfresco/tomcat hotcopy-tomcat-jar

Once the JAR file has been deployed into your application server you will need to configure the Share application to display the action as in _[Installation](#installation)_, above.

Finally after have made these changes you will need to restart Tomcat so that the configuration and your classpath resources in the JAR file are picked up.

Usage
-----

Log in to Alfresco Share and navigate to the _Data Lists_ page of any site that you have write permission on. You should see a _Backup_ action - complete with UI labels and icon - on the document list page, and the details page if you have configured this.

More information
----------------

http://blogs.alfresco.com/wp/wabson/2010/02/28/share-custom-actions-in-a-jar/
http://wiki.alfresco.com/wiki/Custom_Document_Library_Action