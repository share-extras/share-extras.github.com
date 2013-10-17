GitHub Dashlets
===============

Display information from and interact with GitHub directly from Alfresco Share.

![GitHub Notifications Dashlet](screenshots/notifications-dashlet.png)

Pre-requisites
--------------

* Alfresco 4.2.d or later
* Latest [Share-OAuth](https://github.com/share-extras/share-oauth) code built from `master` branch

Building and Installing
-----------------------

Use Maven to build the JAR file, which you can then install into your local Tomcat instance

    mvn clean package && \
      cp target/github-dashlets-1.0-SNAPSHOT.jar <TOMCAT_HOME>/webapps/share/WEB-INF/lib
