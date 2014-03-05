OAuth Support for Alfresco Share
================================

Author: Will Abson

This add-on provides custom Spring Surf connectors and client-side helper class, allowing easy OAuth-based access to external resources. It is a prerequisite for the Twitter, Yammer, LinkedIn and GitHub dashlets provided by Share Extras, and the Chatter Dashlet built by Alfresco's Integrations team.

Building from Source
--------------------

An Maven POM is provided to build the extension, which can then be installed into your Alfresco installation.

To build the project, run Maven from the base project directory.

    mvn clean package

This will give you two JAR files which you can install as follows.

Installation
------------

The extension is packaged as a two JAR files, one for the repository and one for Share.

To install the component, copy the two files into your Alfresco installation, and restart the application server.

  * Copy `share-oauth/target/share-oauth.jar` into `tomcat/webapps/share/WEB-INF/lib`
  * Copy `share-oauth-repo/target/share-oauth-repo.jar` into `tomcat/webapps/alfresco/WEB-INF/lib`

Debugging
---------

You can use the following log4j settings to capture information on the live requests which are being proxied by the connector.

    log4j.logger.org.sharextras.webscripts.OAuth2Return=DEBUG
    log4j.logger.org.sharextras.webscripts.connector=DEBUG
    log4j.logger.org.apache.commons.httpclient=DEBUG
    log4j.logger.httpclient.wire=DEBUG