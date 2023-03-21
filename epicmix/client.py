# -*- coding: utf-8 -*-
"""A simple python package for the EpicMix Web API.
"""

import requests
from epicmix.exceptions import EpicError
from epicmix.models import LifetimeStats

AUTH_URL = "https://bridge.mountain.live/passerelles/clients/Vail/authentication/v3/authentication.php"
API_URL = "https://bridge.mountain.live/passerelles/clients/Vail/proxy.php"


class EpicMix:
    """A Python wrapper for the EpicMix API.

    This class provides a convenient way to access and interact with the EpicMix API
    by handling authentication, sending HTTP requests, and parsing JSON responses.
    To use this class, you'll need to have a valid EpicMix account.

    Attributes:
        user_creds: A dictionary containing the user's username and password.


    Typical usage example:
        rider = EpicMix(username, password)
        lt_stats = rider.get_lifetime_stats()
    """

    def __init__(
        self,
        username: str,
        password: str,
        requests_session: requests.Session | None = None,
    ) -> None:
        """Initializes an Epic Mix API client.

        Args:
            username:
                A string containing the user's Epic Mix username (email)
            password:
                A string containing the user's Epic Mix password
            requests_session:
                A Requests session object or None to create one.
        """
        self.user_creds = {"username": username, "password": password}
        self._auth_response = None

        if requests_session is not None:
            self._session = requests_session
        else:
            self._session = requests.Session()

        self._authenticate()

    def _make_request(self, method: str, url: str, **kwargs) -> dict:
        try:
            response = self._session.request(method, url, **kwargs)
            response.raise_for_status()
            result = response.json()

        except requests.exceptions.HTTPError as http_error:
            response = http_error.response
            try:
                json_response = response.json()
                error_msg = json_response.get("error")
                description = json_response.get("error_description")
            except requests.exceptions.JSONDecodeError:
                error_msg = response.text or None
                description = None

            raise EpicError(
                http_status=response.status_code,
                reason=response.reason,
                msg=error_msg,
                description=description,
            ) from http_error

        return result

    def _authenticate(self):
        if self._auth_response is None:
            response = self._make_request(
                "POST",
                AUTH_URL,
                params=self._make_auth_params("authenticate"),
                json=self.user_creds,
            )
        else:
            response = self._make_request(
                method="POST",
                url=AUTH_URL,
                params=self._make_auth_params("token"),
                json=self._auth_response,
            )

        self._auth_response = response["specific"]
        self._api_headers = {
            "Authorization": str(
                "Bearer " + self._auth_response["tokenResponse"]["accessToken"]
            )
        }

    def get_lifetime_stats(self) -> LifetimeStats:
        """Gets lifetime stats from Epic Mix

        Returns:
            dict: User's lifetime stats
        """
        response = self._get("v3/Stats/LifetimeStat")
        return LifetimeStats(**response["data"])

    def _get(self, path):
        try:
            response = self._make_request(
                method="GET",
                url=API_URL,
                params=self._make_api_query(path),
                headers=self._api_headers,
            )
        except EpicError as epic_error:
            # Handles expired accessToken
            if epic_error.http_status == 401:
                self._authenticate()
                response = self._make_request(
                    method="GET",
                    url=API_URL,
                    params=self._make_api_query(path),
                    headers=self._api_headers,
                )
        return response

    def _make_api_query(self, path: str) -> dict:
        return {"env": "PROD", "path": path}

    def _make_auth_params(self, mode: str) -> dict:
        return {"env": "PROD", "mode": mode, "lang": "en"}
