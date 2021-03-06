# coding: utf-8

"""
    Onfido API

    The Onfido API is used to submit background checking requests

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import os
import sys
import unittest

import onfido
from onfido.rest import ApiException
from onfido.apis.default_api import DefaultApi


class TestDefaultApi(unittest.TestCase):
    """ DefaultApi unit test stubs """

    def setUp(self):
        self.api = onfido.apis.default_api.DefaultApi()

    def tearDown(self):
        pass

    def test_cancel_report(self):
        """
        Test case for cancel_report

        This endpoint is for cancelling individual paused reports.
        """
        pass

    def test_create_applicant(self):
        """
        Test case for create_applicant

        Create Applicant
        """
        pass

    def test_create_check(self):
        """
        Test case for create_check

        Create a check
        """
        pass

    def test_destroy_applicant(self):
        """
        Test case for destroy_applicant

        Delete Applicant
        """
        pass

    def test_download_document(self):
        """
        Test case for download_document

        Download a documents raw data
        """
        pass

    def test_find_applicant(self):
        """
        Test case for find_applicant

        Retrieve Applicant
        """
        pass

    def test_find_check(self):
        """
        Test case for find_check

        Retrieve a Check
        """
        pass

    def test_find_document(self):
        """
        Test case for find_document

        A single document can be retrieved by calling this endpoint with the document’s unique identifier.
        """
        pass

    def test_find_report(self):
        """
        Test case for find_report

        A single report can be retrieved using this endpoint with the corresponding unique identifier.
        """
        pass

    def test_find_report_type_group(self):
        """
        Test case for find_report_type_group

        Retrieve single report type group object
        """
        pass

    def test_list_applicants(self):
        """
        Test case for list_applicants

        List Applicants
        """
        pass

    def test_list_checks(self):
        """
        Test case for list_checks

        Retrieve Checks
        """
        pass

    def test_list_documents(self):
        """
        Test case for list_documents

        List documents
        """
        pass

    def test_list_report_type_groups(self):
        """
        Test case for list_report_type_groups

        Retrieve all report type groups
        """
        pass

    def test_list_reports(self):
        """
        Test case for list_reports

        All the reports belonging to a particular check can be listed from this endpoint.
        """
        pass

    def test_resume_check(self):
        """
        Test case for resume_check

        Resume a Check
        """
        pass

    def test_resume_report(self):
        """
        Test case for resume_report

        This endpoint is for resuming individual paused reports.
        """
        pass

    def test_update_applicant(self):
        """
        Test case for update_applicant

        Update Applicant
        """
        pass

    def test_upload_document(self):
        """
        Test case for upload_document

        Upload a document
        """
        pass


if __name__ == '__main__':
    unittest.main()
