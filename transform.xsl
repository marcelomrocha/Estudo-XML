<?xml version="1.0" encoding="UTF-8" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="xml" encoding="UTF-8" omit-xml-declaration="yes" indent="yes" />


<xsl:template match="interaction">
{
"_id": "<xsl:value-of select="@id" />",
"nombre": "<xsl:value-of select="@name" />",
"data": {
"node": [
  <xsl:apply-templates />
</xsl:template>

<xsl:template match="light">
{
"key": 1629716981648,
"name": "Light_8",
"type": "light",
"color": "lightblue",
"isGroup": false,
"group": "",
"lcolor": "<xsl:value-of select="@color" />",
"state": "<xsl:value-of select="@state" />",
"__gohashid": 1
},
	<xsl:apply-templates />
</xsl:template>

<xsl:template match="voice">
{
"key": 1629715823158,
"name": "Voice_1",
"type": "voice",
"color": "lightblue",
"isGroup": false,
"voice": "pt-BR_IsabelaV3Voice",
"__gohashid": 2
},
	<xsl:apply-templates />
</xsl:template>

<xsl:template match="talk">
{
"key": 1624799131196,
"name": "Talk_1",
"type": "speak",
"color": "lightblue",
"isGroup": false,
"text": "<xsl:value-of select="text()" />",
"__gohashid": 3
},
</xsl:template>

<xsl:template match="wait">
{
"key": 1629715910493,
"name": "Wait_2",
"type": "wait",
"color": "lightblue",
"isGroup": false,
"time": <xsl:value-of select="@duration" />,
"__gohashid": 4
},
	<xsl:apply-templates />
</xsl:template>

<xsl:template match="random">
{
"key": 1629719228119,
"name": "Random_10",
"type": "random",
"color": "lightblue",
"isGroup": false,
"group": "",
"min": <xsl:value-of select="@min" />,
"max": <xsl:value-of select="@max" />,
"__gohashid": 5
},
</xsl:template>

<xsl:template match="links">
],
"link": []
}
}
</xsl:template>
</xsl:stylesheet>