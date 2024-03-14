from django.utils.translation import gettext_lazy as _
from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible


@deconstructible
class MaxImageSizeValidator(BaseValidator):
    message = _("The image size should not exceed %(limit_value)s MB.")
    code = "image_size_limit"

    def compare(self, image_file, limit_value):
        """
        Compare the size of the image file with the specified limit.
        """
        max_size_bytes = limit_value * 1024 * 1024  # Convert MB to bytes
        return image_file > max_size_bytes

    def clean(self, image_file):
        """
        Clean the value by checking if it's an image file.
        """
        if not image_file:
            return 0  # Return 0 if no image file is provided
        if not image_file._committed:
            # If the file is not committed (not yet saved), use temporary file size
            return image_file.file.size
        # If the file is committed (saved), get the actual file size
        return image_file.size
