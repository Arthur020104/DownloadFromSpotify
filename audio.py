from pytube import YouTube
import os
import subprocess
import sys
from youtubesearchpython import VideosSearch
import string

def DownloadAudio(link, filename, onlyaudio, path):
    audio = 0
    filename = remove_non_ascii_and_symbols(filename)
    qualaudio = []
    
    # Pesquisa o vídeo no YouTube
    videosSearch = VideosSearch(link, limit=1)
    link = videosSearch.result()["result"][0]["link"]
    
    linkstream = YouTube(link).streams
    for x in linkstream:
        z = str(x)
        try:
            l = int(retornarpesquisa(z, 'abr="', 'type="audio"'))
            qualaudio.append(l)
        except:
            pass
            
    for x in linkstream:
        z = str(x)
        k = max(qualaudio)
        if (str(k) + 'kbps') in z:
            audio = x
            break
            
    audiotype = (retornarpesquisa(str(audio), 'mime_type="audio/', 'XXXXXX'))
    audiotype = audiotype[0:audiotype.find('"')]
    
    if onlyaudio == 1:
        i = 0
        existi_aquivo_com_msm_nome = os.path.exists(f"{path}/" + filename + '.' + audiotype) or os.path.exists(f"{path}/" + filename + '.mp3')
        
        while existi_aquivo_com_msm_nome:
            i += 1
            filename = f"{filename}{i}"
            existi_aquivo_com_msm_nome = os.path.exists(f"{path}/" + filename + '.' + audiotype) or os.path.exists(f"{path}/" + filename + '.mp3')
        
        try:
            audio.download(f"{path}/", filename=filename + '.' + audiotype)
        except:
            print(f"ERROR: Erro em baixar {filename}")
        
        if audiotype != 'mp3':
            src = (f"{path}/" + filename + '.' + audiotype)
            dst = (f"{path}/" + filename + '.mp3')
            subprocess.run(f'ffmpeg -i "{src}" "{dst}"', shell=False, capture_output=False, stdout=False, stderr=False)
            os.remove(f"{path}/" + filename + '.' + audiotype)
            return
        return

def retornarpesquisa(frase, acao, audioo):
    location = frase.find(acao)
    location += len(acao)
    name = ''
    name = "".join([i if i != "/n" and i != "" else "" for i in frase[location:len(frase)]])
    
    if audioo in name:
        name_t = ''
        for i in range(len(name)):
            x = name[i]
            if x == 'p' or (x == 'k' and name[i + 1] == 'b'):
                break
            name_t += x
        
        try:
            if int(name_t):
                return name_t.lstrip()
        except ValueError:
            return 1
    
    return name

def remove_non_ascii_and_symbols(input_string):
    allowed_chars = string.ascii_letters + string.digits + " "  # Include space
    cleaned_string = ''.join([char for char in input_string if char in allowed_chars])
    return cleaned_string