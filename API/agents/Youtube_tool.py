from langchain_community.tools import YouTubeSearchTool
import ast

async def youTube_search(query: str):
    tool = YouTubeSearchTool()
    youtube_links = tool.run(query)
    if isinstance(youtube_links, str):
        try:
            youtube_links = ast.literal_eval(youtube_links)
        except:
            youtube_links = [youtube_links]
    return youtube_links;

