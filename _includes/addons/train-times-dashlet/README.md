<?xml version="1.0" encoding="utf-8"?><!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
 "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
  <head>
    <title>204 No Content</title>
  </head>
  <body>
    <h1>Error 204 No Content</h1>
    <p>No Content</p>
    <h3>Guru Meditation:</h3>
    <p>XID: 584277146</p>
    <hr>
    <p>Varnish cache server</p>
  </body>
</html>
HTTP/1.1 200 OK
Server: GitHub.com
Content-Type: text/plain; charset=utf-8
Status: 200 OK
Strict-Transport-Security: max-age=31536000
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: deny
Content-Security-Policy: default-src *; script-src https://github.global.ssl.fastly.net https://ssl.google-analytics.com https://collector-cdn.github.com; style-src 'self' 'unsafe-inline' https://github.global.ssl.fastly.net; object-src https://github.global.ssl.fastly.net
X-GitHub-User: wabson
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 100
Access-Control-Allow-Origin: https://render.github.com
X-Git-Blob-Oid: d39a5e328a6fe3d03996ab4e39a8f3d2320350f2
Content-Disposition: inline
Content-Transfer-Encoding: binary
ETag: "e010beb3695e70728b0ec1498b547054"
X-GitHub-Request-Id: B91F111F:1345:13E8E05:532978DC
Content-Length: 2004
Accept-Ranges: bytes
Date: Wed, 19 Mar 2014 12:00:29 GMT
Via: 1.1 varnish
Age: 3585
Connection: keep-alive
X-Served-By: 50b06cef3698e972f044d7dc2cb41530, cache-fra1221-FRA
X-Cache: MISS
X-Cache-Hits: 0
Vary: Accept-Encoding
Cache-Control: private

Train Times dashlet for Alfresco Share
======================================

Author: Will Abson

This project defines a custom dashlet which displays train status information from the National Rail Enquires web site.

![Train Times Dashlet](screenshots/train-times-dashlet.png)

Installation
------------

The dashlet is packaged as a single JAR file for easy installation into Alfresco Share.

To install the dashlet, simply drop the `train-times-dashlet-<version>.jar` file into the `tomcat/shared/lib` folder within your Alfresco installation, and restart the application server. You might need to create this folder if it does not already exist.

Building from Source
--------------------

An Ant build script is provided to build a JAR file containing the custom files, which can then be installed into the `tomcat/shared/lib` folder of your Alfresco installation.

To build the JAR file, run Ant from the base project directory.

    ant dist-jar

The command should build a JAR file named `train-times-dashlet-<version>.jar` in the `build/dist` directory within your project, which you can then copy into the `tomcat/shared/lib` folder of your Alfresco installation.

Alternatively, you can use the build script to _hot deploy_ the JAR file directly into a local Tomcat instance for testing. You will need to use the `hotcopy-tomcat-jar task` and set the `tomcat.home`
property in Ant.

    ant -Dtomcat.home=C:/Alfresco/tomcat hotcopy-tomcat-jar
    
After you have deployed the JAR file you will need to restart Tomcat to ensure it picks up the changes.

Usage
-----

  1. Log in to Alfresco Share and navigate to a site where you are a Site Manager, OR to your user dashboard
  2. On the dashboard and click the *Customize Dashboard* button to edit the contents of the dashboard. Drag the Train Times dashlet into one of the columns from the list of dashlets to add it.
  3. Click *OK* to save the configuration.
  4. The dashlet should now be shown in your dashboard.