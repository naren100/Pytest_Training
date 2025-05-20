def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


# This is a basic pytest. Pytest needs to be installed in your app.
# It always begins with the Word "Test". Assert statement determines if the test
# has passed or failed.
# Any uncaught exception will cause the test to fail
# Assertion Error is what what you will get when a test cases fails
# The dot after test_one.py means that one test was run and it passed.
# Test files should be named test_<something>.py or <something>_test.py.
# Test methods and functions should be named test_<something>.
# Test classes should be named Test<Something>.
# What are the different Outcomes in Pytest?  Passed - Failed = Skipped - XFail - Error



