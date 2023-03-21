# -*- coding: utf-8 -*-


class EpicError(Exception):
    """There was an exception that occurred while preforming your request."""

    def __init__(
        self,
        http_status: int,
        reason: str,
        msg: str | None = None,
        description: str | None = None,
    ):
        self.http_status = http_status
        self.reason = reason
        self.msg = msg
        self.description = description

    def __str__(self):
        return f"""
        Http Status: {str(self.http_status)}
        Http Reason: {self.reason}
        Error Message: {self.msg}
        Error Description: {self.description}"""
