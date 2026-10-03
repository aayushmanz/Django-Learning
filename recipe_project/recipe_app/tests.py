from pathlib import Path
from tempfile import TemporaryDirectory

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings

from .models import recipe


class RecipeImageUploadTests(TestCase):
    def setUp(self):
        self.media_directory = TemporaryDirectory()
        self.media_override = override_settings(MEDIA_ROOT=self.media_directory.name)
        self.media_override.enable()

    def tearDown(self):
        self.media_override.disable()
        self.media_directory.cleanup()

    def test_upload_is_saved_and_rendered(self):
        image = SimpleUploadedFile(
            "recipe.png",
            (
                b"\x89PNG\r\n\x1a\n"
                b"\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01"
                b"\x08\x06\x00\x00\x00\x1f\x15\xc4\x89"
                b"\x00\x00\x00\x0cIDAT\x08\xd7c\xf8\xcf\xc0\xf0\x1f\x00"
                b"\x05\x00\x01\xff\x89\x99=\x1d\x00\x00\x00\x00IEND\xaeB`\x82"
            ),
            content_type="image/png",
        )

        response = self.client.post(
            "/recipe/",
            {
                "recipe_name": "Pasta",
                "recipe_desc": "Simple pasta",
                "recipe_img": image,
            },
        )

        self.assertRedirects(response, "/recipe/")
        saved_recipe = recipe.objects.get()
        self.assertEqual(saved_recipe.recipe_img.name, "recipe_images/recipe.png")
        self.assertTrue(
            Path(self.media_directory.name, saved_recipe.recipe_img.name).is_file()
        )

        response = self.client.get("/recipe/")
        self.assertContains(response, saved_recipe.recipe_img.url)

# Create your tests here.
