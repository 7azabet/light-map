U
    {�]_�  �                '   @   s�  d dl Z d dlZd dlZd dlmZ dZdZdZdZdZ	dZ
dZd	Zd
d� Zdd� Zdd� Zdd� ZddddgZddddddddddd d!d"d#d$d%d&d'd(d)d*d+d,d-d.gZd/d0d1d2d3d4d5d6d7d8d9d:d6d;d5d;d<d=d>d?d@dAdBdCdDdEdFdGdHdIdJdKdLdMdNdOdPdQdRg'ZedS� e�  e�  e�  eedT � dZedUe �ZedVk�rnedW� eD ]Ze�dX� eee � �qDedS� �q"edYk�r e�  eedZ e
 �ZedSk�r�ed[� e�  eeed\ e
 ��ZedSk�r�ed[� e�  eeed]�D ](ZedS� e�dX� ed^e� d_�� �q�eed` � edS� �q"edak�r�eedb e
 �Zedck�r~eedd e � e�de� e � d� e � df� e � dg� n*edhk�r�eedi � needj � e�  n�edkk�r�ee
dl � e�dX� eD ]Z!e�dX� eee! � �q�n�edmk�r>ee
dl � e�dX� eD ]Z"e�dX� eee" � �qeedn � nRedok�r�e�dX� dpZ#e#D ]Z$e�dq� ee$d_dr� �qZedS� e�  neds� �q"dS )t�    N)�searchz[1;30mz[1;31mz[1;32mz[1;33mz[1;35mz[1;36mz[1;37mc                   C   s   t �d� d S )N�clear��os�system� r   r   �Name/lightmap.pyr      s    r   c                  C   s�   t �d� t �d� td� t�  ttd � ttd t �} ttd t �}d}d}| |kr�||kr�t�	d	� ttd
 � t�	d� n&t�	d� ttd � t�	d� t
�  d S )Nznohup pip3 install google &z#nohup pip3 install beautifulsoup4 &� a  

dP                   oo          
88                               
88 .d8888b. .d8888b. dP 88d888b. 
88 88'  `88 88'  `88 88 88'  `88 
88 88.  .88 88.  .88 88 88    88 
dP `88888P' `8888P88 dP dP    dP 
                 .88             
             d8888P              

         z	USERNAME:z	PASSWORD:Z7azabetZ	Palestineg      �?z[+] Done Successfully :) �   z[!] NOT FOUNDg�������?)r   r   �printr   �G�input�R�C�time�sleep�exit)ZUSERNAMEZPASSWORD�userZpasswdr   r   r   �login   s"    




r   c                   C   s   t �d� t �d� d S )Nr	   zcat banner/bannerlight.txtr   r   r   r   r   �banner=   s    
r   c                   C   sl   z@t td � t�d� t�d� t d� t�d� t�d� W n& tk
rf   t t	d � t
�  Y nX d S )Nz$Checking Your Internet Connection...�   )zinformation-eg.blogspot.com�P   z[1;32m[+] You Are Connectedr
   r   z%[!] You Are Not Connected To Internet)r   �Wr   r   �socketZcreate_connectionr   r   �OSErrorr   r   r   r   r   r   �test_connectionB   s    


r   z"(israel)>>>> site:.gov.il inurl:idz0(United Kingdom [uk] )>>>> site:.gov.uk inurl:idz:(United States Of American [us] )>>> site:.gov.us inurl:idz!(China)>>> site:.gov.cn inurl:id zinurl:".php?cmd="zinurl:".php?z="zinurl:".php?q="zinurl:".php?search="zinurl:".php?query="u   inurl:".php?searchst­ring="u   inurl:".php?keyword=­"zinurl:".php?file="zinurl:".php?years="zinurl:".php?txt="zinurl:".php?tag="zinurl:".php?max="zinurl:".php?from="zinurl:".php?author="zinurl:".php?pass="u   inurl:".php?feedback­="zinurl:".php?mail="zinurl:".php?cat="zinurl:".php?vote="zinurl:search.php?q=u)   inurl:com_feedpostol­d/feedpost.php?url=u   inurl:scrapbook.php?­id=u   inurl:headersearch.p­hp?sid=u    inurl:/poll/­default.asp?catid=u%   inurl:/­search_results.php?se­arch=z>- https://www.gov.il/en/subjects/certificates_and_passports/idz8- https://services.mod.gov.il/Help/Api/GET-api-SubReq-idzI- https://services.mod.gov.il/Help/Api/DELETE-api-MarketingDestination-idz8- http://gpophoto.gov.il/haetonot/Eng_ShowPage.aspx?id=6z-- https://knesset.gov.il/mk/arb/mk.asp?ID=790zS- https://en.caa.gov.il/index.php?option=com_content&view=article&id=666&Itemid=371zE- https://services.mod.gov.il/Help/Api/DELETE-api-MarketingProduct-idz;- https://services.mod.gov.il/Help/Api/DELETE-api-Tester-idz8- https://services.mod.gov.il/Help/Api/PUT-api-SubReq-idz9- https://old.cbs.gov.il/reader/cw_usr_view_Folder?ID=141zh- https://mfa.gov.il/MFA/Government/Communiques/2003/ISA+Arrests+Ala-ah+Sheikh+Ale-id+-+Feb+12-+2003.htmz3- https://itrade.gov.il/netherlands2/tag/beller-id/z;- https://services.mod.gov.il/Help/Api/GET-api-SaveDraft-idzc- https://embassies.gov.il/bucharest/NewsAndEvents/Pages/New-lab-test-to-ID-early-lung-cancer-.aspxz@- http://www.parishcouncilwebsites.com/getting-started.php?id=12z*- http://www.evertz.com/frame/Bulk.php?id=z@- http://www.excelsiorhotel.com/prenotazioni_it.php?id_offerte=2zG- http://www.languagelink.com.cn/messageboard/language_convert.php?id=2z)- http://www.oil.lt/index.php?id=home&L=1z-- http://www.eurotubi.com/notizia-it.php?id=2z<- http://www.eminentelectronics.net/phones.php?carrier_id=11z - http://dbees.com/text.php?id=6z+- http://convert2mp3.net/c-mp3.php?url=httpz?- http://www.associazionecaniliveneto.it/news_eventi.php?id=354z1- http://www.apdcc.com.ar/mapa-countries.php?id=0z>- http://www.motoracingsupermotard.it/cardetail.php?id_car=148z,- http://ririechamber.com/business.php?id=28zV- http://www.univaq.it/en/macroarea.php?id=2,- http://oxxygene.ro/article_it.php?id=68zG- https://resourcecentre.globaliris.com/getting-started.php?id=opencartz0- http://consulsthailand.org/countries.php?id=36zB- http://us.fulbrightonline.org/program_regions_countries.php?id=5z)- https://www.allvoi.com/phones.php?id=27zE- http://www.simsim.ge/programs.php?id=8- http://grzl.net/it.php?id=4z=- http://www.comesaria.org/site/en/countries.php?id_article=3z1- https://www.mantisbt.org/bugs/view.php?id=13065zd- http://www.kristanix.com/getstarted.php?id=SE- http://www.radioendirect.net/countries.php?idCat=51r	   z{

[1] Ready Dorks
[2] Search For Dorks
[3] Download & Install sqlmap Tool
[4] XSS Dorks
[5] Sites affected by sql
[x] Exit
z[1;31mCHOICE>>>�1z[1;32mWait...r
   �2z%Enter The Dork That You Wanna Search:z[!] Not Foundz"Enter The Number Of Search Result:)�stopz[1;32m[+] URL Found: [1;36m� z<=======================>�3z+Do You Wanna Install sqlmap Tool...?! (y/n)�yz[+] Downloading sqlmap Tool...r   zcat banner/bannersql.txtz1git clone https://github.com/sqlmapproject/sqlmap�nzOkay,Done :) z[!] No Choices�4zWait...�5z<<<<<<< Fuck israel >>>>>>>�xzGood Bye Bro :) g�������?)�endz[1;31m[!] ERROR 404)%r   r   r   Zgooglesearchr   Zblackr   r   r!   �b�Pr   r   r   r   r   r   ZDorksZXSSZsqlr   �gr   ZchoiceZdorkr   Zwordr   �int�countZurlZacceptr   ZxssZsql_dork�close�charr   r   r   r   �<module>   s   " �
               �      �"	




















