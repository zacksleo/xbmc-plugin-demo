import sys
import xbmcgui
import xbmcplugin
import urllib.parse

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urllib.parse.parse_qs(sys.argv[2][1:])

defaultImg = 'http://i2.hdslb.com/bfs/archive/1a846ab7cbc91cd795d7c2cc18575ceb7c53df93.jpg'
defaultImg2 = 'http://i1.hdslb.com/bfs/archive/0fff9526870060581a05c08f0740d74fdac8aac4.jpg'

xbmcplugin.setContent(addon_handle, 'movies')


def build_url(query):
    return base_url + '?' + urllib.parse.urlencode(query)


mode = args.get('mode', None)

if mode is None:
    url = build_url({'mode': 'folder', 'foldername': 'Folder A'})
    li = xbmcgui.ListItem('Folder A', 'label2', "path")
    li.setArt({
        'thumb': defaultImg,
        'poster': defaultImg,
        'banner': defaultImg,
        'fanart': defaultImg,
        'clearart': defaultImg,
        'clearlogo': defaultImg,
        'landscape': defaultImg,
        'icon': defaultImg,
    })
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=True)
    url = build_url({'mode': 'folder', 'foldername': 'Folder B'})
    li = xbmcgui.ListItem('Folder B', 'label2', 'path')
    li.setArt({
        'thumb': defaultImg2,
        'poster': defaultImg2,
        'banner': defaultImg2,
        'fanart': defaultImg2,
        'clearart': defaultImg2,
        'clearlogo': defaultImg2,
        'landscape': defaultImg2,
        'icon': defaultImg2,
    })
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=True)
    xbmcplugin.endOfDirectory(addon_handle)

elif mode[0] == 'folder':
    foldername = args['foldername'][0]
    url = 'https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-mp4-file.mp4'
    li = xbmcgui.ListItem('三体影视化四大版本信息汇总 前景越来越灰暗？【玫瑰叔品三体】', "label2", "path")
    li.setArt({
        'thumb': defaultImg,
        'poster': defaultImg,
        'banner': defaultImg,
        'fanart': defaultImg,
        'clearart': defaultImg,
        'clearlogo': defaultImg,
        'landscape': defaultImg,
        'icon': defaultImg,
    })
    li.setInfo('video', {
        'genre': '影视杂谈',
        'title': '三体影视化四大版本信息汇总 前景越来越灰暗？【玫瑰叔品三体】',
        'plot': '久违了的玫瑰叔品三体又来一期特别篇，先梳理三体影视化四大版本目前的进度，包括动画版三体，电影版三体，网剧版三体和美剧版三体，然后谈谈我对三体影视化的预期为什么越来越悲观，现在说不要拍摄不要拍摄不要拍摄还来得及吗？最后有计划的一部分。',
        'duration': 300,
        'country': '中国',
        'year': 2020,
        'episode': 1,
        'season': 1,
        'rating': 5,
        'playcount': 100,
        'overlay': xbmcgui.ICON_OVERLAY_WATCHED,
        'cast': ['Fuji_玫瑰叔'],
        'director': 'Fuji_玫瑰叔',
        'writer': 'Fuji_玫瑰叔',
        'originaltitle': '久违了的玫瑰叔品三体又来一期特别篇，先梳理三体影视化四大版本目前的进度，包括动画版三体，电影版三体，网剧版三体和美剧版三体，然后谈谈我对三体影视化的预期为什么越来越悲观，现在说不要拍摄不要拍摄不要拍摄还来得及吗？最后有计划的一部分。',
        'mediatype': 'video',
        'studio': 'Fuji_玫瑰叔',
        'aired': '2020-05-01',
        'artist': ['Fuji_玫瑰叔'],
        'votes': '100',
        'lastplayed': '2009-04-05 23:16:04',
        'dateadded': '2009-04-05 23:16:04',
        'tag': '影视杂谈',
        'userrating': 10,
        'showlink': ['Fuji_玫瑰叔'],
    })
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    xbmcplugin.endOfDirectory(addon_handle)
