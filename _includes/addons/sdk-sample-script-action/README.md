Sample Script Action for Alfresco Share
=======================================

Author: Will Abson

This project defines a common source directory layout, [Eclipse](http://www.eclipse.org/) project configuration and [Ant](http://ant.apache.org/) build script that is used by all the Share Extras add-ons, together with some sample files to help you implement a basic [Document Library action](http://wiki.alfresco.com/wiki/Custom_Document_Library_Action).

The project provides an example Document Library action, which can be easily customised to run a JavaScript file of your choice when run by a user.

Using the Sample Project
------------------------

The sample project is intended to help you build your own Share Document Library action, using standard tools such as Eclipse and Ant.

The action executes a basic [JavaScript](http://wiki.alfresco.com/wiki/JavaScript_API) file when fired by the user. All you need to do is add your own JavaScript file to Data Dictionary/Scripts and customise the action definition to use it.

Creating Your Own Projects
--------------------------

To use the sample project, download the `sample-script-action-<version>.zip` file from the Downloads area, and use this to start a new project using Eclipse's Import wizard (select _General_ > _Existing Projects into Workspace_).

Once you have created your project, it should be named _Sample Script Action_ in Eclipse. You should rename this to something of your choosing and update the corresponding JAR file name specified in `build.properties`.

You should also update the information in `README.txt` and `MAINTAINERS.txt` to give some basic information about your project.

### Create Repository JavaScript

Out of the box the action uses the `backup.js` script supplied by Alfresco, but it is likely you will want to create your own script.

You must create the JavaScript file yourself and place this directly into the Data Dictionary/Scripts space in the repository. This must be done in each repository that you wish to install the action on, so you may want to add the script to your Eclipse project to ensure you keep a central copy.

### Customise the Action

Once you have created your script you are ready to customise this action to use it.

The folder `source/web/extras/components/documentlibrary` contains the client-side assets used by the custom action. You should rename `sample-script-action.css` and `sample-script-action.js` to something that better describes your action. This will ensure that your action can co-exist with any others you create using this method, but it is recommended you stick to lowercase letters and hyphens (-).

You can leave the file `sample-script-action-16.gif` untouched, or you can add your own 16x16 GIF or PNG image into the directory to represent your action. If you add your own image you will need to update the CSS file to reference this, instead of `sample-script-action-16.gif`.

You will then need to edit a few variables near the beginning of the renamed JS file.

  * `JSCRIPT_NAME` should define the name of the script which you added to the repository's Data Dictionary/Scripts space.
    
  * `MSG_BASE` is the prefix used for message bundle labels, which should be set to a unique value for your action. Generally you should use the same value you used when renaming the client-side files.
    
  * `FN_NAME` will be used as the name of the client-side function used to define the action. Again it should be unique, but it should normally start with the prefix `onAction` and be a valid JavaScript function name, e.g. on `onActionMyCustomScript`.

After you have updated the JavaScript file, open the CSS file and replace the `.onActionSampleScript` selector on line 1 with the value you set `FN_NAME` to in the JS file. Ensure you do not delete the leading dot.

Next you will need to define your message bundle labels. Rename the Spring configuration file in `config/org/springframework/extensions/surf` to something unique, and change the bean's `id` attribute within the file.

Inside the `<value>` element, the bean defines the path to a single message bundle using dot notation. You should edit the part following the last dot to a unique value for your action. After you have done this, rename the .properties file in `config/alfresco/messages` to match this value.

Lastly, update the property names inside the .property file, changing
`sample-script` to the value you specified in your `MSG_BASE` definition in the client-side JavaScript.

Now you are ready to install the action. Before you do, make sure you update the `jar.name` property in the `build.properties` file to give your JAR file a unique name.

Building Your Project
---------------------

The Ant build script `build.xml` can be used to help you distribute your customisations for testing or deployment.

  * Use the `build-jar` target to build a JAR file in the `dist` directory, suitable for deploying as a shared library on any Share 3.3+ installation.

  * Use the `hotcopy-tomcat-jar` target to copy the JAR file containing the customisations into a local Tomcat installation on your system. You will need to specify the location of your Tomcat installation by defining the variable `tomcat.home` when you call the script.

  * Use the `hotcopy-tomcat-zip` target to copy all the individual configuration and resource files into a local Tomcat installation on your system for testing. Unlike `hotcopy-tomcat-jar`, this method allows you to reload changes to your files without having to restart the Tomcat server, and so is better suited for development. You will need to specify the location of your Tomcat installation by defining the variable `tomcat.home` when you call the script.

For more information on these targets and the other targets available in `build.xml`, see the inline comments within the [build script](build.xml).

### Examples

    ant build-jar

This will build a JAR file using the default file name specified in `build.properties`, containing the custom files.

    ant -Djar.name=my-custom.jar build-jar

This will build a JAR file named `my-custom.jar`

    ant -Dtomcat.home=C:\Alfresco\tomcat hotcopy-tomcat-zip

This will copy all your custom files into the Tomcat instance installed at `C:\Alfresco\tomcat`. Configuration files will be placed into `shared/classes`, while resources will be copied below `webapps/share`.

Configuring Share
-----------------

Once the JAR file has been deployed into your application server you will need to configure the Share application to display the action.

### Alfresco 4.x

Add the following configuration to your `share-config-custom.xml` file inside the `<alfresco-config>` element

    <config evaluator="string-compare" condition="DocLibActions">
       <actions>
          <action id="document-sample-script" type="javascript" label="actions.document.sample-script">
             <param name="function">onActionSampleScript</param>
          </action>
       </actions>
       <actionGroups>
          <actionGroup id="document-browse">
             <action index="500" id="document-sample-script" />
          </actionGroup>
          <actionGroup id="document-details">
             <action index="500" id="document-sample-script" />
          </actionGroup>
       </actionGroups>
    </config>
    
    <config evaluator="string-compare" condition="DocLibCustom">
      <dependencies>
          <css src="/extras/components/documentlibrary/sample-script-action.css" />
          <js src="/extras/components/documentlibrary/sample-script-action.js" />
       </dependencies>
    </config>

Some modifications will be required to this configuration based on the changes you made in the [Customisation](#Customisation) section above.
 
  * Change `onActionSampleScript` to the value you specified for `FN_NAME`. Set the final part of the value for the `label` attribute to the value you specified in your `MSG_BASE` definition in the client-side JavaScript.
  * You should edit the dependencies paths to that the links point correctly to your client-side assets, if you renamed them.
  * If you have multiple actions then the `id` of each of them must be unique

### Alfresco 3.3/3.4

Firstly, copy the web script configuration file `WEB-INF/classes/alfresco/site-webscripts/org/alfresco/components/documentlibrary/documentlist.get.config.xml` from the Share webapp into the directory `alfresco/web-extension/site-webscripts/org/alfresco/components/documentlibrary` in Tomcat’s `shared/classes` to override it. You should see a section `<actionSet id="document">` which defines all the actions shown for a normal document in the document list view.

To add the action to this list, add the following line just before the `</actionset>` element for that block.

    <action type="action-link" id="onActionSampleScript" permission="edit" label="actions.document.sample-script" />

Change `onActionSampleScript` to the value you specified for `FN_NAME` in the [Customisation](#Customisation) section above. Set the final part of the value for the `label` attribute to the value you specified in your `MSG_BASE` definition in the client-side JavaScript.

To make the action appear for folder items in addition to documents, add the same line into the section `<actionSet id="folder">`.

If you also want the action to show up in the document details view, you need to copy the file `WEB-INF/classes/alfresco/site-webscripts/org/alfresco/components/document-details/document-actions.get.config.xml` into `alfresco/web-extension/site-webscripts/org/alfresco/components/document-details` in `shared/classes`, and add the extra `<action>` definition in the same way.

Lastly, you need to ensure that the client-side JS and CSS assets get pulled into the UI as unfortunately the config files do not allow us to specify these dependencies.

To do this, you must override the file `WEB-INF/classes/alfresco/site-webscripts/org/alfresco/components/documentlibrary/actions-common.get.head.ftl`. Copy this into the directory `alfresco/web-extension/site-webscripts/org/alfresco/components/documentlibrary` in `shared/classes` and add the following lines at the bottom of the file.

    <#-- Custom Script Action -->
    <@link rel="stylesheet" type="text/css" href="${page.url.context}/res/extras/components/documentlibrary/sample-script-action.css" />
    <@script type="text/javascript" src="${page.url.context}/res/extras/components/documentlibrary/sample-script-action.js"></@script>

You should edit the paths above to that the links point correctly to your client-side assets, as you renamed them in the [Customisation](#Customisation) section above.

Once you have made these changes you will need to restart Tomcat so that the configuration and your classpath resources in the JAR file are picked up.

Note: If you want the action to appear in the repository browsing pages or in Web Quick Start or DOD sites, you will also need to update the corresponding `.config.xml` and `.head.ftl` files for those page components.

Usage
-----

  1. Log in to Alfresco Share and navigate to any Document Library where you are a Site Collaborator or a Site Manager.
  2. Locate a document in the document list view and hover over the actions list on the right hand-side of the row. You should see your action in the _More..._ section when you expand this.
  3. If you have configured the action in the document details screen above, then click on the document in the list view to navigate to the Document Details screen. You should see the action in the list on the right hand side of the screen.

Credits
-------

Thanks to Mike Farman for the original suggestion.