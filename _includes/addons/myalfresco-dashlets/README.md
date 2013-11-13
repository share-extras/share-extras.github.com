MyAlfresco Dashlets
===============

Interact with the [MyAlfresco](https://my.alfresco.com/) service from your on-premise install. Currently provides a single dashlet called _MyAlfresco Sites_, which shows the list of sites that you have access to in MyAlfresco.

Pre-requisites
--------------

* Alfresco 4.2.d or later
* Latest [Share-OAuth](https://github.com/share-extras/share-oauth) code built from `master` branch

Building and Installing
-----------------------

Use Maven to build the JAR file, which you can then install into the Tomcat instance where you have the Share webapp deployed

    mvn clean package && \
      cp target/myalfresco-dashlets-1.0-SNAPSHOT.jar <TOMCAT_HOME>/webapps/share/WEB-INF/lib

There is no need to install any repository-side component, but as mentioned in _Pre-requisites_ above, you must have already installed Share OAuth as detailed in that project.

Configuring
-----------

Before using the dashlet you should register a new application of your own on the Alfresco [developer portal](https://developer.alfresco.com/) and then [add some configuration](http://docs.alfresco.com/4.2/topic/com.alfresco.enterprise.doc/tasks/share-customizing-custom-config-file.html) to your `share-config-custom.xml` to override the endpoint used by the dashlets, e.g.

```
    <config evaluator="string-compare" condition="Remote">
        <remote>
            <endpoint>
                <id>myalfresco-api</id>
                <name>Custom MyAlfresco Public API</name>
                <connector-id>myalfresco</connector-id>
                <endpoint-url>https://api.alfresco.com/alfresco.com/public/alfresco/versions/1</endpoint-url>
                <client-id>myclientid</client-id>
                <client-secret>myclientsecret</client-secret>
                <access-token-url>https://api.alfresco.com/auth/oauth/versions/2/token</access-token-url>
            </endpoint>
        </remote>
    </config>
```

Your config should contain the correct details for the app you registered and your MyAlfresco network (tenant ID)

 * You will need to insert the correct values that correspond to your newly-created application in the `client-id` and `client-secret` parameters
 * If your MyAlfresco network is not `alfresco.com` then you will need to update the first segment of the URL path in `endpoint-url`, e.g. if your e-mail address is `bob@example.com` then your Network ID is `example.com` and the value should be set to `https://api.alfresco.com/example.com/public/alfresco/versions/1`
 * The `name` field can be anything of your choosing, whatever makes sense to you
