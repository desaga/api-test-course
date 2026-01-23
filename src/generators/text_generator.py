# src/generators/text_generator.py
from lorem_text import lorem
import random
import json


def get_lorem_create_product_payload():
    create_product_data = {
        "name": lorem.words(random.randint(1, 4)).title() + '.',
        "type": "simple",
        "regular_price": f"{(round(random.uniform(0, 10000), 2)):.2f}",
        "description": " ".join(
            lorem.sentence() for _ in range(random.randint(2, 3))),
        "short_description": lorem.sentence(),
    }
    return create_product_data


if __name__ == "__main__":
    load = get_lorem_create_product_payload()
    print(json.dumps(load, indent=2))
