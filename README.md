## Hello Flask Testing

Very basic app. Shows list of animals, can select animal, see list of attributes.

On attributes page, can click like button.

Relies on deliberately buggy backend.py file.

Tests in test.py check for happy paths, and various ways requests can go wrong. For example, unexpected data in request, missing data in request, requests for animals that don't exist. 