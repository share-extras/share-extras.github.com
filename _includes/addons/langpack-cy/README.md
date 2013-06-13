Alfresco Welsh Language Pack
============================

Author: Will Abson

This language pack provides translation of Alfresco Share as well as all translatable repository
messages.

The translation is complete for Alfresco Community 4.2.c and
should be backwards-compatible with all previous versions.

All translations have been spell-checked using the Welsh dictionary
files for OpenOffice.org and manually checked for grammatical errors. 
As part of the project it has been necessary to standardise the 
translation of many of the terms used in the Alfresco interface, 
which have been documented in the file [glossary.txt](glossary.txt).

Building from Source
--------------------

An Ant build script is provided to build a JAR file containing the
custom files, which can then be installed into your Alfresco installation.

To build the JAR file, run the following command from the base project
directory.

    ant dist-jar

The command should build a JAR file named `alfresco-langpack_cy.jar`
in the `build/dist` directory within the project.

Installation
------------

Copy the JAR file into `<TOMCAT_HOME>/shared/lib`. If this directory does
not exist then you can create it, but you should also check that the `shared.loader`
property defined in `<TOMCAT_HOME>/conf/catalina.properties` includes it, e.g.

    shared.loader=${catalina.home}/shared/classes,${catalina.home}/shared/lib/*.jar

You should update the value if it is empty, or add this value to the bottom of the 
file if it is not already defined or is commented out.

You will need to restart the Alfresco server before you can use the language pack.

Usage
-----

Alfresco Share will auto-detect the client language based on your 
browser settings. You will need to add 'Welsh' as the first entry in 
your preferred languages - in Firefox click _Tools > Options > Content > 
Languages > Choose_ or click _Language settings_ in Chrome's Advanced Settings.

To use the language pack in the Alfresco Explorer web client you will 
need to add the `cy` locale to the list of additional languages 
displayed on the login screen in `web-client-config-custom.xml`.

Note: TinyMCE translations (including Welsh) are available from the
[TinyMCE Language Packs](http://tinymce.moxiecode.com/download_i18n.php) page. You will need to 
install these into the `alfresco` and `share` webapps in order to
use TinyMCE as without a language pack for the current locale
TinyMCE will not work.

 * Web client: `alfresco/scripts/tiny_mce`
 * Share: `share/modules/editors/tiny_mce`

Thanks
------

The following sources have been instrumental in helping to develop 
the translation:

 * [Kywiro](http://www.kyfieithu.co.uk/kywiro/index.php) by Kevin Donnelly - provided searchable translations of all
   the major open source Welsh translations

 * The Welsh Language Board's [National Database of Term](http://www.e-gymraeg.co.uk/bwrdd-yr-iaith/termau/Default.aspx)

 * The BBC [Learn Welsh](http://www.bbc.co.uk/wales/learnwelsh/) dictionary, grammer checker and guides

 * Mark H. Nodine's [searchable lexicon of Welsh words](http://www.cs.cf.ac.uk/fun/welsh/LexiconForms.html)

