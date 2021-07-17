from django.test import TestCase

from apps.corecode.models import (
    AcademicSession,
    AcademicTerm,
    SiteConfig,
    Subject,
)


class SiteConfigTest(TestCase):
    def test_siteconfig(self):
        site_config = SiteConfig.objects.create(key="akey", value="aname")
        self.assertEqual(str(site_config), "akey")


class AcademicSessionTest(TestCase):
    def test_academicsession(self):
        session = AcademicSession.objects.create(name="test session", current=True)
        self.assertEqual(str(session), "test session")


class AcademicTermTest(TestCase):
    def test_academicterm(self):
        term = AcademicTerm.objects.create(name="test Term", current=True)
        self.assertEqual(str(term), "test Term")


class SubjectTest(TestCase):
    def test_subject(self):
        subject = Subject.objects.create(name="a_subject")
        self.assertEqual(str(subject), "a_subject")
