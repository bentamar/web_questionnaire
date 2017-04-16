from setuptools import setup

setup(
    name="wq_project",
    packages=["wq_project"],
    include_package_data=True,
    install_requires=[
        "django",
        "email",
        "smtplib"
    ]
)
