from pytube import Search
import webbrowser

def play_youtube(query):
    search = Search(query)
    if search.results:
        video_url = f"https://www.youtube.com/watch?v={search.results[0].video_id}"
        webbrowser.open(video_url)
        return f"Playing: {search.results[0].title}"
    return "No results found."