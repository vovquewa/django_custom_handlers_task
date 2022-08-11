from django.test import TestCase


class ViewTestClass(TestCase):
    def test_error_page(self):
        url = '/nonexist-page/'
        template = 'core/404.html'
        response = self.client.get(url)
        
        
        # Проверьте, что статус ответа сервера - 404
        self.assertEqual(response.status_code, 404)
        # Проверьте, что используется шаблон core/404.html
        self.assertTemplateUsed(response,template)
        
        
    