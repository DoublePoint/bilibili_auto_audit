import mitmproxy.http
from mitmproxy import ctx

path = 'D:/video/'
class Counter:
    def __init__(self):
        self.num = 0

    def requests(self, flow: mitmproxy.http.HTTPFlow):
        self.num = self.num + 1
        ctx.log.info("We've seen %d flows" % self.num)

    def response(self,flow: mitmproxy.http.HTTPFlow):
        resp = flow.response
        response_header = resp.headers
        if 'Content-Type' in response_header:
            content_type = response_header['Content-Type']
            ctx.log.info("Content Type is %s " % content_type)
            if 'video/mp4' in content_type:
                print('这里返回的视频')
                # 设置视频名
                self.num = self.num + 1
                filename = path + str(self.num) + '.mp4'
                with open(filename, 'wb') as f:
                    ctx.log.info(resp.content)
                    f.write(resp.content)
                f.close()
                print(filename + '下载完成')

addons = [
    Counter()
]
