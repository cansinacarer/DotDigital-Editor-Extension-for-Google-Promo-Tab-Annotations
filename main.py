from app.utilities import read_file, update_block

# Deals block fields
block_inputs = [
    {
        "id": "deal_description",
        "name": "Description",
        "parameter_type": "string",
        "default_value": "",
        "required": False,
        "help": "Optional. The text that displays with the deal badge, such as 20% off or Free shipping.",
    },
    {
        "id": "deal_discount_Code",
        "name": "Discount code",
        "parameter_type": "string",
        "default_value": "",
        "required": False,
        "help": "Optional. The discount or promotion code for the offer, such as 20TODAY.",
    },
    {
        "id": "deal_start_date_time",
        "name": "Deal start date and time",
        "parameter_type": "date-time",
        "request_time": True,
        "default_value": "",
        "required": False,
        "help": "Optional. The date and time when the offer begins in ISO 8601 format, such as 2024-11-25T08:00:00-04:00",
    },
    {
        "id": "deal_end_date_time",
        "name": "Deal end date and time",
        "parameter_type": "date-time",
        "request_time": True,
        "default_value": "",
        "required": False,
        "help": "Optional. The end date and time of the promotion in ISO 8601 format, such as 2024-11-28T23:59:59-04:00",
    },
]

# Upload the deals block
update_block(
    block_key="deal_annotation",
    group_name="Promo Annotations",
    group_icon=read_file("app/svg/star.svg"),
    block_name="Deal Annotation",
    block_icon=read_file("app/svg/deal.svg"),
    block_desc="Used to display promo codes.",
    block_inputs=block_inputs,
    template=read_file("app/html/deal.html"),
    extension_key="promo_annotations",
)


# Logo block fields
block_inputs = [
    {
        "id": "logo_url",
        "name": "Logo URL",
        "parameter_type": "string",
        "default_value": "",
        "required": True,
        "help": "Required. Upload the image in the email builder, then paste the URL of the uploaded image here.",
    },
]


# Upload the logo block
update_block(
    block_key="logo_annotation",
    group_name="Promo Annotations",
    group_icon=read_file("app/svg/star.svg"),
    block_name="Logo Annotation",
    block_icon=read_file("app/svg/logo.svg"),
    block_desc="Used to display a custom logo as the sender profile picture.",
    block_inputs=block_inputs,
    template=read_file("app/html/logo.html"),
    extension_key="promo_annotations",
)


# Product block fields - Using this block multiple times creates the carousel
block_inputs = [
    {
        "id": "image_url",
        "name": "Image URL",
        "parameter_type": "string",
        "default_value": "",
        "required": True,
        "help": "Required. Upload the image in the email builder, then paste the URL of the uploaded image here.",
    },
    {
        "id": "promo_url",
        "name": "Promo URL",
        "parameter_type": "string",
        "default_value": "",
        "required": True,
        "help": "Required. The URL for the promotion. When users click on the email's image, they are directed to this URL.",
    },
    {
        "id": "headline",
        "name": "Headline",
        "parameter_type": "string",
        "default_value": "",
        "required": False,
        "help": "Optional. A 1 to 2-line description of the promotion that is displayed under the image.",
    },
    {
        "id": "price",
        "name": "Price",
        "parameter_type": "string",
        "default_value": "",
        "required": False,
        "help": "Optional. The price of the promotion. If Discount Value is set, shows original price before the discount.",
    },
    {
        "id": "price_currency",
        "name": "Price Currency",
        "parameter_type": "string",
        "default_value": "",
        "required": False,
        "help": "Optional. The currency of the price in 3-letter ISO 4217 format, such as USD.",
    },
    {
        "id": "discount_value",
        "name": "Discount Value",
        "parameter_type": "string",
        "default_value": "",
        "required": False,
        "help": "Optional. The amount subtracted from the price to display an adjusted price.",
    },
    {
        "id": "order",
        "name": "Product Order",
        "parameter_type": "numeric",
        "default_value": "",
        "required": False,
        "help": "Optional. The amount subtracted from the price to display an adjusted price.",
    },
]


# Upload the Product block
update_block(
    block_key="product",
    group_name="Promo Annotations",
    group_icon=read_file("app/svg/star.svg"),
    block_name="Product Preview Annotation",
    block_icon=read_file("app/svg/product.svg"),
    block_desc="You can use this block to showcase a product. You can add this block more than once to create a carousel. The image must be in PNG or JPEG format. The supported aspect ratios are 4:5, 1:1, and 1.91:1. Images are center-cropped automatically.",
    block_inputs=block_inputs,
    template=read_file("app/html/product.html"),
    extension_key="promo_annotations",
)


# Subject
block_inputs = [
    {
        "id": "subject_line",
        "name": "Subject Line",
        "parameter_type": "string",
        "default_value": "",
        "required": True,
        "help": "Required. Type in the subject line here.",
    },
]

update_block(
    block_key="subject_annotation",
    group_name="Promo Annotations",
    group_icon=read_file("app/svg/star.svg"),
    block_name="Subject Annotation",
    block_icon=read_file("app/svg/subject.svg"),
    block_desc="You can use this block to add the annotation for the subject line.",
    block_inputs=block_inputs,
    template=read_file("app/html/subject.html"),
    extension_key="promo_annotations",
)
