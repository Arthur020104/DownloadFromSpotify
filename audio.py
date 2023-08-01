from pytube import YouTube
import os
import urllib.request
import re
import subprocess
import sys

def DownloadAudio(link,filename,onlyaudio,path):
    audio = 0
    qualaudio = []

    link = link.replace(" ", "_" )
    html = urllib.request.urlopen('https://www.youtube.com/results?search_query='+link)
    ids = re.findall(r"watch\s?(\S{14})",html.read().decode())
    for id in ids:
        if '?v=' in id:
            ids = id
            break
    link = 'https://www.youtube.com/watch'+ids
    linkstream = YouTube(link).streams
    for x in linkstream:
        z = str(x)
        try :
            l = int(retornarpesquisa(z,'abr="','type="audio"'))
            qualaudio.append(l)
        except:
            pass
    for x in linkstream:
        z = str(x)
        k = max(qualaudio)
        if (str(k)+'kbps') in z :
            audio=x
            break
    audiotype = (retornarpesquisa(str(audio), 'mime_type="audio/','XXXXXX'))
    audiotype= audiotype[0:audiotype.find('"')]
    if onlyaudio == 1:
        i = 0
        existi_aquivo_com_msm_nome = os.path.exists(f"{path}/"+filename+'.'+audiotype) or os.path.exists(f"{path}/"+filename+'.mp3')
        while existi_aquivo_com_msm_nome:
            i +=1
            filename = f"{filename}{i}"
            existi_aquivo_com_msm_nome = os.path.exists(f"{path}/"+filename+'.'+audiotype) or os.path.exists(f"{path}/"+filename+'.mp3')
        try:
            
            audio.download(f"{path}/",filename = filename+'.'+audiotype)
        except:
            print(f"ERROR: Erro em baixar {filename}")
        if audiotype != 'mp3':
            src = (f"{path}/"+filename+'.'+audiotype)
            dst = (f"{path}/"+filename+'.mp3')
            subprocess.run(f'ffmpeg -i "{src}" "{dst}"',shell=False,capture_output=False,stdout=False,stderr=False)
            os.remove(f"{path}/"+filename+'.'+audiotype)
            return
        return
def retornarpesquisa(frase, acao,audioo):
    location = frase.find(acao)
    location += len(acao)
    name = ''
    name = "".join([i if i != "/n" and i != ""else "" for i in frase[location:len(frase)]])
    if audioo in name:
        name_t = ''
        for i in range(len(name)):
            x=name[i]
            if x =='p'or (x=='k'and name[i+1]=='b'):
                break
            name_t += x
        try:
            if(int(name_t)):
                return name_t.lstrip()
        except ValueError: 
            return 1
    return name

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)