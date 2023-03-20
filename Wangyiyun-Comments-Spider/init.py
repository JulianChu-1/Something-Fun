import CommentSpider
import DataCleaning

if __name__ == '_main_':
    CommentSpider.Spider("https://music.163.com/#/song?id=413829859",20)
    DataCleaning.dataCleaning(20)
