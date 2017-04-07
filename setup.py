#!/usr/bin/python3
# Copyright (C) 2017, Hadron Industries, Inc.
# Entanglement is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# as published by the Free Software Foundation. It is distributed
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the file
# LICENSE for details.


from setuptools import setup

setup(
    name = "hadron.entanglement",
    license = "proprietary",
    maintainer = "Sam Hartman",
    maintainer_email = "sam.hartman@hadronindustries.com",
    url = "http://www.hadronindustries.com/",
    namespace_packages = ["hadron"],
    packages = ["hadron.entanglement", "hadron.entanglement.sql"],
    install_requires = ['SQLAlchemy', 'pyOpenSSL', 'iso8601'],
    scripts = ['bin/entanglement-cli'],
    test_suite = "tests",
    version = 0.1,
)
