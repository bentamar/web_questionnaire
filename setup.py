from setuptools import setup

setup(
    name="web_questionnaire",
    packages=["web_questionnaire"],
    include_package_data=True,
    install_requires=[
        "flask",
        "email",
        "smtplib",
        "pymongo"
    ]
)
