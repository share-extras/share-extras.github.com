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

Repository API
--------------

A small set of web scripts are provided in the repository component to allow the connector to get and set OAuth tokens as needed.

It should not normally be necessary to call these APIs directly, but in the event of tokens becoming corrupted or to force a re-authorization from the provider, a `DELETE` script allows them to be removed. This can be invoked using Curl, e.g.

    curl http://localhost:8080/alfresco/s/extras/oauth2/token/<token-name> -u admin:admin -X DELETE

Debugging
---------

You can use the following log4j settings to capture information on the live requests which are being proxied by the connector.

    log4j.logger.org.sharextras.webscripts.OAuth2Return=DEBUG
    log4j.logger.org.sharextras.webscripts.connector=DEBUG
    log4j.logger.org.apache.commons.httpclient=DEBUG
    log4j.logger.httpclient.wire=DEBUG