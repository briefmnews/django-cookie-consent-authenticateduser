import pytest
from django.template import Context, Template

pytestmark = pytest.mark.django_db


class TestDisplayCookieConsent:
    @pytest.mark.usefixtures("cookie_group")
    def test_no_cookies_set_in_request(self, request_builder):
        # GIVEN
        request = request_builder.get()

        # Template using the template tag
        template_code = """
        {% load cookie_tags %}
        {% display_cookie_consent %}
        """

        # WHEN
        template = Template(template_code)
        context = Context({"request": request})
        rendered_template = template.render(context)

        # THEN
        assert "My custom cookie banner here" in rendered_template

    def test_cookies_set_in_request(self, request_builder, cookie_group, settings):
        # GIVEN
        request = request_builder.get()
        request.COOKIES[settings.COOKIE_CONSENT_NAME] = f"{cookie_group.varname}=dummy"

        # Template using the template tag
        template_code = """
        {% load cookie_tags %}
        {% display_cookie_consent %}
        """

        # WHEN
        template = Template(template_code)
        context = Context({"request": request})
        rendered_template = template.render(context)

        # THEN
        assert "My custom cookie banner here" not in rendered_template

    def test_no_cookies_in_request_but_in_database(
        self, request_builder, user_with_preferences
    ):
        # GIVEN
        request = request_builder.get(user=user_with_preferences)

        # Template using the template tag
        template_code = """
        {% load cookie_tags %}
        {% display_cookie_consent %}
        """

        # WHEN
        template = Template(template_code)
        context = Context({"request": request})
        rendered_template = template.render(context)

        # THEN
        assert "My custom cookie banner here" not in rendered_template

    def test_no_cookies_set_in_request_nor_database(self, request_builder, user):
        # GIVEN
        request = request_builder.get(user=user)

        # Template using the template tag
        template_code = """
        {% load cookie_tags %}
        {% display_cookie_consent %}
        """

        # WHEN
        template = Template(template_code)
        context = Context({"request": request})
        rendered_template = template.render(context)

        # THEN
        assert "My custom cookie banner here" in rendered_template
