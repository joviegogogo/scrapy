class UserAgentDownloadMiddleware(object):
    def process_request(self,request,spider):
        pass
        # if self.user_agent:
        #     request.headers.setdefault(b'User-Agent',self.user_agent)
