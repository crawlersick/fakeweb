from typing import Optional, Awaitable

import tornado
import tornado.web
import tornado.escape
import logging
import json


class ApiCommon(tornado.web.RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def my_finish(self, msg_dict):
        self.finish(json.dumps(msg_dict, ensure_ascii=False))

    def my_get_post_data(self):
        pd = tornado.escape.json_decode(self.request.body)
        logging.info('----got post data as:----')
        logging.info(pd)
        return pd

    def my_get_args(self):
        t_args = self.request.arguments
        logging.info('----got get data as:----')
        logging.info(t_args)
        r = {x: t_args.get(x)[0].decode("utf-8") for x in t_args.keys()}
        return r

    def prepare(self) -> Optional[Awaitable[None]]:
        logging.info(">>>>>>>>>>>>>>>>request header as:")
        logging.info(self.request.headers)

    def options(self):
        logging.info(">>>>>options request pass")
        pass

    def set_default_headers(self) -> None:
        self.set_header('Content-Type', 'application/json')
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', '*')


