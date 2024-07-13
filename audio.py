from youtubesearchpython import VideosSearch
import string
import yt_dlp
from unidecode import unidecode
def DownloadAudio(link_name, filename, onlyaudio, path):
    filename = remove_non_ascii_and_symbols(filename)
    
    # Pesquisa o vídeo no YouTube
    link_name += " audio"
    videosSearch = VideosSearch(link_name, limit=1)
    link_name = videosSearch.result()["result"][0]["link"]
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{path}/{filename}.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }] if onlyaudio else {}
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link_name])
    except Exception as e:
        print(f"ERROR: Erro em baixar {filename}. Erro: {e}")

def remove_non_ascii_and_symbols(input_string):
    cleaned_string = unidecode(input_string)  # Converte caracteres não-ASCII para ASCII
    allowed_chars = string.ascii_letters + string.digits + " "  # Inclui espaço
    cleaned_string = ''.join([char for char in cleaned_string if char in allowed_chars])
    return cleaned_string
