#!/bin/bash
#Wireless_view_zones
#Copyright (C) 2009 Paul Sharrad

#This file is part of Karoshi Server.
#
#Karoshi Server is free software: you can redistribute it and/or modify
#it under the terms of the GNU Affero General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#Karoshi Server is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU Affero General Public License for more details.
#
#You should have received a copy of the GNU Affero General Public License
#along with Karoshi Server.  If not, see <http://www.gnu.org/licenses/>.

#
#The Karoshi Team can be contacted at: 
#mpsharrad@karoshi.org.uk
#jharris@karoshi.org.uk
#aball@karoshi.org.uk
#
#Website: http://www.karoshi.org.uk

#Language
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/user_prefs/$REMOTE_USER ] && source /opt/karoshi/web_controls/user_prefs/$REMOTE_USER
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/client/wireless_view_zones ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/client/wireless_view_zones
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
############################
#Show page
############################

echo "Content-type: text/html"
echo ""
echo '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>'$TITLE2'</title><link rel="stylesheet" href="/css/'$STYLESHEET'"><script src="/all/stuHover.js" type="text/javascript"></script></head><body>
<body>'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_admin

echo '<div id="actionbox"><b>'$TITLE'</b><br><br>
'
#########################
#Get data input
#########################
TCPIP_ADDR=$REMOTE_ADDR
DATA=`cat | tr -cd 'A-Za-z0-9\._:%\-+'`

#########################
#Assign data to variables
#########################
END_POINT=3

#Assign ZONECHOICE
COUNTER=2
while [ $COUNTER -le $END_POINT ]
do
DATAHEADER=`echo $DATA | cut -s -d'_' -f$COUNTER`
if [ `echo $DATAHEADER'check'` = ZONECHOICEcheck ]
then
let COUNTER=$COUNTER+1
ZONECHOICE=`echo $DATA | cut -s -d'_' -f$COUNTER | tr -cd 'A-Za-z0-9_\-+'`
break
fi
let COUNTER=$COUNTER+1
done

function show_status {
echo '<SCRIPT language="Javascript">'
echo 'alert("'$MESSAGE'")';
echo 'window.location = "/cgi-bin/admin/wireless_view_zones_fm.cgi"'
echo '</script>'
echo "</body></html>"
exit
}
#########################
#Check https access
#########################
if [ https_$HTTPS != https_on ]
then
export MESSAGE=$HTTPS_ERROR
show_status
fi
#########################
#Check user accessing this script
#########################
if [ ! -f /opt/karoshi/web_controls/web_access_admin ] || [ $REMOTE_USER'null' = null ]
then
MESSAGE=$ACCESS_ERROR1
show_status
fi

if [ `grep -c ^$REMOTE_USER: /opt/karoshi/web_controls/web_access_admin` != 1 ]
then
MESSAGE=$ACCESS_ERROR1
show_status
fi
#########################
#Check data
#########################

if [ $ZONECHOICE'null' = null ]
then
MESSAGE=$ERRORMSG1
show_status
fi

if [ `echo $ZONECHOICE | grep -c ^delete` = 1 ]
then
ACTION=delete
else
ACTION=edit
fi
ZONE=`echo $ZONECHOICE | sed 's/^edit//g' | sed 's/^delete//g'`


MD5SUM=`md5sum /var/www/cgi-bin_karoshi/admin/wireless_view_zones.cgi | cut -d' ' -f1`

if [ $ACTION = delete ]
then
echo "$REMOTE_USER:$REMOTE_ADDR:$MD5SUM:$ZONE:" | sudo -H /opt/karoshi/web_controls/exec/wireless_delete_zone
fi

if $ACTION = edit ]
then
source /opt/karoshi/web_controls/language/$LANGCHOICE/client/wireless_view_zones
echo '<input name="_ZONECHOICE_" value="'$ZONECHOICE'" type="hidden"
<table class="standard" style="text-align: left; height: 10px;" border="0" cellpadding="2" cellspacing="2">
    <tbody>
<tr><td style="width: 180px;">'$TCPIPMSG'</td><td><input name="_TCPIP_" maxlength="20" size="20" type="text"></td><td>
<a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$TCPIPHELPMSG1'<br><br>'$TCPIPHELPMSG2'</span></a></td></tr>
<tr><td style="width: 180px;">'$WPAMSG'</td><td><input name="_WPAKEY_" maxlength="63" size="63" type="text"></td><td>
<a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG3'<br><br>'$HELPMSG4'</span></a>
</td></tr></tbody></table>'
fi

if [ `echo $?` = 101 ]
then
MESSAGE=`echo $PROBLEMMSG $LOGMSG`
else
MESSAGE=`echo $WPAKEY '\n\n' $COMPLETEDMSG`
fi
show_status
exit
