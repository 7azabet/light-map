a
    2��`�  �                   @   s  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZzd dlZW n( eyl   e�	dej
d  � �� Y n0 d dlmZ dZdZdZdZdZdZd	Zd
Zdd� Zdd� Zdd� Zdd� Zg d�Zg d�Zg d�Zed� e�  e�  e�  eed � dZede �Zedk�rDed� eD ]Ze� d� ee� �qed� �n�edk�r�e�  eed e �Z!e!dk�r|ed� e"�  e#eed e ��Z$e$dk�r�ed� e"�  ee!e$d �D ](Z%ed� e� d� ed!e%� d"�� �q�eed# � ed� �ned$k�r�eed% e �Z&e&d&k�rTeed' e � e� d(� e�	d� e�	d)� e�	d*� n*e&d+k�rleed, � need- � e"�  n�ed.k�r�ed/� e� d� eD ]Z'e� d� eee' � �q�nPed0k�red/� e� d� eD ]Z(e� d� ee(� �q�eed1 � ned2� dS )3�    Nz"pip install googlesearch; python3 )�searchz[1;30mz[1;31mz[1;32mz[1;33mz[1;35mz[1;36mz[1;37mc                   C   s   t �d� d S )N�clear��os�system� r   r   �lightmap.pyr      s    r   c                  C   s�   t �d� t �d� td� t�  ttd � ttd t �} t�td t �}d}d}| |kr�||kr�t	�
d	� ttd
 � t	�
d� n&t	�
d� ttd � t	�
d� t�  d S )Nznohup pip3 install google &z#nohup pip3 install beautifulsoup4 &� a-  
    
dP                   oo          
88                               
88 .d8888b. .d8888b. dP 88d888b. 
88 88'  `88 88'  `88 88 88'  `88 
88 88.  .88 88.  .88 88 88    88 
dP `88888P' `8888P88 dP dP    dP 
                 .88             
             d8888P              
             
         z
USERNAME: z
PASSWORD: ZPerSonZ	Palestineg      �?z[+] Done Successfully :) �   z[!] NOT FOUNDg�������?)r   r   �printr   �G�input�R�C�getpass�time�sleep�exit)ZUSERNAMEZPASSWORD�userZpasswdr   r   r   �login"   s"    




r   c                   C   s   t �d� t �d� d S )Nr	   zcat banner/bannerlight.txtr   r   r   r   r   �bannerD   s    
r   c                   C   sr   zHt td � t�d� t�d� t d� t�d� t�d� t d� W n$ tyl   t t	d � t
�  Y n0 d S )	Nz$Checking Your Internet Connection...�   )zinformation-eg.blogspot.com�P   z[1;32m[+] You Are Connectedr
   r   r	   z%[!] You Are Not Connected To Internet)r   �Wr   r   �socketZcreate_connectionr   r   �OSErrorr   r   r   r   r   r   �test_connectionI   s    



r   )z"(israel)>>>> site:.gov.il inurl:idz0(United Kingdom [uk] )>>>> site:.gov.uk inurl:idz:(United States Of American [us] )>>> site:.gov.us inurl:idz!(China)>>> site:.gov.cn inurl:id )zinurl:".php?cmd="zinurl:".php?z="zinurl:".php?q="zinurl:".php?search="zinurl:".php?query="u   inurl:".php?searchst­ring="u   inurl:".php?keyword=­"zinurl:".php?file="zinurl:".php?years="zinurl:".php?txt="zinurl:".php?tag="zinurl:".php?max="zinurl:".php?from="zinurl:".php?author="zinurl:".php?pass="u   inurl:".php?feedback­="zinurl:".php?mail="zinurl:".php?cat="zinurl:".php?vote="zinurl:search.php?q=u)   inurl:com_feedpostol­d/feedpost.php?url=u   inurl:scrapbook.php?­id=u   inurl:headersearch.p­hp?sid=u    inurl:/poll/­default.asp?catid=u%   inurl:/­search_results.php?se­arch=))z<https://www.gov.il/en/subjects/certificates_and_passports/idz6https://services.mod.gov.il/Help/Api/GET-api-SubReq-idzGhttps://services.mod.gov.il/Help/Api/DELETE-api-MarketingDestination-idz6http://gpophoto.gov.il/haetonot/Eng_ShowPage.aspx?id=6z+https://knesset.gov.il/mk/arb/mk.asp?ID=790zQhttps://en.caa.gov.il/index.php?option=com_content&view=article&id=666&Itemid=371�Chttps://services.mod.gov.il/Help/Api/DELETE-api-MarketingProduct-id�9https://services.mod.gov.il/Help/Api/DELETE-api-Tester-idz6https://services.mod.gov.il/Help/Api/PUT-api-SubReq-idz7https://old.cbs.gov.il/reader/cw_usr_view_Folder?ID=141zfhttps://mfa.gov.il/MFA/Government/Communiques/2003/ISA+Arrests+Ala-ah+Sheikh+Ale-id+-+Feb+12-+2003.htmz1https://itrade.gov.il/netherlands2/tag/beller-id/r   �9https://services.mod.gov.il/Help/Api/GET-api-SaveDraft-idr   r   zahttps://embassies.gov.il/bucharest/NewsAndEvents/Pages/New-lab-test-to-ID-early-lung-cancer-.aspxz@- http://www.parishcouncilwebsites.com/getting-started.php?id=12z*- http://www.evertz.com/frame/Bulk.php?id=z@- http://www.excelsiorhotel.com/prenotazioni_it.php?id_offerte=2zG- http://www.languagelink.com.cn/messageboard/language_convert.php?id=2z)- http://www.oil.lt/index.php?id=home&L=1z-- http://www.eurotubi.com/notizia-it.php?id=2z<- http://www.eminentelectronics.net/phones.php?carrier_id=11zL- http://dbees.com/text.php?id=6,- http://convert2mp3.net/c-mp3.php?url=httpz?- http://www.associazionecaniliveneto.it/news_eventi.php?id=354z1- http://www.apdcc.com.ar/mapa-countries.php?id=0z>- http://www.motoracingsupermotard.it/cardetail.php?id_car=148z,- http://ririechamber.com/business.php?id=28z,- http://www.univaq.it/en/macroarea.php?id=2z)- http://oxxygene.ro/article_it.php?id=68zG- https://resourcecentre.globaliris.com/getting-started.php?id=opencartz0- http://consulsthailand.org/countries.php?id=36zB- http://us.fulbrightonline.org/program_regions_countries.php?id=5z)- https://www.allvoi.com/phones.php?id=27z(- http://www.simsim.ge/programs.php?id=8z- http://grzl.net/it.php?id=4z=- http://www.comesaria.org/site/en/countries.php?id_article=3z1- https://www.mantisbt.org/bugs/view.php?id=13065z/- http://www.kristanix.com/getstarted.php?id=SEz5- http://www.radioendirect.net/countries.php?idCat=51r	   zs

[1] Ready Dorks
[2] Search For Dorks
[3] Download & Install sqlmap Tool
[4] XSS Dorks
[5] Sites affected by sql

z[1;31mCHOICE >>> �1z[1;32mWait...r
   �2z%Enter The Dork That You Wanna Search:z[!] Not Foundz"Enter The Number Of Search Result:)Znum_resultsz[1;32m[+] URL Found: [1;36m� z<=======================>�3z+Do You Wanna Install sqlmap Tool...?! (y/n)�yz[+] Downloading sqlmap Tool...r   zcat banner/bannersql.txtz1git clone https://github.com/sqlmapproject/sqlmap�nzOkay,Done :) z[!] No Choices�4zWait...�5zFuck israelz[1;31m[!] ERROR 404))r   r   r   �sysr   Z
webbrowserZurllib3Zgooglesearch�ModuleNotFoundErrorr   �argvr   Zblackr   r   r$   �b�Pr   r   r   r   r   r   ZDorksZXSSZsqlr   �gr   ZchoiceZdorkr   Zwordr   �int�countZurlZacceptZxssZsql_dorkr   r   r   r   �<module>   s�   ""



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





