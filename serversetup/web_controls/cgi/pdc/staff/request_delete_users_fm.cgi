#!/bin/bash
#Copyright (C) 2009  Paul Sharrad
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
#The Karoshi Team can be contacted at: 
#mpsharrad@karoshi.org.uk
#jharris@karoshi.org.uk
#aball@karoshi.org.uk
#
#Website: http://www.karoshi.org.uk
############################
#Language
############################
LANGCHOICE=englishuk
STYLESHEET=defaultstyle.css
[ -f /opt/karoshi/web_controls/global_prefs ] && source /opt/karoshi/web_controls/global_prefs
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/user/request_delete_users ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/user/request_delete_users
[ -f /opt/karoshi/web_controls/language/$LANGCHOICE/all ] || LANGCHOICE=englishuk
source /opt/karoshi/web_controls/language/$LANGCHOICE/all
############################
#Show page
############################
echo "Content-type: text/html"
echo ""
echo '
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>'$TITLE'</title>
  <link rel="stylesheet" href="/css/'$STYLESHEET'">
<META HTTP-EQUIV="refresh" CONTENT="300; URL=/cgi-bin/blank.cgi">
<script src="/all/stuHover.js" type="text/javascript"></script>
</head>
<body>'
#Generate navigation bar
/opt/karoshi/web_controls/generate_navbar_staff
echo '
<form action="/cgi-bin/staff/request_delete_users.cgi" method="post">
  <div id="actionbox">
<b>'$TITLE'</b> <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG3'</span></a><br><br>
<table class="standard" style="text-align: left;" border="0" cellpadding="2" cellspacing="2"><tbody>
<tr><td>'$FORENAMEMSG'</td><td>'$SURNAMEMSG'</td><td>'$YEARGROUPMSG' <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG1'</span></a></td><td>'$ADNOMSG' <a class="info" href="javascript:void(0)"><img class="images" alt="" src="/images/help/info.png"><span>'$HELPMSG2'</span></a></td></tr>
<tr><td><input tabindex= "3" size="10" name="_FORENAME1_"></td><td><input tabindex= "4" size="15" name="_SURNAME1_"></td><td>'`/opt/karoshi/web_controls/group_dropdown_list | sed "s/GROUP/GROUP1/g"`'</td><td><input tabindex= "6" size="18" name="_ADNO1_"></td></tr>
<tr><td><input tabindex= "7" size="10" name="_FORENAME2_"></td><td><input tabindex= "8" size="15" name="_SURNAME2_"></td><td>'`/opt/karoshi/web_controls/group_dropdown_list | sed "s/GROUP/GROUP2/g"`'</td><td><input tabindex= "9" size="18" name="_ADNO2_"></td></tr>
<tr><td><input tabindex= "10" size="10" name="_FORENAME3_"></td><td><input tabindex= "11" size="15" name="_SURNAME3_"></td><td>'`/opt/karoshi/web_controls/group_dropdown_list | sed "s/GROUP/GROUP3/g"`'</td><td><input tabindex= "13" size="18" name="_ADNO3_"></td></tr>
<tr><td><input tabindex= "14" size="10" name="_FORENAME4_"></td><td><input tabindex= "15" size="15" name="_SURNAME4_"></td><td>'`/opt/karoshi/web_controls/group_dropdown_list | sed "s/GROUP/GROUP4/g"`'</td><td><input tabindex= "21" size="18" name="_ADNO4_"></td></tr>
<tr><td><input tabindex= "18" size="10" name="_FORENAME5_"></td><td><input tabindex= "19" size="15" name="_SURNAME5_"></td><td>'`/opt/karoshi/web_controls/group_dropdown_list | sed "s/GROUP/GROUP5/g"`'</td><td><input tabindex= "21" size="18" name="_ADNO5_"></td></tr>
<tr><td><input tabindex= "22" size="10" name="_FORENAME6_"></td><td><input tabindex= "23" size="15" name="_SURNAME6_"></td><td>'`/opt/karoshi/web_controls/group_dropdown_list | sed "s/GROUP/GROUP6/g"`'</td><td><input tabindex= "25" size="18" name="_ADNO6_"></td></tr>
<tr><td><input tabindex= "26" size="10" name="_FORENAME7_"></td><td><input tabindex= "27" size="15" name="_SURNAME7_"></td><td>'`/opt/karoshi/web_controls/group_dropdown_list | sed "s/GROUP/GROUP7/g"`'</td><td><input tabindex= "29" size="18" name="_ADNO7_"></td></tr>
<tr><td><input tabindex= "30" size="10" name="_FORENAME8_"></td><td><input tabindex= "31" size="15" name="_SURNAME8_"></td><td>'`/opt/karoshi/web_controls/group_dropdown_list | sed "s/GROUP/GROUP8/g"`'</td><td><input tabindex= "33" size="18" name="_ADNO8_"></td></tr>
<tr><td><input tabindex= "34" size="10" name="_FORENAME9_"></td><td><input tabindex= "35" size="15" name="_SURNAME9_"></td><td>'`/opt/karoshi/web_controls/group_dropdown_list | sed "s/GROUP/GROUP9/g"`'</td><td><input tabindex= "37" size="18" name="_ADNO9_"></td></tr>
<tr><td><input tabindex= "38" size="10" name="_FORENAME10_"></td><td><input tabindex= "39" size="15" name="_SURNAME10_"></td><td>'`/opt/karoshi/web_controls/group_dropdown_list | sed "s/GROUP/GROUP10/g"`'</td><td><input tabindex= "41" size="18" name="_ADNO10_"></td></tr>
</tbody></table><br></div>
<div id="submitbox"><input value="'$SUBMITMSG'" type="submit"> <input value="'$RESETMSG'" type="reset"></div>
</form></body></html>
'
exit
