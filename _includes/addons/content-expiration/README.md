Content Expiration Reports for Alfresco Share
=============================================

Author: Will Abson

This project provides a custom dashlet that lists 'expired' content owned by the current user, plus a full page report implemented as a custom Surf page.

Content is considered to have expired when the value of its `cm:to` date property (part of the out-of-the-box _Effectivity_ aspect) is in the past. Ownership is specified explicitly by the value of the `cm:owner` (part of the out-of-the-box _Ownable_ aspect) property, which should be set the username of the owner.

To allow expiration dates to be set automatically based on a simple policy, a custom aspect named _Validity_ is supplied in a custom model. The aspect specifies a _Validity Period_ property value, which defines how long that content item should be considered valid for before a further review is necessary.

A repository script `apply-expiration.js` is supplied in `config/alfresco/script` to allow a default validity period (3 months) to be set against content items. The script can be run against a single document or against a folder. In the latter case it will recurse through the folder contents and apply the policy to all document below that level.

In addition to setting the validity period (if not already set), the script also sets the content owner to the user who created the content, and sets an initial expiration date by adding the validity period to the last modified time stamp.

You must add `apply-expiration.js` to the _Data Dictionary/Scripts_ space in the repository. You can then run it from the _Run Action_ dialogue in Alfresco Explorer, or using the _Execute Script_ add-on from Share Extras. If you want to apply expiration to all documents added below a specific folder then you can set up a rule to automatically run the script against new documents.

After the action has run the _Validity Period_ and _Owner_ can be changed at any time using the _Edit Metadata_ page for the document. The expiration date cannot be set directly, only indirectly via the validity period.

To allow the expiration date to be extended when the document is reviewed, another repository script `update-expiration.js` is provided. Like `apply-expiration.js` this can be run on-demand from Explorer or via the _Execute Script_ action, but since this will be used more frequently by users you may wish to configure the custom action also supplied (see [Custom Action Installation](#Custom-Action-Installation), below), which will allow users to run the script with a single click.

Alternatively you can also set up a content rule to execute `update-expiration.js` whenever a user updates the content item. This may be preferable to adding custom actions in some circumstances.

A third script `remove-expiration.js` will remove the expiration metadata from a content item that you no longer wish to be managed in this way. You can run this on a document or on a folder to remove the metadata from all documents below that level.

You can also manually remove content expiration metadata from items by using Share's _Manage Aspects_ dialogue, to remove the _Validity_ and _Effectivity_ aspects.

Installation
------------

The dashlet is packaged as a single JAR file for easy installation into Alfresco Share.

An Ant build script is provided to build a JAR file containing the custom files, which can then be installed into the `'tomcat/shared/lib` folder of your Alfresco installation.

To build the JAR file, run Ant from the base project directory.

    ant dist-jar

The command should build a JAR file named `content-expiration-<version>.jar` in the `build/dist` directory within your project.

To deploy the add-on files into a local Tomcat instance for testing, you can use the `hotcopy-tomcat-jar` task. You will need to set the `tomcat.home` property in Ant.

    ant -Dtomcat.home=C:/Alfresco/tomcat hotcopy-tomcat-jar

Once you have deployed the JAR file you will need to restart Tomcat so that the classpath resources in the JAR file are picked up.

Custom Action Installation (Optional)
-------------------------------------

Once the JAR file has been deployed into your application server you can configure the Share application to display the custom 'Update Expiration' action.

Firstly, copy the web script configuration file `WEB-INF/classes/alfresco/site-webscripts/org/alfresco/components/documentlibrary/documentlist.get.config.xml` from the Share webapp into the directory 
`alfresco/web-extension/site-webscripts/org/alfresco/components/documentlibrary` in Tomcat’s `shared/classes` to override it. You should see a section `<actionSet id="document">` which defines all the actions shown for a normal document in the document list view.

To add the action to this list, add the following line just before the `</actionset>` element for that block.

    <action type="action-link" id="onActionUpdateExpiration" permission="edit" label="actions.document.update-expiration" />

To make the action appear for folder items in addition to documents, add the same line into the section `<actionSet id="folder">`.

If you also want the action to show up in the document details view, you need to copy the file `WEB-INF/classes/alfresco/site-webscripts/org/alfresco/components/document-details/document-actions.get.config.xml` into `alfresco/web-extension/site-webscripts/org/alfresco/components/document-details` in `shared/classes`, and add the extra `<action>` definition(s) in the same way.

Lastly, you need to ensure that the client-side JS and CSS assets get pulled into the UI as unfortunately the config files do not allow us to specify these dependencies.

To do this, you must override the file `WEB-INF/classes/alfresco/site-webscripts/org/alfresco/components/documentlibrary/actions-common.get.head.ftl`. Copy this into the directory `alfresco/web-extension/site-webscripts/org/alfresco/components/documentlibrary` in `shared/classes` and add the following lines at the bottom of the file.

    <#-- Update Expiration Action -->
    <@link rel="stylesheet" type="text/css" href="${page.url.context}/res/extras/components/documentlibrary/update-expiration-action.css" />
    <@script type="text/javascript" src="${page.url.context}/res/extras/components/documentlibrary/update-expiration-action.js"></@script>

Once you have made these changes you will need to restart Tomcat so that the configuration and your classpath resources in the JAR file are picked up.

Note: If you want the action to appear in the repository browsing pages or in Web Quick Start or DOD sites, you will also need to update the corresponding `.config.xml` and `.head.ftl` files for those page components.

## Usage

### Using the dashlet

Log in to Alfresco Share and navigate to your user dashboard. Click the _Customize Dashboard_ button to edit the contents of the dashboard and drag the dashlet into one of the columns from the list of dashlets.

### Access the Full Report

You can view the full report for your expired content items by clicking the _Full Report_ link at the top of the dashlet.